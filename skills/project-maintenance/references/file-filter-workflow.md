# filter 模式:文件过滤配置刷新(当前工程)

> 范围 = **当前工程根**(会话工作目录所在工程)。方法论文档为 skill 内置 `references/file-filter-methodology.md`。

## 前置(必做)

1. **先读 `<skill>/references/file-filter-methodology.md` 全文**——它是内置权威依据:§2 五条判断规则、§3 项目类型识别表、§4 执行流程、§5.1 .claudeignore 模板、§5.2 settings.json 模板、§5.3 决策矩阵、§6 完整案例、§7 五个常见误判、§8 验证清单。
2. (可选覆盖)若 `config/config.conf` 仍配了外部 `file_filter_methodology_doc` 路径,则改读该外部文档并以其为准(为兼容旧配置;默认不配,用内置 reference)。
3. 按 §3 识别当前工程类型:标记文件 `*.uvprojx`=Keil MDK、`.cproject`=S32 Design Studio、`package.json`=Node、`CMakeLists.txt`=CMake 等;识别不出 → 停下让用户告知技术栈。
4. **读 `config/config.conf` 的 `[doc_filter]` 段**(不存在则用默认值:`file=doc-filter.txt`、`scan_dirs=doc`、`auto_analyze=true`、`writeback=true`)——文档目录过滤的开关与范围全部由该段决定,不得由 AI 自行判定。

## doc/ 目录过滤(脚本化,config 驱动)

双通道规则源,**doc-filter.txt 分区保存,两者都生效、互不覆盖**:

1. `config/doc-filter.txt` **锚点(`# ==== 自动生成区`)上方 = 手填区**:纯 gitignore 语法,一行一条。支持目录(`doc/xxx/`)、具体文件(`doc/a/b.pdf`)、通配(`*.tmp`)、取反(`!path`);路径相对工程根,不支持绝对路径。用户可随时手动增删,脚本**永不改动**手填区。
2. **锚点下方 = 自动生成区**:`scripts/docfilter.py` 按 `[doc_filter].scan_dirs` 扫描文档目录,对二进制/图片/OS 垃圾文件推导排除规则,`writeback=true` 时重写生成区(手填区原样保留,回写前备份 `.bak`);保底规则 `!**/CLAUDE.md`、`!**/*.md` 由脚本保证。
3. 合并进 `.claudeignore` 时手填+生成全部规则去重后生效,**手填优先级靠位置自然保证**。

执行(在 skill 目录下):

```
python scripts/docfilter.py --repo <工程根> --apply-ignore
```

- 行为:读 config → 读 doc-filter.txt → (auto_analyze)扫描分析+回写 → 把规则合并进 `<工程根>/.claudeignore` 的受控区段(锚点 `# === doc/ 过滤 (project-maintenance 自动维护,勿手改本段) ===` 到 `# === /doc 过滤 ===`,整段替换,不会堆叠重复)。
- 退出码:0=正常 / 2=config 或规则文件解析失败 / 3=合并 .claudeignore 失败。
- `--render-only` 只打印将合并的规则不动文件;`--no-write` 跳过回写 doc-filter.txt;`--json` 供脚本消费。
- **受控区段之外的 .claudeignore 内容一概不动**;`!**/CLAUDE.md`、`!**/*.md` 保底规则由脚本保证存在。
- 手动只想改排除项:直接编辑 `config/doc-filter.txt`,再跑一次 `--apply-ignore` 同步到 .claudeignore,无需动 AI。


## 变更检测(减少无效写入)

```
du -sh */ 2>/dev/null | sort -rh | head -10
```

- 与现有 `.claudeignore` 比对是否新增需忽略的大头目录/产物目录。
- **top10 大目录无变化且无新增产物目录 → 报告「本次无变更,跳过」,禁止强行写入。**
- 无 `.claudeignore` → 首次生成(init 场景),不走跳过。

## 无人值守默认决策规则(本任务无人在场确认)

