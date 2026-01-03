# Reconnaissance Toolkit 👁️

This repository serves as a collection of custom tools and scripts developed for the **Reconnaissance (Information Gathering)** phase of penetration testing and Red Team operations.

Each tool is built from scratch to understand the underlying protocols and bypass standard limitations.

## 🛠️ Tools

### 1. ARP_Scanner/network_scanner.py (Network Discovery)
- **Description:** A local network scanner that maps active devices on a subnet.
- **Mechanism:** Constructs custom **Ethernet Frames** carrying **ARP Requests**. Broadcasts to `ff:ff:ff:ff:ff:ff` and parses incoming ARP Replies to extract IP and MAC addresses.
- **Key Features:**
  - Uses `scapy` for raw packet manipulation (Layer 2 & 3).
  - Dynamic input handling for flexible subnet targeting.
  - Bypass OS network stack using `srp()` (Send/Receive Packet).
- **Technique:** ARP Protocol Manipulation & Packet Crafting (Layer 2).

### 2. MacChanger/mac_changer.py (Identity Spoofer)
- **Description:** Automated MAC Address Spoofer for Linux to mask device identity.
- **Mechanism:** Manipulates Linux Kernel network stack to change interface hardware address.
- **Key Features:**
  - Uses "Down -> Change -> Up" algorithm to bypass kernel locks.
  - Auto-discovers available network interfaces from `/sys/class/net`.
  - Regex validation to ensure format correctness.
- **Technique:** System Calls (subprocess) & Regex Parsing.

### 3. Scanner/scanner.py (Port Scanner)
- **Description:** Simple TCP Port Scanner using Python sockets.
- **Mechanism:** Initiates TCP Handshakes with target ports to determine service availability.
- **Key Features:**
  - Detects open ports on target IP.
  - Multi-threaded scanning (planned).
- **Technique:** Socket Connection & TCP Handshake (Layer 4).

---

## 🚀 Usage

### ARP Network Scanner
Requires root privileges for raw packet access.
```bash
sudo python3 ARP_Scanner/network_scanner.py
# Enter Target IP/Subnet when prompted (e.g. 192.168.1.1/24)
