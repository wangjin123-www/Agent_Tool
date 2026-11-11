# L3 交互 HTML 生成规则（report-page 融合版）

版本：2026-10-25 v2.0.0（整体取代旧版；html-anything 引擎已于 2026-10-25 删除，禁止引用其风格文件）。

融合来源：
- **概念层**（体裁判定 / story spine / 块模型 / 源依据纪律）= report-page skill 的语义
- **实现层**（浅色单文件文档页 / mermaid CDN 渲染 / 内联动效 / GitLab MR Changes diff）= 本工程已实测交付风格

核心：**figure-first、单文件自包含、一图顶千字、内容必须来自真实工程且可溯。**

升层判定（L2 → L3）：多图 / 需交互（hover、tooltip、步骤回放、hunk 折叠）/ 多区块（图 + diff 拼版）/ 长文导航。单图能说清 → 留在 L2（聊天内 mermaid），不开本层。

## 交付形态

| 项 | 规定 |
|---|---|
| 文件 | 单个 `output.html`，CSS/JS 全内联 |
| 主题 | 浅色固定；不做深色模式，不做主题切换按钮 |
| 外部依赖 | 唯一默认 mermaid@11 CDN；ECharts 仅量化多系列图可选 |
| 路径 | `<仓库根>/.answer-hub/output/<主题英文短横线>/output.html`（优先级与回退规则见 SKILL.md「输出路径规则」） |
| 骨架 | `h1` → `p.lead`（一句结论）→ `.chips`（关键元数据）→ `section`（图/表/diff 区块）→ `footer`（来源） |
| 聊天回复 | 一句结论 + computer:// 链接，不把全文贴聊天 |

## 体裁判定（写页前先定体）

体裁决定开篇形状与区块顺序，不硬套单一模板：

| 体裁 | 开篇 | 主区块顺序 |
|---|---|---|
| 研究报告 | 结论 lead | 结论 → 图 → 表 → 细节 → 来源 |
| 变更说明 / MR | 统计 tiles | diff 视图为主体，结论 tile 置顶 |
| 机制讲解 | 一句机制 lead | 动效图 + mermaid + 分步文字 |
| 操作指南 | 目标 lead | 步骤表 / 流程图 |
| 数据解读 | 数字 chips | 图表 → 口径说明 → 来源 |

story spine：一条主线讲完，区块为主线服务，不堆砌；元数据不堆徽章墙，进 `.chips` / `footer`。

## 块模型映射（report-page 块 × 本风格实现）

| report-page 块 | 本风格实现 | 用法 |
|---|---|---|
| text | `p` 段落 | 每块 ≤3 行；分析文字放图后 |
| callout | `p.lead`（蓝左边框）/ `.hint` | lead = 开篇一句结论；hint = 口径 / 风险提示 |
| metric | `.chips` 或表格列 | 关键数字 3–5 个 |
| table | HTML table | 默认承载形态（对比 / 清单 / 多字段） |
| diagram | mermaid | 结构 / 关系 / 流转 / 时序 / 拓扑 / 甘特 |
| chart | 纯 CSS/SVG；量化多系列可选 ECharts | 见「信息形态路由」 |
| （本风格特有）动效 | CSS + JS 内联 | 状态机回放 / A-B 对比 / 自动播放 |
| note | `.hint` 小字 | 口径、脚注 |
| sources | `footer` | 数据源 + 口径 + 生成时间，必须可溯 |

## 信息形态路由

