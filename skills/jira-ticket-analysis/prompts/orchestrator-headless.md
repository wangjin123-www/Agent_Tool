# 无人值守分析编排（headless claude -p 专用）

你是被 `daily.cmd` 无头调用的执行者。任务：对参数指定的工单目录，完成每一单的 AI 分析步骤。
没有人在场，不要提问，按本文档执行到底。

参数（由调用方在 prompt 里给出）：
- `DATE=<YYYY-MM-DD>`
- `WORKSPACE=C:/Users/Lenovo/jta_workspace/out/<DATE>`

## 步骤

1. 枚举 `WORKSPACE` 下的工单子目录。**待办** = 有 `worker_prompt.md` 且没有 `analysis.md` 的目录。
   一个都没有 → 输出 `{"analyzed":0}` 并结束。
2. 对每个待办目录（**顺序处理，一次一单**，防止并发抢资源）：
   a. 完整读取该目录的 `worker_prompt.md`——它就是派给 subagent 的完整提示词。
   b. 用 Task 工具派一个 general-purpose subagent，把 worker_prompt.md 的内容作为任务下发。
      subagent 会读工单/证据/代码快照，写出 `analysis.md`。
   c. subagent 返回后，检查该目录是否有 `analysis.md`：
      - 有 → 继续 d
      - 没有 → 重派一次，重派时明确指示：「你只允许写一个文件：<目录>/analysis.md，
        严格按 worker_prompt.md 里的 12 节报告格式」；再失败就记入 failed，继续下一单
   d. 写 `<目录>/receipt.json`（用 Write 工具直接写）：
      ```json
      {
        "key": "<工单号>",
        "title": "<工单标题>",
        "project": "<工程归属名>",
        "confidence": "<high/medium/low>",
        "size": "<报告行数，如 210>",
        "conclusion": "<analysis.md 第 0 节的一句话结论>",
        "pending": <第 9 节待确认问题条数>,
        "attention": "<需要人工特别注意的一句，无则填 无>",
        "status": "analyzed"
      }
      ```
3. 全部处理完后，输出一行 JSON 总结：`{"analyzed": <n>, "failed": ["KEY1", ...]}`

## 禁止

- 不修改任何代码仓库（快照目录只读）
- 不写 Jira（由 `jtat feedback` 统一在该工单下建子任务：报告挂附件全文 + 打标签；父单不动）
- 不删除任何文件；不碰 WORKSPACE 之外的目录（**唯一例外**：worker 在标签表里所有词都对不上时，
  按 `prompts/ticket_worker.md` 规则 2 往 `template/labels.md` 补一行新词）
