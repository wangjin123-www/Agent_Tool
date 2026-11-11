# proto-toolkit

通信协议理解工具（飞书多维表格数据源，平台宏路由，当前仅 7255）。

详见 [SKILL.md](./SKILL.md)。

```powershell
cd .claude/skills/proto-toolkit
python scripts/cli.py platform      # 活动平台
python scripts/cli.py read          # 协议概览
python scripts/cli.py query 心跳    # 关键词搜索
python scripts/cli.py show interface PowerOnHandshakeMtd
```

旧版（电子表格全生命周期 sync/edit/parse/gen/console）备份在
`.claude/skills-backup/proto-toolkit_20261108/`。
