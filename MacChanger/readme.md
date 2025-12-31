# Cyber Security Projects

## Tools

1. **Scanner/scanner.py** (Port Scanner):
   - Simple TCP Port Scanner using Python sockets.
   - Detects open ports on target IP.
   - **Technique:** Socket Connection (Layer 4).

2. **MacChanger/mac_changer.py** (Identity Spoofer):
   - Automated MAC Address Spoofer for Linux.
   - Manipulates Linux Kernel network stack to change interface identity.
   - Uses "Down -> Change -> Up" algorithm to bypass kernel locks.
   - Auto-discovers available network interfaces from `/sys/class/net`.
   - **Technique:** System Calls (subprocess) & Regex Parsing.

## Usage

### 1. Port Scanner
Target IP is required.
```bash
python3 Scanner/scanner.py <target_ip>