| 信息形态 | 交付物 | 实现 | 交互 |
|---|---|---|---|
| 结构 / 关系 / 流转 / 时序 / 拓扑 / 甘特 | mermaid 图 | mermaid@11 CDN | 渲染 + 当前态高亮 / 步骤回放 |
| 机制 / 动态过程 | 动效图 | CSS + JS 内联 | 播放 / 单步 / A-B 对比 |
| 对比 / 清单 / 多字段 | 表格 | HTML table | hover 行高亮 |
| 数据对比（少量系列） | 柱状 / 条形 | 纯 CSS div | hover 高亮 + 数值标签 |
| 趋势 / 变化 | 折线图 | SVG polyline | hover 点 tooltip |
| 占比 / 构成 | 环形图 | SVG stroke-dasharray | hover 扇区 + 图例联动 |
| 量化多系列图表 | ECharts（可选） | CDN | ECharts 原生交互 |
| 代码变更 | GitLab MR Changes 视图 | 见下方模板 | 控制条 + hunk 折叠 |
| 纯代码片段 | 不进 HTML | markdown 围栏 + 语言高亮 | — |
| 文档交付 | 不转 HTML | markdown | — |
| PPT / 幻灯片 | 不用本层 | 见 SKILL.md「HTML 统一政策」 | — |
| 讲解视频 | L4 占位 | 降层 L3（内嵌动画 / 步骤回放） | — |

混合形态（图 + 表 + diff）拼多个 `section` 进同一文件。

## 硬规则

1. **单文件自包含**。CSS/JS 全内联；唯一默认外部依赖 mermaid CDN。
2. **figure-first**。首屏 = 图 + 一句结论；分析文字放图后，短。
3. **必须可交互**。至少 hover / tooltip；流程图必有步骤回放；diff 的 hunk 可折叠。
4. **浅色固定**。不做深色模式、不做主题切换按钮（与 SKILL.md「GitLab MR Changes 浅色」规则一致）。
5. **数据真实可溯**。来自对话上下文 / 工程文件，不编造；footer 标数据源与口径。
6. **真链接**。GitLab MR / issue、JIRA 单号必须是可跳转的真实 URL。
7. **diff 控制条不可省**。`全部展开` / `全部收起` + `⏎ 换行` 必须有；字号 `A−`/`A+` 可选；状态存 localStorage。
8. **交付前必须实测**（见文末）。

## 文档页骨架（CSS 模板）

```css
:root{
  --ink:#1b1f24; --ink2:#4a5361; --ink3:#7a8494;
  --line:#e3e7ee; --line2:#eef1f6; --bg:#f6f7f9; --card:#fff;
  --blue:#1f6feb; --blue-bg:#eaf2ff;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
     font:15px/1.65 system-ui,"Segoe UI","Microsoft YaHei",sans-serif}
.wrap{max-width:1060px;margin:0 auto;padding:34px 24px 72px}
h1{margin:0;font-size:25px}
.lead{margin:14px 0 0;padding:2px 0 2px 14px;border-left:3px solid var(--blue);
      color:var(--ink2);font-size:14.5px}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0 4px}
.chip{font-size:12px;color:var(--ink2);background:var(--card);border:1px solid var(--line);
      border-radius:999px;padding:4px 11px}
section{background:var(--card);border:1px solid var(--line);border-radius:10px;
        margin-top:16px;padding:18px 20px}
section h2{margin:0 0 10px;font-size:17px}
.hint{margin-top:10px;color:var(--ink3);font-size:12.5px}
footer{margin-top:26px;color:var(--ink3);font-size:12px;line-height:1.8}
code,.mono{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}
```

## GitLab MR Changes 视图（代码变更必用）

版式参照 GitLab MR Changes 浅色页：文件头（路径 + `+N`/`−M` 徽章）→ hunk 头 `@@ -a,b +c,d @@` → 双列行号行区。**禁深色终端风配色。**

### 控制条（不可省，sticky 置顶）

| 按钮 | 必须 | 行为 |
|---|---|---|
| `全部展开` / `全部收起` | **必须** | 批量开合所有 `details.file-diff` |
| `⏎ 换行：关/开` | **必须** | `white-space: pre ↔ pre-wrap` 切换（默认关 = 横向滚动看长行） |
| `A−` / `A+` / `⟲ 重置` | 可选 | 代码字号 11–18px，步进 0.5px；基准 12.5px=100% |

