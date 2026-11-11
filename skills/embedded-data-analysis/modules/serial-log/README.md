# 模块：串口日志（serial-log）

embedded-data-analysis（嵌入式数据分析）的串口日志模块。嵌入式串口日志的**采集 / 网页监视 / 分析 / 邮件**一体化工具。面向 DAB_BOX 等 MCU 工程，Windows 环境。

## 环境要求

| 依赖 | 必需 | 说明 |
|---|---|---|
| Windows 10/11 | ✅ | 串口权限、bat 启动器均为 Windows 设计 |
| Python 3.10+ | ✅ | 装好后确认 `python --version` |
| pyserial | ✅ | `python -m pip install pyserial` |
| 浏览器 | ✅ | Chrome / Edge，网页监视界面 |
| lark-cli | 可选 | 仅"邮件"功能需要（`capture_serial.py` 结束分析发邮件、网页"保存日志"勾选发邮件）。需登录，收件人自动取当前账号邮箱 |
| TRAE | 可选 | 仅"AI 分析选中"、"AI 对话分析日志"需要；不用 TRAE 时网页/采集/分析/邮件全部可用 |

## 快速开始

### 方式一：网页实时监视（日常推荐）

双击 **`嵌入式_超级串口工具.bat`**：

- 弹出控制台窗口 = 服务宿主，**窗口开着服务就在，关窗口即停**
- 服务启动后自动打开浏览器 `http://localhost:8765`
- 串口选择 / 波特率（含自动检测）/ 连接断开 **全部在网页操作**
- 重复双击不会起第二个服务，只会再开一个浏览器页
- **8765 已被占用（含旧服务挂死）时**：启动器会打印 `Web UI: http://localhost:8765/` 并直接打开现有页面，不再杀进程/报错；页面打不开就先关旧服务窗口或执行 `嵌入式_超级串口工具.bat stop`
- 命令行停止：`嵌入式_超级串口工具.bat stop`

### 方式二：后台无界面采集（压测/长稳）

```bash
cd scripts
python capture_serial.py --list                          # 看可用串口
python capture_serial.py --port COM6 --auto-baud --echo \
    --confirm --end-cond unlimited --analysis-mode auto  # 开采
```

- 采集中有看门狗：异常中断自动备份并发邮件
- 外部控制（另开终端）：
  ```bash
  python capture_cmd.py <log路径> status   # 查状态
  python capture_cmd.py <log路径> mail     # 发快照邮件, 采集不中断
  python capture_cmd.py <log路径> stop     # 正常停止(备份+统计+分析)
  ```

## 文件一览

```
serial-log/
├── 嵌入式_超级串口工具.bat               # 网页串口工具启动器(双击=起服务并自动开页面)
├── README.md                  # 本文件
├── SKILL.md                   # AI 侧技能说明(TRAE 读的)
├── assets/                    # icon.ico(任务栏图标)、background.png(网页背景)
├── config/config.conf         # 配置: 串口/波特率/邮件/工程注册表
├── output/logs/               # 输出目录: 根只留"正在采集"主 log, 其余分类子目录
│   ├── 完成采集/              # 采集结束(正常/异常)归档的主 log  serial_<开始>_结束<结束>.log
│   ├── 告警/                  # 告警邮件快照副本      serial_<开始>_告警<HHMMSS>.log
│   ├── 快照/                  # 采集中手动邮件快照副本 serial_<开始>_快照<HHMMSS>.log
│   ├── 分析/                  # md/json/html 分析产物
│   └── ctl/                   # status.json/cmd.json/看门狗日志(<log名>.ctl/)
└── scripts/
    ├── serial_monitor.py      # 网页监视服务(localhost:8765)
    ├── capture_serial.py      # 后台采集(勿随意改, 门禁参数多)
    ├── capture_cmd.py         # 采集中外部控制(status/mail/stop)
    ├── capture_watchdog.py    # 采集看门狗(自动拉起, 一般不用手动跑)
    ├── analyze_log.py         # 日志分析(fixed/free/auto 三模式)
    ├── parse_fixed.py         # 固定格式解析器
    ├── gen_report.py          # HTML 报告生成
    ├── send_mail.py           # 飞书邮件发送(lark-cli)
    └── find_com_holder.py     # 查串口被哪个进程占用(可 --kill)
```

## 日志格式约定

**网页保存 / 后台采集落盘**（两者一致）：

```
[2026-09-20 00:35:57.941] [1000][WARN][usb.c:88] [USB] retry
[2026-09-20 00:35:57.941] IcPwrSta=0,IviPwrSta=0,StrPin=0!
```

- **行首 `[YYYY-MM-DD HH:MM:SS.mmm]`** = 主机系统时间（落盘时加）
- 其后为设备原始行。DAB_BOX 固定格式：`[设备时间戳][LEVEL][文件:行号] [模块] 正文`，LEVEL 可省略
- 分析链（analyze_log/parse_fixed）会**自动剥掉行首主机时间**再匹配，不影响固定格式判定

## 网页功能速查

| 功能 | 操作 |
|---|---|
| 连接/断开、自动检测波特率 | 页面顶部工具栏 |
| 保存日志 | "保存日志"按钮（带主机时间、可选发邮件、可选分析） |
| 历史日志回看 | "打开日志"→ 文件列表 → 选中载入；过滤/显示模式/关键词全部可用 |
| 关键词过滤 | 输入后回车 → 高亮 / 只显示；支持全词匹配、区分大小写、命中计数 |
| 显示模式 | ASCII / HEX / ASCII+HEX 切换；行号开关 |
| 5A A5 协议帧 | 从字节流中按 LEN 重组 5A A5 帧(跨行/帧内 0x0A 也能正确重装),独立成行并强制 HEX 显示(黄色);文本日志仍按文本保留 |
| 隐藏 5A A5 帧 | 工具栏"隐藏5A A5:关/开"按钮,只隐藏协议帧、保留日志;偏好存 localStorage,刷新后保持 |
| 选中分析 | 单击选中 / Ctrl 追加 / Shift 范围；"取消选中"一键清空；实时显示已选行数 |
| AI 分析选中 | 选中若干行 → 按钮 → 在 TRAE 对话里让 AI 分析 `output/logs/ctl/selection_pending.json` |
| 健康状态 | "查看详情"旁常驻徽章（✓正常 / ⚠N项异常） |

## 配置说明（config/config.conf）

```ini
[serial]
port = COM6            # 参考, 不作为启动依据
baud = 115200          # 参考, 不作为启动依据
bauds = 9600,...       # 网页波特率下拉候选

[mail]
enabled = true         # false=全局关邮件
cc =                   # 抄送邮箱, 逗号分隔

[projects]
1 = d:\...\dabbox_app  # 工程根目录, 分析结论关联源码用
2 = d:\...\cdc_7255
default = 2            # 默认工程编号
```

## 常见问题

| 现象 | 原因与处理 |
|---|---|
| `PermissionError(13) 拒绝访问` | 串口被占。`python scripts/common/find_com_holder.py COM6` 查占用，加 `--kill` 结束 |
| 采集 5 秒乱码 | 波特率不对。**永远加 `--auto-baud`**，禁止凭记忆假设波特率 |
| 网页改了代码不生效 | Python 不热重载。关窗口重启服务（服务 = 那个控制台窗口） |
| 日志里时间是独立一行 | 旧版本文件（行尾时间+裸\r）。新版本已根治（行首时间） |
| 邮件发不出 | 未装/未登录 lark-cli；或 config `[mail] enabled=false` |
| 换机器后 lnk 失效 | lnk 存绝对路径。双击 bat 代替，或重建 lnk |