1. **文件过滤决策表不等人确认**:按 §2/§5.3 自动生成决策并直接写入文件,决策表纳入最终报告。
2. **`.claude/settings.json` 已存在 → 合并模式**:保留现有 deny 条目,仅追加缺失项,**绝不整文件覆盖**;不存在 → 按 §5.2 模板新建。
3. **疑似密钥/凭据文件未被 .gitignore 跟踪 → 自动加入 `permissions.deny(Read)`**,并在报告高亮告警待用户复核。
4. **top 大目录中出现 §3 表外的未知目录 → 按第三方/产物保守忽略**,在报告列出待用户复核。
5. **项目根无 .gitignore → 跳过文件过滤子任务并报告**(有 .gitignore 的工程正常不会触发)。

## Scope / Constraints

- 只修改当前工程根的 `.claudeignore` 与 `.claude/settings.json`;不修改 `.gitignore`;不覆盖 `.claude/settings.local.json`。
- 严格按 §2 五条判断规则(源/产物、内容/状态、我的/第三方、文本/二进制、业务/过程)决策。
- 严格按 §5.3 决策矩阵选择机制(.claudeignore / deny Read / deny Write)。
- 第三方库源码忽略实现(.c/.py/.js),但必须保留接口(.h/类型定义),如 nanopb。
- 所有层级 CLAUDE.md 必须可读,通配符不能误伤(**用 `!**/CLAUDE.md` 兜底**)。
- **构建工程主文件必须可编辑**:`.cproject`、`*.uvprojx`、`test_prj.mex` 等构建/配置输入源**不加入 `Edit/Write` deny**(用户 2026-11-05 裁定);否则无法维护工程配置、无法把 `board/`、`generate/` 回写 mex,重新生成即回退。
- deny Write 只用于链接脚本、启动代码、密钥/凭据/本地状态等真正不该改的项。
- 含密钥/凭据/本地路径的文件必须用 `permissions.deny`,不能只用 `.claudeignore`。
- 业务文档(.md)必须可读,只忽略二进制文档(.pdf/.xlsx/.png)。
- 锁文件不要忽略。

## Done when

1. 输出项目类型识别结果(标记文件)。
2. 输出 top10 大目录及大小。
3. 输出决策表(目录/文件 | 大小 | 应用规则 A-E | 决策)。
4. 输出更新后的 `.claudeignore` 内容。
5. 输出合并后的 `.claude/settings.json` 内容(标注本次新增的 deny 条目)。
6. 报告预估 token 节省比例。
7. 写入两个文件并报告路径。

## Stop if

- 项目根没有 `.gitignore`:先建议用户创建并提交,再继续。
- 项目类型无法识别:让用户告知技术栈。
- 已存在 `.claude/settings.json`:合并模式处理。
- 检测到疑似密钥/凭据文件未被 .gitignore 跟踪:自动 deny(Read) 并告警。
- top 5 大目录中有未知目录:保守忽略并报告待复核。

## 输出与报告(文字总结到对话 + 落盘统一报告)

- 本节 1-6 项内容同时作为 filter 章节写入统一报告文件(路径规则见 SKILL.md「统一报告文件」)。

- 本次是否有变更(有/无,无则说明跳过原因)。
- 改动的文件路径清单。
- 文件过滤:决策表、top10 大目录、token 节省估算、`.claudeignore` 与 `settings.json` 的 diff(新增了哪些行)。
- doc/ 过滤:docfilter.py 本次回写 `doc-filter.txt` 的新增规则行、合并进 `.claudeignore` 受控区段的结果(created/updated/skipped)。
- 所有告警/待用户复核项汇总(疑似密钥文件、未知大目录)。

## 硬约束(全流程不可违反)

- 只允许改/新建当前工程根的:`.claudeignore`、`.claude/settings.json`。
- 禁止碰:任何 `.c/.h/.s` 源码、构建工程文件(`.uvprojx/.uvoptx/.ewp/.cproject` 等)、`.gitignore`、`.claude/settings.local.json`、CLAUDE.md、CODE_MAP.md。
- 不得在无变更时强行写入。
