#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mac Changer Tool
Description: A Python tool to change the MAC address of a network interface.
It manipulates the Linux Kernel network stack using system calls.
Author: [YakupPayan4578]
"""

import subprocess
import os
import re

def get_current_mac(interface):
    """Retrieves the current MAC address from the interface."""
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface])
        mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
        if mac_search_result:
            return mac_search_result.group(0)
        else:
            return None
    except Exception:
        return None

def change_mac_address(interface, new_mac):
    """
    Changes the MAC address using the 'Down -> Change -> Up' algorithm.
    This bypasses the Kernel lock on active interfaces.
    """
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

# --- Main Execution ---
if __name__ == "__main__":
    print("-" * 40)
    print("Available Network Interfaces:")
    iface_list = os.listdir('/sys/class/net')
    
    for idx, iface in enumerate(iface_list):
        print(f"[{idx}] {iface}")
    print("-" * 40)

    try:
        selection = int(input("Select Interface Index: "))
        interface = iface_list[selection]
        
        current_mac = get_current_mac(interface)
        print(f"[i] Current MAC: {str(current_mac)}")
        
        new_mac = input("Enter New MAC (e.g., 00:11:22:33:44:55): ")
        
        change_mac_address(interface, new_mac)
        
        final_mac = get_current_mac(interface)
        if final_mac == new_mac:
            print(f"[+] SUCCESS! New MAC: {final_mac}")
        else:
            print("[-] FAILURE! MAC did not change. Try running as sudo.")
            
    except (IndexError, ValueError):
        print("[-] Invalid Input.")
    except KeyboardInterrupt:
        print("\n[-] Exiting.")