字号与换行状态存 `localStorage`（key：`diff-fs`、`diff-wrap`），刷新保持。**不放主题切换按钮。**

### 行规则

- 增行：旧行号列留空，符号 `+`，绿底；删行：新行号列留空，符号 `-`，红底。
- 上下文行：符号空格，无底色。
- 行内单词级变更加 `<span class="hl-add">` / `<span class="hl-del">`。
- 制表符展开 4 空格；`<` `>` `&` HTML 转义。
- 文件头徽章数字必须与行区实际增删行数一致。
- 多文件时：页首统计 tiles（文件数 / +行 / −行 / 关键结论）+ TOC 锚点胶囊；数据量小时 tiles/callout/TOC 可省，**控制条不可省**。

### 横滚与行号（移动端铁律 · 2026-11-08 实测教训）

- **横向滚动只挂容器级**（`.diff-wrap` 文件块 wrapper，`overflow-x:auto`）。**禁止任何行/单元格级 `overflow-x`**——per-cell 滚动 = 一次只能拖一行、整块不联动，手机上不可用（2026-11-08 实测翻车，用户当场打回）。
- 表格按内容撑开：`table.diff{width:max-content;min-width:100%}`；**禁 `table-layout:fixed` + `width:100%`**（长行被压回单元格，是逼出 per-cell 滚动的根因）。
- **行号列 sticky**（GitLab 网页版同款）：`td.ln{position:sticky}`，第一列 `left:0`、第二列 `left:46px`（= 行号列宽）；hunk 头 `position:sticky;left:0`。横滚长行时行号/hunk 头固定在左侧不丢失。
- 触摸惯性：`.diff-wrap` 加 `-webkit-overflow-scrolling:touch`。
- 手机适配 `@media(max-width:640px)`：代码字号降 11.5px、行号列收窄 34px（第二列 `left` 偏移同步改 34px）。
- 换行模式开启时：`table.diff{width:100%;min-width:0}` + `td.ln{position:static}`（无横滚需求，sticky 反占宽）。

### 完整模板

