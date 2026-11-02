# -*- coding: utf-8 -*-
"""检查结果收集与打印。

一条结果 = (level, code, message)。level ∈ ERR / WARN / OK / INFO。
退出码约定：存在 ERR → 1，否则 0。
"""
import sys

ERR = "ERR"
WARN = "WARN"
OK = "OK"
INFO = "INFO"

_ICON = {ERR: "✗", WARN: "!", OK: "✓", INFO: "·"}


class Report:
    def __init__(self, title=""):
        self.title = title
        self.rows = []

    def add(self, level, code, msg):
        self.rows.append((level, code, msg))
        return self

    def err(self, code, msg):
        return self.add(ERR, code, msg)

    def warn(self, code, msg):
        return self.add(WARN, code, msg)

    def ok(self, code, msg):
        return self.add(OK, code, msg)

    def info(self, code, msg):
        return self.add(INFO, code, msg)

    def merge(self, other):
        self.rows.extend(other.rows)
        return self

    def count(self, level):
        return sum(1 for r in self.rows if r[0] == level)

    @property
    def exit_code(self):
        return 1 if self.count(ERR) else 0

    def passed(self):
        return self.exit_code == 0

    def dump(self, stream=None):
        stream = stream or sys.stdout
        if self.title:
            stream.write("\n== %s ==\n" % self.title)
        for level, code, msg in self.rows:
            if level == OK and self.count(ERR):
                continue          # 有错时只显示问题项，避免噪声
            stream.write("  %s [%s] %s\n" % (_ICON[level], code, msg))
        stream.write("\n  汇总: %d 错误 / %d 告警 / %d 通过\n"
                     % (self.count(ERR), self.count(WARN), self.count(OK)))
        return self.exit_code
