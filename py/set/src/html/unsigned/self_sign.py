#!/usr/bin/env python

import subprocess
import os
import sys

#########################
# Simple signer for signing the java applet attack
#########################
# Thanks Thomas Werth <----
#create Key: keytool -genkey -alias signapplet -keystore mykeystore -keypass mykeypass -storepass mystorepass
#sign: jarsigner -keystore mykeystore -storepass mystorepass -keypass mykeypass -signedjar SignedMicrosoft.jar oMicrosoft.jar signapplet

sys.path.append("src/core")
try: reload(core)
except: import core

os.chdir("src/html/unsigned")
print """
Simply enter in the required fields, easy example below:

Name: FakeCompany
Organization: Fake Company
Organization Name: Fake Company
City: Cleveland
State: Ohio
Country: US
Is this correct: yes

"""
print core.bcolors.RED + """*** WARNING ***
IN ORDER FOR THIS TO WORK YOU MUST INSTALL sun-java6-jdk or openjdk-6-jdk, so apt-get install openjdk-6-jdk
*** WARNING ***""" + core.bcolors.ENDC
# grab keystore to use later
subprocess.Popen("keytool -genkey -alias signapplet -keystore mykeystore -keypass mykeypass -storepass mystorepass", shell=True).wait()
# self-sign the applet
subprocess.Popen("jarsigner -keystore mykeystore -storepass mystorepass -keypass mykeypass -signedjar Signed_Update.jar unsigned.jar signapplet", shell=True).wait()
# move it into our html directory
subprocess.Popen("cp Signed_Update.jar ../", shell=True).wait()
# move back to original directory
os.chdir("../../../")
print "\nJava Applet is now signed and will be imported into the website.\n"
