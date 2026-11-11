# -*- coding: utf-8 -*-
"""最小回归：不联网、不写表，只锁住「解析往返 / 配置派生 / 规则判据 / 只读闸门」。

跑法：python -m unittest discover -s tests -v
"""
import os
import sys
import unittest
from unittest import mock

_HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(_HERE)
sys.path.insert(0, SKILL_DIR)

from scripts.common import conf, feishu            # noqa: E402
from scripts.model import Protocol                 # noqa: E402
from scripts.rules import precheck as pre          # noqa: E402


class _FakeProto:
    def __init__(self, enums=None, structs=None, source=None):
        self.enums = enums or []
        self.structs = structs or []
        self.source = source or {}

    def find_struct(self, name):
        return next((s for s in self.structs if getattr(s, "name", s) == name), None)

    def find_enum(self, name):
        return next((e for e in self.enums if getattr(e, "name", e) == name), None)


class _FakeCtx:
    def __init__(self, enums=None, structs=None, source=None):
        self.proto = _FakeProto(enums, structs, source)
        self.pending_structs = set()
        self.pending_enums = set()


class T1ProtocolRoundTrip(unittest.TestCase):
    """output/protocol.json 是黄金样本：to_dict → from_dict → to_dict 必须逐键相等。"""

    def test_round_trip(self):
        path = conf.PROTO_JSON
        if not os.path.exists(path):
            self.skipTest("无 protocol.json，先跑 cli.py parse")
        p = Protocol.load(path)
        again = Protocol.from_dict(p.to_dict()).to_dict()
        self.assertEqual(p.to_dict(), again)
        # 计数不得为 0（防「解析器静默失败但没报错」）
        c = p.counts()
        for k in ("services", "interfaces", "structs", "enums"):
            self.assertGreater(c[k], 0, "protocol.json 的 %s 为 0" % k)


class T4PrecheckRules(unittest.TestCase):
    """写表前预检：纯函数，用伪造 ctx + ops 断言判据。"""

    def _codes(self, op, enums=None, structs=None):
        return [i.rule_id for i in pre._precheck(_FakeCtx(enums, structs), op)]

    def test_mod_interface_allows_shared_columns(self):
        # 关键回归：precheck 与 apply 共用 conf.MOD_INTERFACE_COLUMNS，
        # struct 参数写入的 N/O/P 必须放行（此前只到 M，会把自动修挡在门外）。
        for col in ("N", "O", "P", "Q"):
            self.assertNotIn("SEC", self._codes(
                {"kind": "mod_interface", "name": "X", "fields": {col: "v"}}),
                "列 %s 应被允许" % col)
        self.assertIn("SEC", self._codes(
            {"kind": "mod_interface", "name": "X", "fields": {"A": "v"}}))

    def test_add_enum_value_format(self):
        ok = {"kind": "add_enum", "name": "E", "msg_id": "0x0101",
              "values": [{"value": "0x0A", "c_name": "E_A"}]}
        self.assertEqual(self._codes(ok), [])
        bad = {"kind": "add_enum", "name": "E", "msg_id": "0x0101",
               "values": [{"value": "10", "c_name": "E_A"}]}
        self.assertIn("R23", self._codes(bad))

    def test_add_struct_byte_continuity(self):
        ok = {"kind": "add_struct", "name": "S",
              "members": [{"byte": "0-1B", "name": "a", "type": "uint16"},
                          {"byte": "2B", "name": "b", "type": "uint8"}]}
        self.assertEqual(self._codes(ok), [])
        gap = {"kind": "add_struct", "name": "S",
               "members": [{"byte": "0-1B", "name": "a", "type": "uint16"},
                           {"byte": "3B", "name": "b", "type": "uint8"}]}
        self.assertIn("S11", self._codes(gap))

    def test_param_ref_must_exist_before_write(self):
        # 「SI 有参数但 DS 没有该 struct」必须在写表前拦（S08 同源判据），
        # 而不是落表后等 sync 报。struct:/enum: 引用均查。
        _NS = type("S", (), {"name": "KnownStruct"})
        op = {"kind": "add_interface", "name": "X",
              "params": [{"name": "p1", "type": "struct:GhostStruct"},
                         {"name": "p2", "type": "enum:GhostEnum"}]}
        codes = [i.rule_id for i in pre._precheck(_FakeCtx(structs=[_NS()]), op)]
        self.assertIn("S08", codes)
        self.assertIn("S09", codes)
        # 已存在的引用放行
        ok = {"kind": "add_interface", "name": "X",
              "params": [{"name": "p1", "type": "struct:KnownStruct"}]}
        self.assertNotIn("S08", self._codes(ok, structs=[_NS()]))
        # mod_interface 改 N/O 指向不存在的 struct 同样拦
        mod = {"kind": "mod_interface", "name": "X",
               "fields": {"N": "GhostStruct", "O": "struct"}}
        self.assertIn("S08", self._codes(mod))

    def test_param_ref_allows_same_batch_definition(self):
        # 同批 add_struct → add_interface 引用新 struct 是合法序列（pending 放行）
        ctx = _FakeCtx()
        ctx.pending_structs.add("NewStruct")
        op = {"kind": "add_interface", "name": "X",
              "params": [{"name": "p1", "type": "struct:NewStruct"}]}
        codes = [i.rule_id for i in pre._precheck(ctx, op)]
        self.assertNotIn("S08", codes)


