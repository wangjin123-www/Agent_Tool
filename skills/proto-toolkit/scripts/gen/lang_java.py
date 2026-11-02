# -*- coding: utf-8 -*-
"""Java 语言生成器（插槽）：尚未实现，调用即报明确错误。

实现方式见 codegen/java/README.md：写 generate(proto, gcfg, root) 后，
把 codegen/config/languages.json 的 java.status 改成 ready 即可生效。
"""
import os


def generate(proto, gcfg, root):
    raise SystemExit(
        "语言 java 的生成器尚未实现：\n"
        "  1) 写 scripts/gen/lang_java.py 的 generate(proto, gcfg, root)，返回写出的文件路径列表\n"
        "  2) 模板放 %s\n"
        "  3) 输出目录见 %s 的 output_dir\n"
        "  4) 把 codegen/config/languages.json 里 java.status 改为 ready"
        % (os.path.join(root, "templates"),
           os.path.join(root, "config", "codegen_config.json")))
