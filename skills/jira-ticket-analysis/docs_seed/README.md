# docs_seed/ —— 分层 CLAUDE.md 投放点

放**已生成好的** CLAUDE.md 文档，供流水线播种缓存，省掉首次的现场生成。

## 目录结构

按 `<repo名>@<branch>/` 一个工程一个目录，内部**按分析范围（scope）为根**组织 ——
也就是把 `analysis_scope` 那一层的 CLAUDE.md 放在根，不要多套一层：

```
docs_seed/
└── ae_mcu_general_platform@Mcu_GeneralPlatform_YB103/
    ├── CLAUDE.md                          ← scope 根（FreeRTOS_S32K312 层的）
    ├── CVI_McuPlatform/
    │   ├── CLAUDE.md
    │   ├── L1_Applications/CLAUDE.md
    │   ├── L2_Tasks/CLAUDE.md
    │   ├── L3_RTOS/CLAUDE.md
    │   ├── L4_Services/CLAUDE.md
    │   └── L5_EcuAL/CLAUDE.md
    ├── HSE/CLAUDE.md
    ├── inc/CLAUDE.md
    └── ...
```

`<repo名>` 取 GitLab 项目路径的最后一段（如
`ae_mcu_projects/platform/ae_mcu_general_platform` → `ae_mcu_general_platform`），
`<branch>` 就是 `config.json` 里配的分支名。

## 两种来源，任选其一

| 来源 | 做法 | 适用 |
|---|---|---|
| **A. 预放**（首选，快） | 手工把已生成好的 CLAUDE.md 按上面结构放进来 | 已跑过一次 `claude-md-map` 全量 INIT 的工程 |
| **B. 现场生成** | 什么都不放，直接跑 `./jtat.cmd run` | 新工程。会用内置的 `vendor/claude-md-map/mdmap.py` 走 `detect→scan→plan→brief`，再由 Claude 会话派 subagent 写 draft 并 `install` |

B 路径需要 Claude 会话介入一轮（因为 CLAUDE.md 正文由 subagent 撰写，不是纯确定性计算）。
A 路径则完全离线，秒级完成。

## 注意

- **只放 CLAUDE.md 文档本身**。代码永远由工具从 GitLab 取到自己的 `workspace/`，
  与任何本地 clone 无关 —— 这是刻意的隔离设计。
- 播种只发生**缓存未命中**时。若 `workspace/claude_md_cache/<repo>@<branch>/` 已有内容，
  会走「缓存命中 → 铺进快照 + 增量刷新」那条路，本目录不参与。
- 想强制重新播种：删掉 `workspace/claude_md_cache/<repo>@<branch>/` 再跑。
- 缓存键是 `<repo>@<branch>`（不是 sha），所以换了 commit 不会导致重新播种。
