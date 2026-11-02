# llm-wiki skill

让 AI agent（Claude Code、Codex 等）通过内置 HTTP API 查询用户本地运行的 **LLM Wiki** 桌面应用。

本 skill **只有文档**。该 API 是标准 HTTP+JSON 契约——用 `curl`、`fetch`、`requests` 或你环境里已有的任意 HTTP 工具调用即可。没有客户端库、没有 SDK、无需编译。

## 安装

### 推荐 —— 用 `skills` CLI 一行搞定

```bash
npx skills add https://github.com/nashsu/llm_wiki_skill.git --skill llm-wiki
```

该命令会从 GitHub 拉取最新版 skill 并注册到你的 agent 运行时。之后重新执行同一命令即可更新到新版本。

### 备选 —— clone + 软链接（Claude Code）

如果你希望本地管理源码并链接进 Claude Code（skill 目录位于 `~/.claude/skills/`）：

```bash
git clone https://github.com/nashsu/llm_wiki_skill.git
ln -s "$(pwd)/llm_wiki_skill" ~/.claude/skills/llm-wiki
```

### 备选 —— 手动放置

本 skill 只有三个 markdown 文件。把整个文件夹放到你的 agent 运行时能发现 skill 的位置即可（例如 Codex 的 `agents/`、自定义 MCP server 的 skill 目录）。无依赖、无构建步骤。

## 本 skill 能做什么

- "我的知识库里关于 X 说了什么？" → 混合检索（关键词 + 向量）+ 读取
- "给我看知识图谱里节点 Y 的邻域" → wikilinks 遍历
- "把关于 Z 的页面读给我" → 获取文件内容
- "我刚加了新文档，重新索引" → 后端 rescan
- "给我知识库的结构概览" → 文件树 + index.md
- "把这个对话/这条消息放到飞书知识库" / "save this to my wiki" → 渲染 `templates/飞书消息专为文档.md`，写入 `raw/sources/Collection/飞书/`，然后调用 `sources/rescan`

API 本身除 `sources/rescan` 外均为只读。落库新内容属于**文件系统写入**（API 没有写接口），写入后再触发 rescan。详见 `SKILL.md` → "Writing into the wiki"。

## 文件说明

| 文件 | 用途 |
|---|---|
| `SKILL.md` | 面向 agent 的指令，由 AI 运行时自动加载。 |
| `templates/飞书消息专为文档.md` | 飞书消息导入的页面模板。 |
| `api-reference.md` | 完整的接口契约（状态码、参数、响应结构）。 |
| `examples.md` | 对话场景 → API 调用配方。 |
| `README.md` | 本文件——面向人的安装 / 配置 / 排障说明。 |

没有脚本、没有包装层。如果你觉得需要写一个，直接用 `curl` 就行。

## 前置条件

1. **已安装并运行 LLM Wiki 桌面应用。** API 仅在该应用打开期间监听 `127.0.0.1:19828`。应用未运行时，agent 会收到 `connection refused` 并告知你。

2. **已启用 API server。** 默认开启。在 `Settings → API Server → "Enable local HTTP API"` 中确认已勾选。

3. **已配置 token。** 默认关闭（token 字段为空 → 所有接口返回 401）。两种方式：
   - 在应用内：`Settings → API Server → Generate new token`，复制并妥善保管。
   - 通过环境变量：`export LLM_WIKI_API_TOKEN=...`（覆盖 UI 设置；对该 agent 进程持续生效）。

   你也可以打开 `Settings → API Server → "Allow access without a token"`，彻底移除鉴权。**仅限本机——但这样本机上任何进程都能读你的知识库。** 只在可信环境下使用。

## 快速冒烟测试

> **Windows 用户**：把 `export LLM_WIKI_API_TOKEN=...` 换成 `$env:LLM_WIKI_API_TOKEN = "..."`（PowerShell）或 `set LLM_WIKI_API_TOKEN=...`（cmd.exe）。在 PowerShell 中用 `curl.exe` 代替 `curl`，以绕过 `Invoke-WebRequest` 别名。反斜杠续行符（`\`）在 PowerShell 中改为反引号（`` ` ``），在 cmd 中改为 `^`。

