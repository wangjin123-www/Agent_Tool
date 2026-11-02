# -*- coding: utf-8 -*-
"""本地控制台服务：托管 utils/protocol_console.html + JSON API（无新增依赖）。

    python cli.py console [--port 8765]      # 浏览器打开 http://127.0.0.1:8765

页面本身是静态单文件（utils/protocol_console.html），所有能力都回落到本进程的
现成函数，不重写业务逻辑：

    GET  /api/meta                     服务/方向/语言/子表信息（下拉框用）
    GET  /api/query?keyword=接口名      ④ 查询：scripts.query.search
    POST /api/edit    {ops,dry_run,force}  ② 修改：scripts.edit.apply_ops
    POST /api/sync    {dry}              ① 校验：scripts.rules.run_sync
    POST /api/parse   {lang}             ③ 解析：scripts.parse.parse_protocol + 生成
    POST /api/gen     {lang}             ③ 只生成代码
    GET  /check_report.html              已有校验报告（有 ERR/WARN 时才存在）
"""
import json
import os
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from .common import conf, feishu
from .parse import parse_protocol
from . import gen as gen_mod
from . import query as query_mod
from . import report as report_mod
from . import rules

PAGE = os.path.join(conf.SKILL_DIR, "utils", "protocol_console.html")


def _meta():
    cfg = conf.proto()
    proto = parse_protocol(cfg)
    return {
        "spreadsheet": cfg.get("spreadsheet", ""),
        "svcs": [{"name": s.name, "id_hex": "0x%02X" % s.id if s.id is not None else "",
                  "namespace": s.namespace, "desc": s.desc} for s in proto.services],
        "directions": ["SOC→MCU", "MCU→SOC"],
        "if_types": ["event", "method", "method(rr)"],
        "langs": [{"name": k, "label": v, "status": st}
                  for k, v, st in gen_mod.available()],
        "counts": proto.counts(),
        "revision": proto.source.get("revision"),
        "report": os.path.exists(conf.output_path(report_mod.PATH)),
    }


def _edit(body):
    from .edit import apply_ops
    ops = body.get("ops") or []
    if not ops:
        raise ValueError("ops 为空")
    return apply_ops({"ops": ops},
                     execute=not body.get("dry_run", False),
                     force=bool(body.get("force")))


def _sync(body):
    dry = bool(body.get("dry", False))
    total, fixed, ctx = rules.run_sync(dry=dry, materialize=not dry)
    path = None if dry else report_mod.emit(total, ctx)
    return {"dry": dry, "err": total.count("ERR"), "warn": total.count("WARN"),
            "ok": total.count("OK"), "fixed": fixed,
            "report": path, "rows": [[lv, code, msg] for lv, code, msg in total.rows
                                     if lv in ("ERR", "WARN")]}


def _parse(body):
    proto = parse_protocol()
    path = proto.save()
    lang = body.get("lang") or "none"
    signed = gen_mod.generate(langs=lang, proto=proto)
    return {"protocol": path, "revision": proto.source.get("revision"),
            "counts": proto.counts(),
            "generated": {k: v for k, v in signed.items()}}


def _gen(body):
    return {"generated": gen_mod.generate(langs=body.get("lang") or "c")}


def _dispatch(method, path, qs, body):
    if path == "/api/meta" and method == "GET":
        return _meta()
    if path == "/api/query" and method == "GET":
        kw = (qs.get("keyword") or [""])[0]
        if not kw.strip():
            raise ValueError("缺 keyword")
        return query_mod.search(kw)
    if path == "/api/edit" and method == "POST":
        return _edit(body)
    if path == "/api/sync" and method == "POST":
        return _sync(body)
    if path == "/api/parse" and method == "POST":
        return _parse(body)
    if path == "/api/gen" and method == "POST":
        return _gen(body)
    raise LookupError("未知接口: %s %s" % (method, path))


class Handler(BaseHTTPRequestHandler):
    server_version = "ProtoConsole/1.0"

    def log_message(self, fmt, *a):          # 只打 API 调用，静态文件不刷屏
        if "/api/" in (self.path or ""):
            sys.stderr.write("%s %s\n" % (self.command, self.path))

    # ---------------------------------------------------------- 输出
    def _send(self, code, payload, ctype="application/json; charset=utf-8"):
        raw = payload if isinstance(payload, bytes) else \
            json.dumps(payload, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def _file(self, path, ctype="text/html; charset=utf-8"):
        if not os.path.exists(path):
            self._send(404, {"error": "文件不存在: %s" % os.path.basename(path)})
            return
        with open(path, "rb") as f:
            self._send(200, f.read(), ctype)

    # ---------------------------------------------------------- 路由
    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ("/", "/index.html"):
            self._file(PAGE)
            return
        if u.path == "/check_report.html":
            self._file(conf.output_path(report_mod.PATH))
            return
        try:
            self._send(200, _dispatch("GET", u.path, parse_qs(u.query), {}))
        except LookupError as e:
            self._send(404, {"error": str(e)})
        except Exception as e:                       # 业务异常原样回前端展示
            self._send(500, {"error": "%s: %s" % (type(e).__name__, e)})

    def do_POST(self):
        u = urlparse(self.path)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n) or b"{}")
        except (ValueError, TypeError) as e:
            self._send(400, {"error": "请求体非 JSON: %s" % e})
            return
        try:
            self._send(200, _dispatch("POST", u.path, parse_qs(u.query), body))
        except LookupError as e:
            self._send(404, {"error": str(e)})
        except Exception as e:
            self._send(500, {"error": "%s: %s" % (type(e).__name__, e)})


def serve(port=8765, open_browser=True):
    if not os.path.exists(PAGE):
        print("缺少页面文件: %s" % PAGE)
        return 2
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = "http://127.0.0.1:%d/" % port
    print("协议控制台 → %s（Ctrl+C 停止）" % url)
    print("校验报告   → %scheck_report.html" % url)
    if open_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
    finally:
        srv.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(serve(int(sys.argv[1]) if len(sys.argv) > 1 else 8765))
