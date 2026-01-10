# Reconnaissance Toolkit 👁️

Custom Python tools for **Reconnaissance** & **MITM** operations.

## 🛠️ Tools

### 1. ARP_Scanner (Network Discovery)
- **Desc:** Maps active devices using ARP Requests (Layer 2).
- **Tech:** Scapy, Broadcast.

### 2. MacChanger (Identity Spoofer)
- **Desc:** Changes network interface MAC address to bypass filters.
- **Tech:** System Calls, Regex.

### 3. Port_Scanner (Service Discovery)
- **Desc:** Checks for open TCP ports on target IP.
- **Tech:** Sockets, TCP Handshake.

### 4. ARP_Spoofer (MITM Attack)
- **Desc:** Intercepts traffic between Target and Gateway via ARP Poisoning.
- **Feat:** **Auto-Restore** (Fixes ARP tables on exit), Bi-directional spoofing.
- **Tech:** Scapy, Packet Crafting.

---

## 🚀 Usage

### Network Scanner
```bash
sudo python3 ARP_Scanner/network_scanner.py
