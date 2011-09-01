#!/usr/bin/env python
import subprocess

#
# Simple python script to kill things created by the SET wifi attack vector
#

interface = raw_input("Enter your wireless interface (ex: wlan0): ")

# fix a bug if present
print "[*] Attempting to set rfkill to unblock all if RTL is in use. Ignore errors on this."
subprocess.Popen("rmmod rtl8187;rfkill block all;rfkill unblock all;modprobe rtl8187;rfkill unblock all;ifconfig %s up" % (interface), shell=True).wait()

print ("[*] Killing airbase-ng...")
subprocess.Popen("killall airbase-ng", shell=True).wait()

print ("[*] Killing dhcpd3 and dhclient3...")
subprocess.Popen("killall dhcpd3", shell=True).wait()
subprocess.Popen("killall dhclient3", shell=True).wait()

print ("[*] Killing dnsspoof...")
subprocess.Popen("killall dnsspoof", shell=True).wait()

print ("[*] Killing monitor mode on mon0...")
subprocess.Popen("src/wireless/airmon-ng stop mon0", shell=True).wait()

print ("[*] Turning off monitor mode on wlan0...")
subprocess.Popen("src/wireless/airmon-ng stop wlan0", shell=True).wait()

print ("[*] SET has stopped the wireless access point. ")
pause = raw_input("[*] Press [return] to go back to the main menu. ")