class T5ReadOnlyGate(unittest.TestCase):
    """--dry-run 的只读是结构保证：写函数必须抛 ReadOnlyError。"""

    def tearDown(self):
        feishu.set_read_only(False)

    def test_write_blocked(self):
        feishu.set_read_only(True)
        with self.assertRaises(feishu.ReadOnlyError):
            feishu.write_cells(conf.proto(), "service_interface", "A1", [["x"]])
        with self.assertRaises(feishu.ReadOnlyError):
            feishu.apply_styles(conf.proto(), "parameter_enum",
                                [{"range": "A1:E1", "font_size": 9}])
        with self.assertRaises(feishu.ReadOnlyError):
            feishu.insert_rows(conf.proto(), "service_interface", 2, 1)

    def test_write_allowed_when_not_read_only(self):
        feishu.set_read_only(False)
        self.assertFalse(feishu.is_read_only())


class T6CheckerDoesNotWrite(unittest.TestCase):
    """规则 2 的契约：checker 传 sink 时只产出修复意图，绝不自己调写接口。"""

    def test_enum_style_sink(self):
        from scripts.check import enum_style as sty

        proto = type("P", (), {"enums": [
            type("E", (), {"name": "E1", "pe_row": 3, "items": []})()]})()
        with mock.patch.object(sty.feishu, "read_range", return_value=[]), \
             mock.patch.object(sty.feishu, "apply_styles") as w:
            sink = {}
            rep = sty.validate({}, proto, repair=True, sink=sink)
            w.assert_not_called()
        self.assertEqual(sink["styles"][0][0], "parameter_enum")
        self.assertTrue(sink["styles"][0][1])
        self.assertTrue(rep.rows)

    def test_merge_sink(self):
        from scripts.check import blocks as blk

        rows = [{}] * 8
        rows[5] = [{"value": "SvcA"}]                    # 第 6 行：服务首行（块首）
        rows[7] = [{}] * 4 + [{"value": "X"}]            # 第 8 行：E 列接口名（块尾）
        with mock.patch.object(blk.feishu, "cli",
                               return_value={"data": {"merged_cells": []}}), \
             mock.patch.object(blk.feishu, "unmerge") as u, \
             mock.patch.object(blk.feishu, "merge") as m:
            sink = {}
            blk.validate(dry=False, rows=rows, sink=sink)
            u.assert_not_called()
            m.assert_not_called()
        sheet_key, unmerge_rng, merge_rngs = sink["merges"][0]
        self.assertEqual(sheet_key, "service_interface")
        self.assertEqual(unmerge_rng, "A6:D8")
        self.assertEqual(merge_rngs, ["A6:A8", "B6:B8", "C6:C8", "D6:D8"])


def _si_rows(cfg, *entries):
    """伪造 SI 行（A..Q 17 列）：entries = [(行号, {列: 文本})]。"""
    start = cfg["si_data_start_row"]
    rows = [[{} for _ in range(17)] for _ in range(max(start - 1, 0) + max(
        (r for r, _ in entries), default=start))]
    for r, cells in entries:
        for col, text in cells.items():
            idx = ord(col) - ord("A")
            rows[r - 1][idx] = {"value": text} if text else {}
    return rows


