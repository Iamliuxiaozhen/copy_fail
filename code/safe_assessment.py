#!/usr/bin/env python3
"""Non-destructive local assessment helper for copy_fail research."""

from __future__ import annotations

import os
import platform
import socket
from pathlib import Path


RELEVANT_CRYPTO_TERMS = (
    "authencesn",
    "hmac(sha256)",
    "cbc(aes)",
    "aead",
)


def yes_no(value: bool) -> str:
    return "yes" if value else "no"


def read_proc_crypto() -> str:
    path = Path("/proc/crypto")
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def af_alg_supported() -> bool:
    family = getattr(socket, "AF_ALG", 38)
    sock_type = getattr(socket, "SOCK_SEQPACKET", 5)
    try:
        probe = socket.socket(family, sock_type, 0)
    except OSError:
        return False
    finally:
        try:
            probe.close()
        except UnboundLocalError:
            pass
    return True


def main() -> int:
    proc_crypto = read_proc_crypto()
    proc_crypto_lower = proc_crypto.lower()
    crypto_hits = [
        term for term in RELEVANT_CRYPTO_TERMS if term.lower() in proc_crypto_lower
    ]

    print("copy_fail safe local assessment")
    print("=" * 31)
    print(f"system: {platform.system()}")
    print(f"platform: {platform.platform()}")
    print(f"kernel_release: {platform.release()}")
    print(f"machine: {platform.machine()}")
    print(f"effective_uid: {os.geteuid()}")
    print(f"running_as_root: {yes_no(os.geteuid() == 0)}")
    print(f"python_af_alg_socket_supported: {yes_no(af_alg_supported())}")
    print(f"proc_crypto_readable: {yes_no(bool(proc_crypto))}")
    print(f"relevant_crypto_terms_seen: {', '.join(crypto_hits) or 'none'}")
    print()
    print("assessment:")
    print("- These checks do not prove whether the kernel is vulnerable.")
    print("- Confirm exposure with vendor advisories and the running kernel package.")
    print("- Patch and reboot systems where untrusted local code can run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
