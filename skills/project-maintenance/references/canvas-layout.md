# Canvas 排版与防重叠规范

> 适用:doc-audit 模式判定需要生成/修改 `.canvas` 时。
> 目标:**文字不溢出、节点不重叠、边标签不压节点、group 不压外部节点**。
> 工具:`python scripts/canvas_layout.py <check|layout> <file.canvas>`

## 1. 参考来源(GitHub / 官方)

- **JSON Canvas 1.0 规范**(节点/边/坐标/group 语义):
  https://github.com/obsidianmd/jsoncanvas
  - `x/y` 是节点左上角,`x` 向右、`y` 向下;group 只是视觉容器,不参与自动布局。
- **Canvas Positioning Toolkit**(Obsidian 插件,网格自动排列;行高取该行最高卡片,混合高度不重叠):
  https://github.com/valleytheknight/Canvas-Positioning-Toolkit
- **Flashcard Canvas**(按箭头做树形 Tidy 布局,子节点列在右侧):
  https://github.com/jcesguerram/flashcard-canvas
- **Overpowered Canvas**(分层流程图/径向布局,碰撞规避):
  https://www.obsidianstats.com/plugins/overpoweredcanvas
- **AgriciDaniel/claude-obsidian canvas skill**(自动定位、零重叠校验;布局常量参考):
  https://github.com/AgriciDaniel/claude-obsidian

采用的核心做法:**文本按内容估尺寸 → 分层/网格排布 → 行高取最高 → 校验零重叠**。

## 2. 硬规则(生成/修改 Canvas 必须满足)

### 2.1 文本节点尺寸

- 不得随手写 200×80 塞多行中文。先按内容估算:
  - CJK 记 2 unit、ASCII 记 1 unit;宽度 ≈ `max_line_units × 8 + 40`。
  - 高度 ≈ `行数 × 24 + 32`。
  - 最小 240×80;长说明 480–680 宽。
- 状态说明、模块职责等多行卡片优先用 260–320 宽、按行数加高。

### 2.2 间距

| 对象 | 最小间距 |
|---|---|
| 同层节点水平 | 100px |
| 层间垂直(有边标签) | **140px** |
| group 内边距 | 40px(顶部另留 40px 给 group label) |
| group / 顶层节点之间 | 240px |
| 无标签的自由网格 | 水平 80px、垂直 80px |

### 2.3 边标签

- Obsidian 把边标签画在边路径中点,**标签没有偏移参数**,长标签会压节点/自动换行;不能靠“差不多够宽”来赌。
- **单条边标签 ≤ 24 units(约 12 个汉字)**。超长条件按下面两种方式之一处理:
  1. **短编号 + 图例节点(推荐)**:边上只写 `T1`/`T2`(≤4 字符),旁边放一个 text 节点写 `T1=...` 的完整条件;
  2. 把条件直接写进源/目标状态节点的正文。
- 同一通道不要放两条反向长标签;即使合并成 `A↔B`,也建议改成 `T#` + 图例,避免 Obsidian 因字体/换行压到节点。
- **边标签之间也不得重叠**;双向边共用同一走廊时,合并标签或改用不同 `fromSide/toSide`。
- 边不要穿过无关节点;跨层边尽量走层间空白带。
- 图例节点放在空白区(如主图左侧/右侧),按正文尺寸给足宽高,不要让图例压到 group/节点。

### 2.4 边颜色（单向 / 双向）

- **单向边**：`"color": "4"`（绿）。
- **双向边**：同一对节点同时存在 `A→B` 和 `B→A` 时，**两条边都用 `"color": "6"`（紫）**。
- Obsidian 的边没有线型参数，颜色是唯一稳定的单向/双向区分方式，不要只靠箭头方向。
- `canvas_layout.py colorize <file>` 自动分类上色；`layout` 也会自动上色；`check` 会校验颜色是否符合该规则。
- 同向重复边（A→B 两条）仍按单向处理；双向判定只看是否存在两个相反方向。

### 2.5 group

- group 内的节点必须被 group 框包住;group 框 = 子节点包围盒 + 40px 内边距 + 40px 顶部标签区。
- group 之间不得重叠;group 不得压到不属于它的节点。
- **固定色带式架构图**(6 横向层 + L6 竖条)按 `doc-audit-workflow.md` §3.4 的人工风格排版,**只用 `check`,不要用 `layout`**,否则会打乱色带。

## 3. 工具用法

### 检查(所有 Canvas 保存前必须跑)

```bash
python scripts/canvas_layout.py check <file.canvas>
```

输出 `OK` 才允许保存;出现 `WARN` 必须修:

| 告警 | 处理 |
|---|---|
| 文本可能溢出 | 按建议尺寸放大节点,或删减文字 |
| 节点重叠 / group 重叠 / group 压外部节点 | 调坐标;流程图可跑 `layout` 初排 |
| 边标签过长(>24 units) | 改成 `T1/T2` 短编号 + 图例节点,或把条件写进节点正文 |
| 边标签可能压到节点 | 调节点间距/换 side/缩短标签 |
| 边标签重叠 | 合并双向边标签,或换 `fromSide/toSide` 错开 |
| 边颜色不符合单向/双向 | 跑 `canvas_layout.py colorize <file>` 自动上色 |

### 自动布局(仅流程图/状态机图)

```bash
python scripts/canvas_layout.py layout <file.canvas> [--out <new.canvas>] [--direction TB|LR]
```

- 自动放大 text 节点;
- group 内按内部边做 DFS 断环 + 最长路径分层;group 之间横向排列;
- 自动选 `fromSide/toSide`;
- 输出后**必须再跑 `check`**;标签过长/压节点仍需人工微调。

> `layout` 是初排工具,不保证语义分组完全正确(它按原始坐标中心判断 group 归属);状态机/流程图跑完要人工复核 group 成员和边走向。**嵌套 group 不支持**,多层 group 的图请人工排版,只用 `check` 校验。

## 4. 快速自检清单

- [ ] `canvas_layout.py check` 输出 `OK`
- [ ] 每个 text 节点文字完整显示,没有被裁剪
- [ ] 节点之间、group 之间无重叠
- [ ] group 包住自己的节点,没压外部节点
- [ ] 边标签没有压住任何节点/其他标签
- [ ] 长条件已移到正文或备注节点
- [ ] 固定色带架构图没有被 `layout` 打乱