```html
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<title>MR · 标题</title>
<style>
  :root{
    --ink:#1b1f24; --ink2:#4a5361; --ink3:#7a8494;
    --line:#e3e7ee; --line2:#eef1f6; --bg:#f6f7f9; --card:#fff;
    --blue:#1f6feb; --blue-bg:#eaf2ff;
    --add:#e6ffec; --add-b:#1a7f37; --del:#ffebe9; --del-b:#cf222e;
    --hunk:#f2f5f9;
    --add-hl:rgba(26,127,55,.18); --del-hl:rgba(207,34,46,.16);
    --code-fs:12.5px;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
       font:15px/1.65 system-ui,"Segoe UI","Microsoft YaHei",sans-serif}
  .wrap{max-width:1060px;margin:0 auto;padding:34px 24px 72px}
  h1{margin:0;font-size:24px}
  .sub{margin:6px 0 0;color:var(--ink2);font-size:13px}
  code,.mono{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}

  .ctrlbar{position:sticky;top:0;z-index:5;display:flex;gap:8px;flex-wrap:wrap;align-items:center;
           padding:10px 0;background:var(--bg);border-bottom:1px solid var(--line);margin-bottom:16px}
  .ctrlbar button{border:1px solid var(--line);background:var(--card);color:var(--ink2);
                  border-radius:8px;padding:5px 11px;font-size:12.5px;cursor:pointer;
                  font-family:inherit;white-space:nowrap}
  .ctrlbar button:hover{color:var(--ink);border-color:var(--ink3)}
  .ctrlbar .pct{color:var(--ink3);font-size:12px;font-variant-numeric:tabular-nums;
                min-width:42px;text-align:center}

  .tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:8px}
  .tile{padding:14px 16px;border-radius:10px;background:var(--card);border:1px solid var(--line)}
  .tile .label{color:var(--ink2);font-size:12.5px}
  .tile .value{font-size:26px;font-weight:650;margin-top:2px;font-variant-numeric:tabular-nums}
  .tile .foot{color:var(--ink3);font-size:12px;margin-top:2px}

  .hint{margin:12px 0;padding:10px 14px;border-radius:8px;background:var(--line2);
        color:var(--ink2);font-size:13px}

  .toc{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0 4px}
  .toc a{font-size:12.5px;color:var(--ink2);text-decoration:none;border:1px solid var(--line);
         background:var(--card);border-radius:999px;padding:4px 11px}
  .toc a:hover{color:var(--ink)}

  .chg{font-size:12px;font-variant-numeric:tabular-nums;white-space:nowrap;margin-left:auto}
  .plus{color:var(--add-b);font-weight:600} .minus{color:var(--del-b);font-weight:600}

  details.file-diff{background:var(--card);border:1px solid var(--line);border-radius:10px;
                    margin-top:10px;overflow:hidden}
  details.file-diff summary{list-style:none;cursor:pointer;display:flex;align-items:center;
                            gap:10px;padding:11px 15px;font-size:13px;min-height:44px}
  details.file-diff summary::-webkit-details-marker{display:none}
  details.file-diff summary:hover{background:var(--line2)}
  .caret{color:var(--ink3);transition:transform .15s;font-size:10px}
  details[open].file-diff .caret{transform:rotate(90deg)}
  .path{font-size:12.5px;color:var(--ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .diff-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;border-top:1px solid var(--line)}
  table.diff{width:max-content;min-width:100%;border-collapse:collapse;font-family:ui-monospace,Consolas,monospace;
             font-size:var(--code-fs);line-height:1.55;tab-size:4}
  table.diff td{padding:0 10px;vertical-align:top;border:0}
  td.ln{text-align:right;color:var(--ink3);background:var(--line2);
        user-select:none;font-variant-numeric:tabular-nums;font-size:11px;width:46px;position:sticky}
  td.ln:nth-child(1){left:0;border-right:none}
  td.ln:nth-child(2){left:46px;border-right:1px solid var(--line)}
  td.code{white-space:pre;color:var(--ink);padding-top:1px;padding-bottom:1px}
  body.wrap-on td.code{white-space:pre-wrap;word-break:break-all}
  body.wrap-on table.diff{width:100%;min-width:0}
  body.wrap-on td.ln{position:static;border-right:1px solid var(--line)}
  tr.add td.code{background:var(--add);color:var(--add-b)}
  tr.del td.code{background:var(--del);color:var(--del-b)}
  tr.hunk td{background:var(--hunk);color:var(--ink2);font-size:11px;padding:4px 12px;
             border-top:1px solid var(--line);border-bottom:1px solid var(--line);position:sticky;left:0}
  .sign{display:inline-block;width:1.1em;color:var(--ink3)}
  tr.add .sign{color:var(--add-b);font-weight:700}
  tr.del .sign{color:var(--del-b);font-weight:700}
  .hl-add{background:var(--add-hl);border-radius:2px}
  .hl-del{background:var(--del-hl);border-radius:2px}

  @media (max-width:900px){.tiles{grid-template-columns:1fr 1fr}}
  @media (max-width:640px){:root{--code-fs:11.5px}
    td.ln{width:34px}td.ln:nth-child(2){left:34px}}
  @media print{.ctrlbar{display:none!important}details.file-diff{break-inside:avoid}}
</style>
</head>
<body>
<div class="wrap">
  <h1>MR · 标题</h1>
  <p class="sub">基线与口径说明 · 日期</p>

  <div class="ctrlbar">
    <button id="expandAll" type="button">全部展开</button>
    <button id="collapseAll" type="button">全部收起</button>
    <button id="wrapBtn" type="button">⏎ 换行：关</button>
    <button id="fsMinus" type="button">A−</button><span class="pct" id="fsPct">100%</span><button id="fsPlus" type="button">A+</button>
    <button id="fsReset" type="button">⟲ 重置</button>
  </div>

  <div class="tiles">
    <div class="tile"><div class="label">差异文件</div><div class="value">1</div><div class="foot">口径说明</div></div>
    <div class="tile"><div class="label">新增行</div><div class="value" style="color:var(--add-b)">+3</div><div class="foot">—</div></div>
    <div class="tile"><div class="label">删除行</div><div class="value" style="color:var(--del-b)">−1</div><div class="foot">—</div></div>
    <div class="tile"><div class="label">关键结论</div><div class="value" style="font-size:16px">一句话</div><div class="foot">—</div></div>
  </div>

  <p class="hint">风险 / 口径提示写这里（可省）。</p>

  <nav class="toc"><a href="#f1">src/main.c</a></nav>

  <details class="file-diff" id="f1" open>
    <summary><span class="caret">▶</span><code class="path">src/main.c</code>
      <span class="chg"><span class="plus">+3</span> <span class="minus">−1</span></span></summary>
    <div class="diff-wrap"><table class="diff">
      <tr class="hunk"><td colspan="3">@@ -128,7 +128,9 @@ int main(void)</td></tr>
      <tr><td class="ln">128</td><td class="ln">128</td><td class="code"><span class="sign"> </span>    SystemInit();</td></tr>
      <tr class="del"><td class="ln">129</td><td class="ln"></td><td class="code"><span class="sign">-</span>    Mcu_AppsStart(<span class="hl-del">0</span>);</td></tr>
      <tr class="add"><td class="ln"></td><td class="ln">129</td><td class="code"><span class="sign">+</span>    Mcu_AppsStart(<span class="hl-add">1</span>);</td></tr>
    </table></div>
  </details>
</div>
<script>
(function () {
  var root = document.documentElement;
  var BASE = 12.5, MIN = 11, MAX = 18;
  var fs = parseFloat(localStorage.getItem('diff-fs') || BASE);
  if (isNaN(fs)) fs = BASE;
  var pct = document.getElementById('fsPct');
  function applyFs() {
    root.style.setProperty('--code-fs', fs + 'px');
    pct.textContent = Math.round(fs / BASE * 100) + '%';
    localStorage.setItem('diff-fs', String(fs));
  }
  document.getElementById('fsMinus').onclick = function () { fs = Math.max(MIN, fs - 0.5); applyFs(); };
  document.getElementById('fsPlus').onclick = function () { fs = Math.min(MAX, fs + 0.5); applyFs(); };
  document.getElementById('fsReset').onclick = function () { fs = BASE; applyFs(); localStorage.removeItem('diff-fs'); };
  applyFs();

  var wrapBtn = document.getElementById('wrapBtn');
  function applyWrap(on) {
    document.body.classList.toggle('wrap-on', on);
    wrapBtn.textContent = '⏎ 换行：' + (on ? '开' : '关');
    localStorage.setItem('diff-wrap', on ? '1' : '0');
  }
  wrapBtn.onclick = function () { applyWrap(!document.body.classList.contains('wrap-on')); };
  applyWrap(localStorage.getItem('diff-wrap') === '1');

  function setAll(open) {
    document.querySelectorAll('details.file-diff').forEach(function (d) { d.open = open; });
  }
  document.getElementById('expandAll').onclick = function () { setAll(true); };
  document.getElementById('collapseAll').onclick = function () { setAll(false); };
})();
</script>
</body>
</html>
```