class T7DirectionFromBit15(unittest.TestCase):
    """方向真源 = msg_id bit15（0x8000=MCU→SOC / 0=SOC→MCU）；分节行只是排版。"""

    def _parse(self, entries):
        from scripts.model import Protocol
        from scripts.parse.sheet_reader import parse_si
        cfg = conf.proto()
        proto = Protocol()
        proto.source["parse_stats"] = {k: {"rows": 0, "skipped": []}
                                       for k in ("si", "ds", "pe")}
        parse_si(cfg, _si_rows(cfg, *entries), proto)
        return proto

    def test_direction_from_msg_id_not_section(self):
        # 同在 SOC→MCU 分节下：0x0101 → SOC_TO_MCU；0x8101（bit15=1）→ MCU_TO_SOC
        cfg = conf.proto()
        proto = self._parse([
            (6, {"E": cfg["section"]["soc_to_mcu"]}),
            (7, {"E": "QueryMtd", "J": "0x0101"}),
            (8, {"E": "OddEvt", "J": "0x8101"}),      # 方向位与分节不符 → 只记 section_dir
        ])
        itfs = [i for s in proto.services for i in s.interfaces]
        self.assertEqual(itfs[0].direction, "SOC_TO_MCU")
        self.assertEqual(itfs[0].section_dir, "SOC_TO_MCU")
        self.assertEqual(itfs[1].direction, "MCU_TO_SOC")   # 真源 bit15，不受分节影响
        self.assertEqual(itfs[1].section_dir, "SOC_TO_MCU")  # 排版参考如实记录

    def test_missing_msg_id_falls_back_to_section(self):
        cfg = conf.proto()
        proto = self._parse([
            (6, {"E": cfg["section"]["mcu_to_soc"]}),
            (7, {"E": "NoIdEvt"}),                    # J 列空 → 分节位置兜底
        ])
        itf = proto.services[0].interfaces[0]
        self.assertEqual(itf.direction, "MCU_TO_SOC")

    def test_dangling_param_recorded_in_parse_stats(self):
        cfg = conf.proto()
        proto = self._parse([
            (6, {"E": cfg["section"]["soc_to_mcu"]}),
            (7, {"N": "p1"}),                         # 分节行后无接口 → 悬空参数，必须留痕
        ])
        sk = proto.source["parse_stats"]["si"]["skipped"]
        self.assertEqual(len(sk), 1)
        self.assertEqual(sk[0][0], 7)
        self.assertIn("参数行无所属接口", sk[0][1])

    def test_cov_rule_warns_on_skipped(self):
        from scripts.rules.legacy import _cov_report
        ctx = _FakeCtx(source={"parse_stats": {
            "si": {"rows": 10, "skipped": [(12, "参数行无所属接口（E 列空且上方无接口行）：N='x' O=''")]},
            "ds": {"rows": 5, "skipped": []},
            "pe": {"rows": 8, "skipped": []},
        }})
        rep = _cov_report(ctx)
        warns = [m for lvl, _c, m in rep.rows if lvl == "WARN"]
        self.assertEqual(len(warns), 1)
        self.assertIn("si 行12", warns[0])

    def test_cov_rule_ok_when_clean(self):
        from scripts.rules.legacy import _cov_report
        ctx = _FakeCtx(source={"parse_stats": {
            "si": {"rows": 91, "skipped": []},
            "ds": {"rows": 34, "skipped": []},
            "pe": {"rows": 116, "skipped": []},
        }})
        rep = _cov_report(ctx)
        self.assertEqual(rep.rows[0][0], "OK")
        self.assertIn("si 91 行", rep.rows[0][2])


class T8SchemaGuard(unittest.TestCase):
    """校验手段 B：config/protocol.schema.json 在 save()/load() 双向拦截。"""

    def _schema(self):
        import json
        with open(conf.rel("config", "protocol.schema.json"), encoding="utf-8") as f:
            return json.load(f)

    def test_lite_validator_basics(self):
        from scripts.model.jsonschema_lite import validate
        s = self._schema()
        node = {"schema_version": "1.1.0", "source": {"spreadsheet": "t", "spreadsheet_token": "k", "revision": 1},
                "services": [], "structs": [], "enums": []}
        self.assertEqual(validate(node, s), [])
        bad = dict(node)
        bad["schema_version"] = "abc"
        self.assertTrue(any("schema_version" in e for e in validate(bad, s)))
        node["services"] = [{"name": "S", "id": 1, "id_hex": "0x01", "interfaces": [
            {"name": "I", "direction": "SIDEWAYS", "msg_id": 1, "msg_id_hex": "0x0001"}]}]
        self.assertTrue(any("direction" in e for e in validate(node, s)))

    def test_save_rejects_bad_direction(self):
        from scripts.model.protocol import SchemaError
        p = Protocol.load(conf.PROTO_JSON)            # 现网 json 本身必须能通过 load
        itf = next(p.all_interfaces())
        itf.direction = "SIDEWAYS"                    # 破坏契约
        with self.assertRaises(SchemaError):
            p.save(os.path.join(conf.OUTPUT_DIR if hasattr(conf, "OUTPUT_DIR") else "output",
                                "_schema_bad.json"))


class T9UnifiedInterfaces(unittest.TestCase):
    """去重后的统一性：配置与工具函数只有一份实现。"""

    def test_col_letter_inverse_of_col_index(self):
        for i in range(0, 30):
            self.assertEqual(conf.col_index(conf.col_letter(i)), i)


if __name__ == "__main__":
    unittest.main()
