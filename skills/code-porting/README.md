# code-porting

跨工程代码移植 skill，**两段交互式**：交互1 生成"只动架构、不动实现"的分步移植方案（Mermaid 执行计划图），获批即止不执行；交互2 基于已批准方案输出 /goal 约束后逐步执行移植。

## 用法

```
/code-porting
```

开场先确认交互模式，然后按模式走：

- **交互1 生成方案**：手动输入四参数（源工程/目标工程/移植范围/用户要求）→ 分析 → 八段式方案 → Plan 批准 → 停止（询问是否进入交互2）。
- **交互2 按方案移植**：基于已批准方案 → /goal → 逐步执行 §五 计划，每步验证。

例：`/code-porting` → "交互1，把 6125 的电源管理移植到 cdc_7255" → 输入四参数 → 出方案。

## 流程

```
交互1: 0 输入确认(四参数) → 1 源解剖 → 2 目标盘点 → 3 熔接面分类+决策 → 4 防漏校验 → 5 Plan 出方案(获批即止)
交互2: (方案已批准) → 6 输出 /goal → 逐步执行 §五(每步验证) → 完成
```

四参数（源工程/目标工程/移植范围/用户要求）全部由用户手动输入，skill 不自行推断。

## 设计立场

- 移植不是重写：源代码只做 include 层名替换，目标已有代码只动极少数熔接面。
- 宁可多花 token 读源码/查台账，不可漏掉任何要移植的部分。
- DLP 透明加密环境下分析用 `scripts/port_scan.py`（Python 读明文），修改走 Edit/Write。

## 目录

| 路径 | 内容 |
|---|---|
| `SKILL.md` | 六阶段工作流路由 |
| `references/analysis-guide.md` | 源解剖/目标盘点/熔接面分类 |
| `references/completeness-check.md` | 七维防漏台账 + 双向核对 |
| `references/plan-template.md` | 八段式方案模板（§五 Mermaid 执行计划图） |
| `references/goal-format.md` | /goal 生成规则与执行纪律 |
| `scripts/port_scan.py` | 目录扫描（文件/行数/include 落点/DLP 密文检测） |
| `example/6125To7255电源管理移植.md` | 成品方案范例（八段式模板实测出处，随包分发） |
| `config/config.conf.example` | 本机默认值配置（复制为 config.conf 使用） |
| `output/` | 台账等分析产物（gitignore） |