多文件 diff = 多个 `details.file-diff` 纵向排列，TOC 锚点一一对应。控制条脚本必须在 `<body>` 尾部的普通 `<script>` 内（早于任何 module 脚本执行交互注册）。

## mermaid 写法（浅色适配）

渲染脚本（module，CDN import，浅色适配，失败降级显源码）：

```html
<pre class="mermaid">
sequenceDiagram
    participant APP as App_PowerHsm
    participant ECU as EcuAL_Mcu
    APP->>ECU: SetPowerMode(STANDBY)
    ECU-->>APP: OK
</pre>
<script type="module">
  try {
    const m = (await import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs')).default;
    m.initialize({ startOnLoad: false, theme: 'base', themeVariables: {
      fontFamily: 'system-ui, "Segoe UI", "Microsoft YaHei", sans-serif',
      fontSize: '13px', primaryColor: '#eaf2ff', primaryBorderColor: '#1f6feb',
      lineColor: #4a5361, textColor: #1b1f24
    }});
    const items = [];
    document.querySelectorAll('pre.mermaid').forEach((el, i) => {
      el.id = 'mmd' + i; items.push({ el, id: el.id, src: el.textContent });
    });
    for (const it of items) {
      try { const { svg } = await m.render(it.id, it.src); it.el.innerHTML = svg; }
      catch (err) { it.el.classList.add('msrc'); }
    }
  } catch (e) {
    document.querySelectorAll('pre.mermaid').forEach(el => el.classList.add('msrc'));
  }
</script>
<style>
  pre.mermaid{background:var(--card);border:1px solid var(--line);border-radius:10px;
              padding:14px;overflow-x:auto;text-align:center}
  pre.mermaid.msrc{text-align:left;font:12.5px/1.6 ui-monospace,Consolas,monospace;color:var(--ink2)}
</style>
```