```bash
export LLM_WIKI_API_TOKEN=...

# 1. 探活 —— 无需鉴权
curl -s http://127.0.0.1:19828/api/v1/health

# 预期返回：
# {
#   "ok": true,
#   "status": "running",
#   "enabled": true,
#   "authConfigured": true,
#   "tokenSource": "env",
#   "allowUnauthenticated": false,
#   ...
# }

# 2. 列出项目
curl -s -H "Authorization: Bearer $LLM_WIKI_API_TOKEN" \
  http://127.0.0.1:19828/api/v1/projects

# 3. 检索当前激活项目
curl -s -H "Authorization: Bearer $LLM_WIKI_API_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"query":"rope","topK":3}' \
  http://127.0.0.1:19828/api/v1/projects/current/search

# 4. 读取某个页面
curl -s -H "Authorization: Bearer $LLM_WIKI_API_TOKEN" \
  "http://127.0.0.1:19828/api/v1/projects/current/files/content?path=wiki/concepts/rope.md"
```

如果装了 `jq` 且想要格式化输出，可在任意命令末尾加 `| jq`。非必需。

## 排障

| 现象 | 原因 | 解决 |
|---|---|---|
| `curl: (7) Failed to connect to 127.0.0.1 port 19828` | 应用未运行 | 启动 LLM Wiki 桌面应用，等约 2 秒让 API server 完成监听。 |
| `/health` 返回 `Status: port_conflict` | 19828 端口被其他进程占用 | 用 `lsof -i :19828` 找到占用进程；退出并重启应用。 |
| 所有接口返回 401 | 未配置 token | Settings → API Server → Generate；或 `export LLM_WIKI_API_TOKEN=...` |
| 所有接口返回 503 且带 "disabled" | 总开关被关闭 | Settings → API Server → 勾选 "Enable local HTTP API"。 |
| 所有接口返回 503 且带 "busy" | 达到并发上限（64 并发） | 降低并发，减少并行请求。 |
| 高频请求返回 429 | 限流：全局 120 req/秒 | 退避 ≥1 秒。 |
| `files/content` 对 `.pdf` 返回 415 | API 仅支持文本 | 通过桌面 UI 阅读源 PDF；仅文本类扩展名对外暴露。 |
| UI 里已清空 token，但 `tokenSource` 仍为 `"env"` | 某处设置了 `LLM_WIKI_API_TOKEN` 环境变量 | `unset LLM_WIKI_API_TOKEN`；或将其值设为与 UI 中一致。 |

## 安全模型

- API 仅监听 `127.0.0.1`，**无法从网络中的其他主机访问**。
- Token 鉴权采用常量时间比较（鉴权检查无时序泄漏）。
- 路径遍历在路由处理器处拦截（`safe_join` + 规范化路径前缀校验）。
- 文件读取受白名单限制（`purpose.md`、`schema.md`、`wiki/**`、`raw/sources/**`）；仅文本扩展名；上限 2 MB。
- Body 上限 1 MB；并发上限 64；限流 120/秒。
- v1 无写接口。`/sources/rescan` 是唯一的变更操作，且它只读磁盘 + 排队内部任务。

**不在**威胁模型内的：

- 持有 token 的**本地**恶意进程可以读取你当前激活项目的 wiki + sources 全部内容。请将 token 视为本地机密。
- 本地恶意进程可以探测 `/health`（无需鉴权）以发现 API 的存在。属于信息暴露，不泄露内容。
- 跨源浏览器页面只有在持有 token 时才能访问该 API。默认 CORS 为 `*`——依赖 token 保密。不要把 token 粘贴到不可信的 web 工具中。

## 版本

本 skill 对应应用版本 `0.4.10+` 所带的 **LLM Wiki API v1**。混合检索（关键词 + 向量）已上线；响应携带 `mode: "keyword" | "vector" | "hybrid"`、`tokenHits`、`vectorHits` 以及每个结果的 `vectorScore`。如果桌面应用的 `/health` 报告了主版本号跃升，请先查阅 `api-reference.md` 确认契约是否有变动，再原样依赖该契约。

## 更新

如果你是通过 `npx skills add` 安装的，重新执行同一命令即可拉取最新版本：

```bash
npx skills add https://github.com/nashsu/llm_wiki_skill.git --skill llm_wiki_skill
```

如果你 clone 了仓库，在 clone 目录内执行 `git pull` 即可——软链接会自动同步变更。

## 贡献

源码仓库：<https://github.com/nashsu/llm_wiki_skill>

欢迎提 Issue 和 PR。本 skill 应始终保持 **client-less**——不加脚本、不加 SDK 封装、不加包装二进制。底层 API 的全部意义就在于任意 HTTP 工具都能调用；本 skill 是契约文档，不是运行时。

## 许可

许可详情见仓库。
