# -*- coding: utf-8 -*-
"""config/protocol.schema.json 的轻量执行器（校验手段 B）。

只实现本 schema 用到的 JSON Schema 关键字子集：
  type（含联合数组）/ required / properties / items / enum /
  minimum / maximum / pattern / $ref（仅 #/definitions/... 内部引用）
不引入 jsonschema 第三方依赖；schema 文件本身仍是标准 draft-07 写法，
以后接入完整库时可整体替换本模块的 validate()。

用法：
    errors = validate(data, schema)   # [] 即通过；否则 ["$.services[0].name: ..."]
"""
import re

_TYPE_OK = {
    "object": dict, "array": list, "string": str,
    "integer": int, "number": (int, float), "boolean": bool, "null": type(None),
}


def _resolve(schema, root):
    """展开 $ref（只支持 #/definitions/... 本文件内引用）。"""
    seen = 0
    while isinstance(schema, dict) and "$ref" in schema and seen < 10:
        ref = schema["$ref"]
        node = root
        for part in ref.lstrip("#/").split("/"):
            node = node[part]
        schema = node
        seen += 1
    return schema


def _type_ok(node, t):
    if t == "null":
        return node is None
    py = _TYPE_OK.get(t)
    if py is None:
        return True           # 未知类型名：放行（宽松）
    if isinstance(node, bool) and t in ("integer", "number"):
        return False          # bool 是 int 子类，显式排除
    return isinstance(node, py)


def validate(node, schema, path="$", root=None):
    """返回错误信息列表（空 = 通过）。"""
    root = root if root is not None else schema
    schema = _resolve(schema, root)
    if not isinstance(schema, dict):
        return []
    errs = []

    t = schema.get("type")
    if t:
        types = t if isinstance(t, list) else [t]
        if not any(_type_ok(node, x) for x in types):
            return ["%s: 类型应为 %s，实际 %s" % (path, "|".join(types), type(node).__name__)]

    if "enum" in schema and node not in schema["enum"]:
        errs.append("%s: 取值 %r 不在 %s 内" % (path, node, schema["enum"]))

    if isinstance(node, dict):
        for key in schema.get("required", []):
            if key not in node:
                errs.append("%s: 缺必填键 %r" % (path, key))
        for key, sub in (schema.get("properties") or {}).items():
            if key in node:
                errs.extend(validate(node[key], sub, "%s.%s" % (path, key), root))

    if isinstance(node, list) and "items" in schema:
        for i, item in enumerate(node):
            errs.extend(validate(item, schema["items"], "%s[%d]" % (path, i), root))

    if isinstance(node, (int, float)) and not isinstance(node, bool):
        if "minimum" in schema and node < schema["minimum"]:
            errs.append("%s: %s 小于最小值 %s" % (path, node, schema["minimum"]))
        if "maximum" in schema and node > schema["maximum"]:
            errs.append("%s: %s 大于最大值 %s" % (path, node, schema["maximum"]))

    if isinstance(node, str) and "pattern" in schema:
        if not re.search(schema["pattern"], node):
            errs.append("%s: %r 不匹配 %r" % (path, node, schema["pattern"]))
    return errs
