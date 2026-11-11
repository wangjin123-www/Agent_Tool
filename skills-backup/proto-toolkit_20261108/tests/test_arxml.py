# -*- coding: utf-8 -*-
"""ARXML 后端最小回归：生成、命名空间、引用闭合、确定性。"""
import os
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

_HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(_HERE)
sys.path.insert(0, SKILL_DIR)

from scripts.common import conf                 # noqa: E402
from scripts.gen import lang_arxml              # noqa: E402
from scripts.model import Protocol              # noqa: E402

NS = "http://autosar.org/schema/r4.0"
REF_TAGS = {"TYPE-TREF", "BASE-TYPE-REF", "COMPU-METHOD-REF",
            "IMPLEMENTATION-DATA-TYPE-REF", "APPLICATION-DATA-TYPE-REF"}


def _ln(e):
    return e.tag.rsplit("}", 1)[-1]


class T5ArxmlGenerate(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(conf.PROTO_JSON):
            self.skipTest("无 protocol.json，先跑 cli.py parse")
        self.proto = Protocol.load(conf.PROTO_JSON)
        self.gcfg = conf.codegen_lang("arxml")
        self.root = conf.lang_root("arxml")

    def _gen(self, out_dir):
        cfg = dict(self.gcfg)
        cfg["output_dir"] = out_dir
        paths = lang_arxml.generate(self.proto, cfg, self.root)
        self.assertEqual(len(paths), 1)
        return paths[0]

    def test_generate_and_refs(self):
        with tempfile.TemporaryDirectory() as td:
            path = self._gen(td)
            with open(path, "rb") as f:
                data = f.read()
            root = ET.fromstring(data)
            self.assertEqual(root.tag, "{%s}AUTOSAR" % NS)

            # 基本对象不能为 0（防生成器静默退化成空文件）
            counts = {}
            for e in root.iter():
                counts[_ln(e)] = counts.get(_ln(e), 0) + 1
            for tag in ("APPLICATION-PRIMITIVE-DATA-TYPE",
                        "APPLICATION-RECORD-DATA-TYPE",
                        "IMPLEMENTATION-DATA-TYPE",
                        "SENDER-RECEIVER-INTERFACE",
                        "CLIENT-SERVER-INTERFACE",
                        "DATA-TYPE-MAP"):
                self.assertGreater(counts.get(tag, 0), 0, tag)

            # 引用闭合：/CDC7255 下的引用必须能找到定义
            defined = {}
            pkgs = root.find("{%s}AR-PACKAGES" % NS)
            for pkg in pkgs:
                if _ln(pkg) == "AR-PACKAGE":
                    self._collect(pkg, "", defined)
            bad = []
            for e in root.iter():
                if _ln(e) in REF_TAGS:
                    ref = (e.text or "").strip()
                    if ref.startswith("/AUTOSAR_Platform"):
                        continue
                    if ref not in defined:
                        bad.append(ref)
            self.assertEqual(bad, [], "未解析引用: %r" % bad[:10])

    def test_deterministic(self):
        with tempfile.TemporaryDirectory() as td1, tempfile.TemporaryDirectory() as td2:
            with open(self._gen(td1), "rb") as f1, open(self._gen(td2), "rb") as f2:
                a, b = f1.read(), f2.read()
            self.assertEqual(a, b, "同一 protocol.json 两次生成必须逐字节相同")

    @staticmethod
    def _collect(pkg, parent, defined):
        sn = pkg.find("{%s}SHORT-NAME" % NS)
        path = parent + "/" + (sn.text if sn is not None else "?")
        els = pkg.find("{%s}ELEMENTS" % NS)
        if els is not None:
            for ch in els:
                csn = ch.find("{%s}SHORT-NAME" % NS)
                name = csn.text if csn is not None else "?"
                defined[path + "/" + name] = _ln(ch)
        ps = pkg.find("{%s}AR-PACKAGES" % NS)
        if ps is not None:
            for s in ps:
                if _ln(s) == "AR-PACKAGE":
                    T5ArxmlGenerate._collect(s, path, defined)


if __name__ == "__main__":
    unittest.main()
