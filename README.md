<h1 align="center"> copy_fail Research Notes</h1>

<p align="center">CVE-2026-31431</p>

[English](README.md) [简体中文](README-zh_CN.md) 




This repository is a defensive research workspace for studying the Linux
`copy_fail` vulnerability tracked as `CVE-2026-31431`.

The goal of this repository is to preserve analysis notes, document impact, and
support safe local assessment. It is not intended to provide a turnkey exploit
or post-exploitation workflow.

## Repository Layout

- `reports/CVE-2026-31431_Copy_Fail_Report.md` - English vulnerability report.
- `code/safe_assessment.py` - Non-destructive local exposure assessment helper.


## Safety Policy

Do not run exploit code on systems you do not own or administer. For local
testing, prefer an isolated virtual machine or disposable lab host. The helper in
`code/safe_assessment.py` performs read-only checks and does not attempt to
trigger memory corruption, overwrite files, spawn a shell, or modify system
state.

> [!CAUTION]
>  You need to understand what you are doing before running `copy_fail_exp.py`. You are solely responsible for the consequences of running this script. Do not run this script on unauthorized computer devices, as this will have unforeseen legal consequences. This code is for educational purposes, technical research, and security testing only; please do not use it for illegal purposes.

Source of copy_fail_exp.py:[theori-io/copy-fail-CVE-2026-31431/copy_fail_exp.py](https://github.com/theori-io/copy-fail-CVE-2026-31431/blob/main/copy_fail_exp.py)

## Quick Start

Run the safe assessment helper:

```bash
python3 code/safe_assessment.py
```

The helper reports kernel metadata, whether AF_ALG appears available to the
current Python runtime, and whether potentially relevant kernel crypto
algorithms are visible in `/proc/crypto`.

## Defensive Checklist

1. Inventory affected Linux hosts and record kernel release strings.
2. Check vendor advisories for fixed kernel packages.
3. Prioritize patching systems where untrusted local users can execute code.
4. Restrict shell access and container escape surfaces while patching.
5. Monitor for unexpected privileged process launches and suspicious use of
   AF_ALG sockets from untrusted user contexts.

## Notes

Public vulnerability names and CVE metadata can change as advisories are
updated. Treat this repository as a working research artifact and refresh the
report before external publication.

Useful public references:

- https://copy.fail/
- https://www.microsoft.com/en-us/security/blog/2026/05/01/cve-2026-31431-copy-fail-vulnerability-enables-linux-root-privilege-escalation/
- https://cert.europa.eu/publications/security-advisories/2026-005/
- https://access.redhat.com/security/vulnerabilities/RHSB-2026-002
