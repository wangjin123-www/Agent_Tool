# Java 代码生成（待实现）

本目录是多语言代码生成的 **Java 插槽**，当前只放骨架，不产出任何文件。

## 目录约定（新增语言照此复制）

```
codegen/java/
├── config/codegen_config.json    # 输入 protocol.json、输出目录、模板→文件名映射
├── templates/                    # Jinja2 模板（*.j2）
└── generated/                    # 生成物，禁手改
```

## 接入步骤（三步）

1. **写生成器**：`scripts/gen/lang_java.py`，导出一个
   `generate(proto, gcfg, root) -> list[str]`（proto=协议模型，gcfg=本目录 config 内容，
   root=`codegen/java` 绝对路径；返回写出的文件绝对路径）。
   可直接复用 `scripts/gen/lang_c.py` 里的 `build_view()` 思路，按 Java 语法重算视图，
   再用 `jinja2.StrictUndefined` 渲染两次比对 md5（确定性自检）。
2. **填配置**：`codegen/java/config/codegen_config.json` 的 `file_names`
   （形如 `{"dto_java": "ProtoDtos.java", ...}`）与 `output_dir`。
3. **改注册表**：`codegen/config/languages.json` 里把 `java.status` 由 `todo` 改 `ready`。

改完即可用：

```powershell
& $PY scripts\cli.py parse --lang java
& $PY scripts\cli.py gen --lang java
```

## 红线

- `generated/` 是生成物，禁手改（下次 gen 覆盖）。
- 模板零逻辑：分支/映射全部在 Python 侧算好，模板只做拼装（与 C 一致）。
- 同一 protocol.json 两次渲染必须逐字节相同（时间戳/随机数一律禁止）。
- 输入只有 `output/protocol.json`，不得直读飞书表（表 → json 由 `parse` 负责）。
