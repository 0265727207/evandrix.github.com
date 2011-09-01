#!/usr/bin/env python
#########################################
#
# The Social-Engineer Toolkit
# Written by: David Kennedy (ReL1K)
# Email: davek@social-engineer.org
#
###############################################
import subprocess
import os
import time
import re
import sys
import socket
from src.core.core import *
from src.core.menu.text import *

###############################################
# Define path and set it to the SET root dir
###############################################

definepath = os.getcwd()
#os.chdir(definepath)
sys.path.append(definepath)

################################################
# ROOT CHECK
################################################

if os.geteuid() != 0:
        print "\nThe Social-Engineer Toolkit (SET) - by David Kennedy (ReL1K)"
        print "\nNot running as root. \n\nExiting the Social-Engineer Toolkit (SET).\n"
        sys.exit(1)

check_pexpect()
check_beautifulsoup()
define_version = get_version()

# remove old stale files and restore java applet to original applet
cleanup_routine()

sys.path.append("../")
try:
   while 1:
     show_banner(define_version,'1')
     
     print bcolors.ENDC + '   Select from the menu:\n'

    ###################################################
    #        USER INPUT: SHOW MAIN MENU               #
    ###################################################   

     for i,option in enumerate(main):
         menunum = i + 1
         print('    %s. %s' % (menunum,option))
     
     choice = (raw_input("\n   Enter your choice: "))

     if choice == '1': #'Spearphishing Attack Vectors
      while 1:
       show_banner(define_version,0)
   
       ###################################################
       #        USER INPUT: SHOW SPEARPHISH MENU         #
       ###################################################   

       print spearphish_text
       for i,option in enumerate(spearphish_menu):
         menunum = i + 1
         print('    %s. %s' % (menunum,option))
       
       choice1 = raw_input("\n   Enter your choice: ")

       if choice1 == '1':
             sys.path.append("src/core/msf_attacks/")
             try: reload("create_payload")
             except: pass
             import create_payload

       if choice1 == '2':
          sys.path.append("src/core/msf_attacks/")
          try: reload(create_payload)
          except: import create_payload   

       if choice1 == '3':
                sys.path.append("src/phishing/smtp/client/")
                try: reload(custom_template)
                except: import custom_template

       if choice1 == '4': break

 #####################
 # Web Attack Menu
 #####################
     if choice == '2':
      while 1:
        show_banner(define_version,0)
        
        ###################################################
        #        USER INPUT: SHOW WEB ATTACK MENU         #
        ###################################################   

        print webattack_text
        for i,option in enumerate(webattack_menu):
            menunum = i + 1
            print('    %s. %s' % (menunum,option))
        attack_vector = raw_input('\n   Enter your choice (press enter for default): ')

        if attack_vector == "":
                attack_vector = "1"

        # import the verified code signing menu
        if attack_vector == '8':
                sys.path.append("src/html/unsigned")
                try: reload(verified_sign)
                except: import verified_sign

        if attack_vector == '9': break

        # check for apache config and multi attack
        if attack_vector == "7":
                fileopen = file("config/set_config","r")
                for line in fileopen:
                        line = line.rstrip()
                        match = re.search("APACHE_SERVER=ON",line)
                        if match:
                                print bcolors.RED+"\nApache mode is set to ON, you cannot use Multi-Attack Mode with Apache.\n\nTurn off APACHE_SERVER=ON in the SET_CONFIG and relaunch SET." + bcolors.ENDC
                                attack_vector = "30"

        try:
                attack_check = int(attack_vector)
        except: 
                print "[*] Invalid selection, going back to menu."
                break
        if attack_check > 8:
                raw_input("\nInvalid option. Press (return) to continue.")
                break

        if attack_vector == "5": choice3='0'
        if attack_vector != "5":
                show_banner(define_version,0)

                ###################################################
                #     USER INPUT: SHOW WEB ATTACK VECTORS MENU    #
                ###################################################   

                print webattack_vectors_text
                for i,option in enumerate(webattack_vectors_menu):
                    menunum = i + 1
                    print('    %s. %s' % (menunum,option))
                choice3 = raw_input("\n   Enter number (1-4): ")
                
                if choice3 == "quit" or choice3 == "exit" or choice3 == '4': break

        try:
                # write our attack vector to file to be called later
                filewrite = file("src/program_junk/attack_vector","w")

                # webjacking and web templates are not allowed
                if attack_vector == "6" and choice3 == "1":
                        print bcolors.RED+ "\nSorry, you can't use the Web Jacking vector with Web Templates."+ bcolors.ENDC
                        raw_input("\nPress "+ bcolors.RED + "{return} " + bcolors.ENDC + "to continue.")
                        break

                # if we select multiattack, web templates are not allowed
                if attack_vector == "7" and choice3 == "1":
                        print bcolors.RED+ "\nSorry, you can't use the Multi-Attack vector with Web Templates." + bcolors.ENDC
                        raw_input("\nPress "+ bcolors.RED + "{return} " + bcolors.ENDC + "to continue.")
                        break

                # if we select web template and tabnabbing, throw this error and bomb out to menu
                if attack_vector == "4" and choice3 == "1":
                        print bcolors.RED+ "\nSorry, you can only use the cloner option with the tabnabbing method." + bcolors.ENDC
                        raw_input("\nPress "+ bcolors.RED + "{return} " + bcolors.ENDC + "to continue.")
                        break

                # if attack vector is default or 1 for java applet
                if attack_vector == '': attack_vector = '1'
                # specify java applet attack
                if attack_vector == '1':
                        attack_vector = "java"
                        filewrite.write(attack_vector)
                        filewrite.close()

                # specify browser exploits
                if attack_vector == '2':
                        attack_vector = "browser"
                        filewrite.write(attack_vector)
                        filewrite.close()

                if attack_vector == '': attack_vector = '3'
                # specify web harvester method
                if attack_vector == '3':
                        attack_vector = "harvester"
                        filewrite.write(attack_vector)
                        filewrite.close()
                        print "\n" + bcolors.BLUE + "Email harvester will allow you to utilize the clone capabilities within SET\nto harvest credentials or parameters from a website as well as place them into a report.\n" + bcolors.ENDC

                # specify tab nabbing attack vector
                if attack_vector == '4':
                        attack_vector = "tabnabbing"
                        filewrite.write(attack_vector)
                        filewrite.close()

                # specify man left int he middle attack vector
                if attack_vector == '5':
                        attack_vector = "mlitm"
                        filewrite.write(attack_vector)
                        filewrite.close()

                # specify webjacking attack vector
                if attack_vector == "6":
                        attack_vector = "webjacking"
                        filewrite.write(attack_vector)
                        filewrite.close()

                # specify Multi-Attack Vector
                attack_vector_multi = ""
                if attack_vector == '7':
                        # trigger the multiattack flag in SET
                        attack_vector = "multiattack"
                        # write the attack vector to file
                        filewrite.write(attack_vector)
                        filewrite.close()

                # pull ip address
                filewrite = file("src/program_junk/ipaddr.file","w")
                if choice3 != "5":
                        fileopen = file("config/set_config", "r").readlines()
                        for line in fileopen:
                                line = line.rstrip()
                                match = re.search("AUTO_DETECT=ON", line)
                                if match:
                                        try:
                                                ipaddr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                                ipaddr.connect(('google.com', 0))
                                                ipaddr.settimeout(2)
                                                ipaddr = ipaddr.getsockname()[0]
                                                filewrite.write(ipaddr)
                                                filewrite.close()
                                        except Exception, error:
                                                log(error)
                                                ipaddr = raw_input("Enter your interface IP Address: ")
                                                filewrite.write(ipaddr)
                                                filewrite.close()

                        # if AUTO_DETECT=OFF prompt for IP Address
                        for line in fileopen:
                                line = line.rstrip()
                                match = re.search("AUTO_DETECT=OFF", line)
                                if match:
                                        if attack_vector != "harvester":
                                                if attack_vector != "tabnabbing":
                                                        if attack_vector != "webjacking":
                                                                # this part is to determine if NAT/port forwarding is used
                                                                # if it is it'll prompt for additional questions
                                                                print "\nNAT/Port Forwarding can be used in the cases where your SET machine is\nnot externally exposed and may be a different IP address than your reverse listener."
                                                                choice90 = raw_input("\nAre you using NAT/Port Forwarding? yes or no: ")
                                                                if choice90 == "" or choice90 == "yes" or choice90 == "y":
                                                                        ipquestion = raw_input("Enter the IP address to your SET web server (this could be your external IP or hostname): ")
                                                                        filewrite2 = file("src/program_junk/interface", "w")
                                                                        filewrite2.write(ipquestion)
                                                                        filewrite2.close()
                                                                        # is your payload/listener on a different IP?
                                                                        natquestion = raw_input("\nIs your payload handler (metasploit) on a different IP from your external NAT/Port FWD address (yes or no): ")
                                                                        if natquestion == 'yes' or natquestion == 'y':
                                                                                ipaddr=raw_input("Enter the IP address for the reverse handler (reverse payload): ")
                                                                        if natquestion == "" or natquestion == "n" or natquestion == "no":
                                                                                ipaddr = ipquestion
                                                                # if you arent using NAT/Port FWD
                                                                if choice90 == "" or choice90 == "no" or choice90 == "n":
                                                                        print "Enter the IP address of your interface IP or if your using an external IP, what\nwill be used for the connection back and to house the web server (your interface address)\n"
                                                                        ipaddr = raw_input("Enter the IP address for the reverse connection: ")
        
                                        if attack_vector == "harvester" or attack_vector == "tabnabbing" or attack_vector == "webjacking":
                                                print "This option is used for what IP the server will POST to."
                                                print "If your using an external IP, use your external IP for this."
                                                ipaddr = raw_input("Enter the IP address for the POST back in Harvester/Tabnabbing: ")
                                        filewrite.write(ipaddr)
                                        filewrite.close()

                        # if java applet attack
                        if attack_vector == "java":
                                # Allow Self-Signed Certificates
                                fileopen = file("config/set_config", "r").readlines()
                                for line in fileopen:
                                        line = line.rstrip()
                                        match = re.search("SELF_SIGNED_APPLET=ON", line)
                                        if match:
                                                sys.path.append("src/html/unsigned/")
                                                import self_sign


                # Select SET quick setup
                if choice3 == '1':

                                # get the template ready
                                sys.path.append("src/html/templates")
                                try: reload(template)
                                except: import template

                                # grab java applet attack
                                if attack_vector == "java":
                                        # create payload here
                                        sys.path.append("src/core/payloadgen")
                                        try: reload(create_payloads)
                                        except: import create_payloads

                                # grab browser exploit selection
                                if attack_vector == "browser":
                                        # grab clientattack
                                        sys.path.append("src/webattack/browser_exploits")
                                        try: reload(gen_payload)
                                        except: import gen_payload

                                # arp cache attack, will exit quickly 
                                # if not in config file
                                sys.path.append("src/core/arp_cache")
                                try: reload(arp_cache)
                                except: import arp_cache
                                # actual website attack here
                                # web_server.py is main core 
                                sys.path.append("src/html/")
                                # clean up stale file
                                subprocess.Popen("rm src/program_junk/cloner.failed 1> /dev/null 2> /dev/null", shell = True).wait()

                                site_cloned = True

                                sys.path.append("src/webattack/web_clone/")
                                try: reload(cloner)
                                except: import cloner

                                if os.path.isfile("src/program_junk/cloner.failed"):
                                        site_cloned = False

                                if site_cloned == True:

                                        # cred harvester for auto site here
                                        if attack_vector == "harvester" or attack_vector == "tabnabbing" or attack_vector == "webjacking":
                                                if attack_vector == "tabnabbing" or attack_vector == "webjacking":
                                                        sys,path.append("src/webattack/tabnabbing")
                                                        try:reload(tabnabbing)
                                                        except: import tabnabbing
                                                # start web cred harvester here
                                                sys.path.append("src/webattack/harvester")
                                                try: reload(harvester)
                                                except: import harvester
        
                                        if attack_vector != "harvester":
                                                if attack_vector != "tabnabbing":
                                                        if attack_vector != "multiattack":
                                                                if attack_vector != "webjacking":
                                                                                if attack_vector != "multiattack":
                                                                                        # spawn web server here
                                                                                        try: reload(spawn)
                                                                                        except: import spawn


                                        # multi attack vector here
                                        if attack_vector =="multiattack":
                                                if choice3 == "1":
                                                        try:
                                                                filewrite = file("src/progam_junk/multiattack.template","w")
                                                                filewrite.write("TEMPLATE=TRUE")
                                                                filewrite.close()
                                                        except: pass
                                                sys.path.append("src/webattack/multi_attack/")
                                                try: reload(multiattack)
                                                except: import multiattack


                # Create a website clone
                if choice3 == '2':
                        # flag that we want a custom website
                        sys.path.append("src/webattack/web_clone/")
                        if os.path.isfile("src/program_junk/site.template"):
                                subprocess.Popen("rm src/program_junk/site.template", shell = True).wait()
                        filewrite = file("src/program_junk/site.template", "w")
                        filewrite.write("TEMPLATE=CUSTOM")
                        print ("\n   SET supports both HTTP and HTTPS")

                        # specify the site to clone
                        print ("   Example: http://www.thisisafakesite.com")
                        URL = raw_input("   Enter the url to clone: ")
                        match = re.search("http://", URL)
                        match1 = re.search("https://", URL)
                        if not match:
                                if not match1:
                                        URL = ("http://"+URL)

                        match2 = re.search("facebook.com", URL)
                        if match2:
                                URL = ("https://login.facebook.com/login.php")

                        filewrite.write("\nURL=%s" % (URL))
                        filewrite.close()

                        # grab browser exploit selection
                        if attack_vector == "browser":
                                   # grab clientattack
                                   sys.path.append("src/webattack/browser_exploits")
                                   try: reload(gen_payload)
                                   except: import gen_payload

                        # set site cloner to true
                        site_cloned = True

                        if attack_vector != "multiattack":
                                # import our website cloner

                                site_cloned = True

                                try: reload(cloner)
                                except: import cloner

                                if os.path.isfile("src/program_junk/cloner.failed"):
                                        site_cloned = False

                        if site_cloned == True:

                                if attack_vector == "java":
                                        # import our payload generator
                                        sys.path.append("src/core/payloadgen/")
                                        try: reload(create_payloads)
                                        except: import create_payloads

                                # arp cache if applicable
                                sys.path.append("src/core/arp_cache")
                                try: reload(arp_cache)
                                except: import arp_cache

                                # tabnabbing and harvester selection here
                                if attack_vector == "harvester" or attack_vector == "tabnabbing" or attack_vector == "webjacking":
                                        if attack_vector == "tabnabbing" or attack_vector == "webjacking":
                                                sys.path.append("src/webattack/tabnabbing")
                                                try: reload(tabnabbing)
                                                except: import tabnabbing
                                        sys.path.append("src/webattack/harvester")
                                        try: reload(harvester)
                                        except: import harvester

                                # multi_attack vector here
                                if attack_vector == "multiattack":
                                        sys.path.append("src/webattack/multi_attack/")
                                        try: reload(multiattack)
                                        except: import multiattack

                                # if we arent using credential harvester or tabnabbing
                                if attack_vector != "harvester":
                                        if attack_vector != "tabnabbing":
                                                if attack_vector != "multiattack":
                                                        if attack_vector != "webjacking":
                                                                sys.path.append("src/html")
                                                                try: reload(spawn)
                                                                except: import spawn

                # Import your own site
                if choice3 == '3':
                        sys.path.append("src/webattack/web_clone/")
                        if os.path.isfile("src/program_junk/site.template"):
                                subprocess.Popen("rm src/program_junk/site.template", shell = True).wait()
                        filewrite = file("src/program_junk/site.template", "w")
                        filewrite.write("TEMPLATE=SELF")
                        # specify the site to clone
                        print ("\n   Example: /home/website/ (make sure you end with /)")
                        print ("   Also note that there MUST be an index.html in the folder you point to.")
                        URL = raw_input("\n   Enter the path to the website to be cloned: ")
                        if not os.path.isfile(URL+"index.html"):
                                print ("\n   [*] Error, index.html not found!!")
                                print ("   [*] Did you just put the path in, not file?")
                                print ("   [*] Exiting the Social-Engineer Toolkit...Hack the Gibson.\n")
                                sys.exit()
                        subprocess.Popen("cp -rf %s src/webattack/web_clone/site/template/" % (URL), shell = True).wait()
                        filewrite.write("\nURL=%s" % (URL))
                        filewrite.close()
                        
                        # if not harvester then load up cloner
                        if attack_vector == "java" or attack_vector == "browser":        
                                 # import our website cloner
                                 try: reload(cloner)
                                 except: import cloner

                        # if java applet attack
                        if attack_vector == "java":
                                # import our payload generator
                                sys.path.append("src/core/payloadgen/")
                                try: reload(create_payloads)
                                except: import create_payloads

                        # grab browser exploit selection
                        if attack_vector == "browser":
                            # grab clientattack
                            sys.path.append("src/webattack/browser_exploits")
                            try: reload(gen_payload)
                            except: import gen_payload

                        # arp cache if applicable
                        sys.path.append("src/core/arp_cache")
                        try: reload(arp_cache)
                        except: import arp_cache

                        # if not harvester spawn server
                        if attack_vector == "java" or attack_vector == "browser":
                                # import web_server and do magic
                                sys.path.append("src/html")
                                try: reload(spawn)
                                except: import spawn

                        # cred harvester for auto site here
                        if attack_vector == "harvester":
                                # get the url
                                print "   Example: http://www.blah.com"
                                URL = raw_input("   Enter the URL of the website you imported: ")
                                match = re.search("http://", URL)
                                match1 = re.search("https://", URL)
                                if not match:
                                        if not match1:
                                                URL = ("http://"+URL)
                                filewrite = file("src/program_junk/site.template","w")
                                filewrite.write("\nURL=%s" % (URL))
                                filewrite.close()

                                # start web cred harvester here
                                sys.path.append("src/webattack/harvester")
                                try: reload(harvester)
                                except: import harvester

                        # tabnabbing for auto site here
                        if attack_vector == "tabnabbing" or attack_vector == "webjacking":
                                # get the url
                                print "   Example: http://www.blah.com"
                                URL = raw_input("   Enter the URL of the website you imported: ")
                                match = re.search("http://", URL)
                                match1 = re.search("https://", URL)
                                if not match:
                                        if not match1:
                                                URL = ("http://"+URL)
                                filewrite = file("src/program_junk/site.template","w")
                                filewrite.write("\nURL=%s" % (URL))
                                filewrite.close()
                                # start tabnabbing here
                                sys.path.append("src/webattack/tabnabbing")
                                try: reload(tabnabbing)
                                except: import tabnabbing

                                # start web cred harvester here
                                sys.path.append("src/webattack/harvester")
                                try: reload(harvester)
                                except: import harvester

                # option for thebiz man left in the middle attack vector
                if choice3 == '0':
                        sys.path.append("src/webattack/mlitm")
                        try: reload(thebiz)
                        except: import thebiz

                # Return to main menu
                if choice3 == '4':
                        print ("   Returning to main menu.\n")        
                        break
        except KeyboardInterrupt:
                print "   Control-C detected, bombing out to previous menu.."
                break

     # Define Auto-Infection USB/CD Method here
     if choice == '3':
        show_banner(define_version,0)
        
        ###################################################
        #     USER INPUT: SHOW INFECTIOUS MEDIA MENU      #
        ###################################################   

        print infectious_text
        for i,option in enumerate(infectious_menu):
                menunum = i + 1
                print('    %s. %s' % (menunum,option))
        choice1 = raw_input('\n   Enter your choice (return for default): ') 
        if choice1 == "": choice1 = "1"
        if int(choice1) > 2: choice1 = "1"

        # if fileformat
        if choice1 == "1":
                ipaddr = raw_input("   Enter the IP address for the reverse connection (payload): ")
                filewrite = file("src/program_junk/ipaddr.file", "w")
                filewrite.write(ipaddr)
                filewrite.close
        filewrite1 = file("src/program_junk/payloadgen", "w")
        filewrite1.write("payloadgen=solo")
        filewrite1.close()

        # if choice is file-format
        if choice1 == "1":
                filewrite = file("src/program_junk/fileformat.file","w")
                filewrite.write("fileformat=on")
                filewrite.close()
                sys.path.append("src/core/msf_attacks/")
                try: reload(create_payload)
                except: import create_payload

        # if choice is standard payload
        if choice1 == "2":
                filewrite = file("src/program_junk/standardpayload.file", "w")
                filewrite.write("standardpayload=on")
                filewrite.close()
                sys.path.append("src/core/payloadgen/")
                try: reload(create_payloads)
                except: import create_payloads

        # import the autorun stuff
        sys.path.append("src/autorun/")
        try: reload(autorun)
        except: import autorun

        if choice1 == "2":
                sys.path.append("src/core/payloadgen/")
                try: reload(solo)
                except: import solo

     # create listener and payload here
     if choice == '4':
        filewrite = file("src/program_junk/payloadgen", "w")
        filewrite.write("payloadgen=solo")
        filewrite.close()
        sys.path.append("src/core/payloadgen/")
        try: reload(create_payloads)
        except: import create_payloads
        print bcolors.BLUE + "\n   [*] Your payload is now in the root directory of SET as msf.exe.\n" + bcolors.ENDC
        subprocess.Popen("cp src/html/msf.exe ./msf.exe 1> /dev/null 2> /dev/null", shell = True).wait()
        
        # if we didn't select the SET interactive shell or RATTE
        if not os.path.isfile("src/program_junk/set.payload"):
                upx("msf.exe")

        # if the set payload is there
        if os.path.isfile("src/program_junk/set.payload"):
                subprocess.Popen("cp src/program_junk/msf.exe ./msf.exe 1> /dev/null 2> /dev/null", shell = True).wait()

        try: reload(solo)
        except: import solo
        raw_input("\nPress " + bcolors.RED + "{return}" + bcolors.ENDC + " to head back to the menu.")

     # Mass Emailer ONLY
     if choice == '5':
        sys.path.append("src/phishing/smtp/client")
        try: reload(smtp_web)
        except: import smtp_web

     # Teensy HID Menu start here
     if choice == '6':
        show_banner(define_version,0)
        
        ###################################################
        #        USER INPUT: SHOW TEENSY MENU             #
        ###################################################   

        print teensy_text
        for i,option in enumerate(teensy_menu):
            menunum = i + 1
            print('    %s. %s' % (menunum,option))
        choice = raw_input("\n   Enter your choice: ")

        # if not return to main menu
        choice2 = ''

        if choice != "7":
                # set our teensy info file in program junk
                filewrite = file("src/program_junk/teensy", "w")
                filewrite.write(choice+"\n")
                if choice != "3":
                        choice2 = raw_input("   Do you want to create a payload and listener yes or no: ")
                        if choice2 == "yes" or choice2 == "y" or choice2 == "":
                                filewrite.write("payload")
                                filewrite.close()
                                # load a payload
                                sys.path.append("src/core/payloadgen")
                                try: reload(create_payloads)
                                except: import create_payloads
                if choice2 == "no" or choice2 == "n":
                        filewrite.close()
                # need these default files for web server load
                filewrite = file("src/program_junk/site.template", "w")
                filewrite.write("TEMPLATE=CUSTOM")
                filewrite.close()
                filewrite = file("src/program_junk/attack_vector", "w")
                filewrite.write("hid")
                filewrite.close()
                sys.path.append("src/teensy")
                try: reload(teensy)
                except: import teensy

        if choice == "7": choice = None

     #
     # wireless attack module starts here
     #
     if choice == '8':

                # set path to nothing
                airbase_path = ""
                dnsspoof_path = ""
                # need to pull the SET config file
                fileopen = file("config/set_config", "r")
                for line in fileopen:
                        line = line.rstrip()
                        match = re.search("AIRBASE_NG_PATH=", line)
                        if match:
                                airbase_path = line.replace("AIRBASE_NG_PATH=", "")

                        match1 = re.search("DNSSPOOF_PATH=", line)
                        if match1: dnsspoof_path = line.replace("DNSSPOOF_PATH=", "")

                if not os.path.isfile(airbase_path):
                        if not os.path.isfile("/usr/local/sbin/airbase-ng"):
                                print "[!] Warning airbase-ng was not detected on your system. Using one in SET."
                                print "[!] If you experience issues, you should install airbase-ng on your system."
                                print "[!] You can configure it through the set_config and point to airbase-ng."
                                airbase_path = ("src/wireless/airbase-ng")
                        if os.path.isfile("/usr/local/sbin/airbase-ng"): 
                                airbase_path = "/usr/local/sbin/airbase-ng"

                if not os.path.isfile(dnsspoof_path):
                        if os.path.isfile("/usr/local/sbin/dnsspoof"): dnsspoof_path = "/usr/local/sbin/dnsspoof"

                # if we can find airbase-ng
                if os.path.isfile(airbase_path):
                        if os.path.isfile(dnsspoof_path):
                                # start the menu here
                                while 1:
                                        show_banner(define_version,0)
                                        
                                        ###################################################
                                        #        USER INPUT: SHOW WIRELESS MENU           #
                                        ###################################################   

                                        print wireless_attack_text
                                        for i,option in enumerate(wireless_attack_menu):
                                                menunum = i + 1
                                                print('    %s. %s' % (menunum,option))
                                        
                                        choice = raw_input("\n   Enter your choice: ")
                                        # if we want to start access point
                                        if choice == "1":                
                                                sys.path.append("src/wireless/")
                                                try: reload(wifiattack)
                                                except: import wifiattack

                                        # if we want to stop the wifi attack
                                        if choice == "2":
                                                sys.path.append("src/wireless/")
                                                try: reload(stop_wifiattack)
                                                except: import stop_wifiattack

                                        # if we want to return to the main menu
                                        if choice == "3":
                                                print ("   [*] Returning to the main menu ...")
                                                break
                
                if not os.path.isfile(dnsspoof_path):
                                if not os.path.isfile("/usr/local/sbin/dnsspoof"):
                                        print "   [!] DNS Spoof was not detected. Check the set_config file."
                                        pause = raw_input("   Press [return] to go back to the main menu.")

     # 
     # END WIFI ATTACK MODULE
     #

     # import third party modules
     if choice == '9':
        sys.path.append("src/core")
        try: reload(module_handler)
        except: import module_handler

     # Define update metasploit framework menu
     if choice == '10':
        update_metasploit()

     # UPDATE SET HERE
     if choice == '11':
        update_set()

     # HELP MENU HERE
     if choice == '12':
        help_menu()
        
 # EXIT SOCIAL-ENGINEER TOOLKIT
     if choice == '13': 
        print "\nThank you for "+ bcolors.RED+"shopping" + bcolors.ENDC+" at the Social-Engineer Toolkit.\n\nHack the Gibson...\n"
        #subprocess.Popen("killall python 1> /dev/null 2> /dev/null", shell = True).wait()
        sys.exit(1)

         # SMS Attack
     if choice == '7':
        choice1 = '0'
        while choice1 != '3':
                show_banner(define_version,0)
                
                ###################################################
                #        USER INPUT: SHOW SMS MENU                #
                ###################################################   

                print sms_attack_text
                for i,option in enumerate(sms_attack_menu):
                    menunum = i + 1
                    print('    %s. %s' % (menunum,option))

                choice1=raw_input("\n   Enter your choice: ")
                        
                if choice1 == '1':
                        sys.path.append("src/sms/client/")
                        try: reload(sms_client)
                        except: import sms_client 
                
                if choice1 == '2':
                        sys.path.append("src/sms/client/")
                        try: reload(custom_sms_template)
                        except: import custom_sms_template
                
                if choice1 == '3': break

# handle keyboard interrupts
except KeyboardInterrupt: 
        print "\n\n   Thank you for " + bcolors.RED+"shopping" + bcolors.ENDC+" at the Social-Engineer Toolkit.\n\nHack the Gibson...\n"

# handle exceptions
except Exception, error:
        log(error)
        print "\n\n   Something went wrong, printing the error: "+ str(error)
