# copy_fail 研究笔记

本仓库是一个防御性研究工作区，用于研究被跟踪为 `CVE-2026-31431`
的 Linux `copy_fail` 漏洞。

本仓库的目标是保存分析笔记、记录影响范围，并支持安全的本地评估。
它并不用于提供可直接使用的漏洞利用或后渗透流程。

## 仓库结构

- `reports/CVE-2026-31431_Copy_Fail_Report.md` - 英文漏洞报告。
- `code/safe_assessment.py` - 非破坏性的本地暴露面评估辅助工具。


## 安全策略

不要在你不拥有或不管理的系统上运行漏洞利用代码。对于本地测试，优先使用
隔离的虚拟机或一次性实验主机。`code/safe_assessment.py` 中的辅助工具只执行
只读检查，不会尝试触发内存损坏、覆盖文件、生成 shell 或修改系统状态。

> [!CAUTION]
>  在运行 `copy_fail_exp.py` 之前，你需要理解自己正在做什么。运行该脚本所产生的后果由你自行承担。不要在未授权的计算机设备上运行此脚本，否则可能带来不可预期的法律后果。本代码仅用于教育目的、技术研究和安全测试；请勿将其用于非法用途。

copy_fail_exp.py 来源：[theori-io/copy-fail-CVE-2026-31431/copy_fail_exp.py](https://github.com/theori-io/copy-fail-CVE-2026-31431/blob/main/copy_fail_exp.py)

## 快速开始

运行安全评估辅助工具：

```bash
python3 code/safe_assessment.py
```

该辅助工具会报告内核元数据、当前 Python 运行时是否看起来支持 AF_ALG，以及
`/proc/crypto` 中是否可见可能相关的内核加密算法。

## 防御检查清单

1. 盘点受影响的 Linux 主机，并记录内核发行版本字符串。
2. 查看供应商公告，确认已修复的内核软件包。
3. 优先修补允许不受信任的本地用户执行代码的系统。
4. 在补丁完成前限制 shell 访问和容器逃逸面。
5. 监控异常的特权进程启动，以及不受信任用户上下文中对 AF_ALG 套接字的可疑使用。

## 备注

随着公告更新，公开漏洞名称和 CVE 元数据可能发生变化。请将本仓库视为进行中的
研究产物，并在对外发布前刷新报告内容。

有用的公开参考：

- https://copy.fail/
- https://www.microsoft.com/en-us/security/blog/2026/05/01/cve-2026-31431-copy-fail-vulnerability-enables-linux-root-privilege-escalation/
- https://cert.europa.eu/publications/security-advisories/2026-005/
- https://access.redhat.com/security/vulnerabilities/RHSB-2026-002