语法红线（实测踩坑，任一违反渲染失败）：
- 节点/边文本内**禁分号 `;`**（含中文语境的 `；` 用 `，` 或换写）。
- 点线边带标签必须整体写成 `-.->|x|`，禁 `-.-|x|->` 等变体。
- `participant 别名 as 显示名` 的显示名**禁括号**。
- 交付前必须浏览器实测渲染（见文末），不许只靠目测源码。

## 动效脚本规则

交互动效（步骤回放 / A-B 对比 / 自动播放）必须写成**普通 `<script>`，且放在 `<script type="module">` 之前**——module 顶层 `await import(CDN)` 会阻塞网络等待，CDN 慢/断网时排在后面的监听注册不上，按钮全部失灵（实测教训）。

```html
<script>
  /* 动效脚本：普通 script，先于 module */
  (function () {
    var step = 0, steps = document.querySelectorAll('[data-step]');
    var btn = document.getElementById('nextBtn');
    btn.addEventListener('click', function () {
      step = (step + 1) % steps.length;
      steps.forEach(function (el, i) { el.classList.toggle('on', i === step); });
    });
  })();
</script>
<script type="module">
  /* mermaid 渲染（见上一节模板） */
</script>
```

规则：
- 交互用 `addEventListener` / `onclick`，禁 `alert` / `prompt`。
- 状态推进用 class 切换（`.on` / `.off`）+ CSS transition，禁改行内样式动画。
- 与 mermaid 联动高亮当前步：mermaid 渲染出的节点带 id，动效脚本对其 `classList.add` 高亮。

## 交付前实测（headless Edge）

生成后必须实测，不许只目测源码交付：

```powershell
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" `
  --headless=new --disable-gpu --no-sandbox `
  --user-data-dir="$env:TEMP\edge_$(New-Guid)" `
  --virtual-time-budget=18000 `
  --dump-dom "file:///D:/path/to/output.html"
```

实测清单（探针 = 复制文件后在 `</body>` 前注入点击 + 采样的 `<script>`，结果写入 `<pre id="__probe">` 再 dump 提取）：

| 检查项 | 判定 |
|---|---|
| mermaid 渲染 | `.mermaid svg` 存在且 `.error-text` 元素数 = 0 |
| 动效 | 按钮点击后状态 class 推进 / 目标文本变化 |
| diff 控制条 | 全部收起后 `details[open]` 数变化；换行按钮切换 `body.wrap-on`；字号变化反映到 `--code-fs` |
| 控制台 | dump 内无 `Syntax error` / `Uncaught` |

全过 → 交付 computer:// 链接；任一不过 → 修复后重测。
