#!/usr/bin/env python

import glob
import re
import sys

# this is just if the user wants to return to menu
menu_return="false"

# base counter to identify numbers
counter=0

# get the menu going
print "\nWelcome to the Social-Engineer Toolkit Third Party Modules menu.\n"
print "Please read the readme/modules.txt for more information on how to create your\nown modules.\n"
for name in glob.glob("modules/*.py"):
    
    counter=counter+1
    fileopen=file(name, "r")
    
    for line in fileopen:
        line=line.rstrip()
        match=re.search("MAIN=", line)
        if match:
            line=line.replace('MAIN="', "")
            line=line.replace('"', "")
            line=str(counter)+ ". "+line
            # need a second loop for author
            #for line2 in fileopen:
            #    match2=re.search("AUTHOR=", line2)
            #    if match2:
            #        line2=line2.rstrip()
            #        line2=line2.replace('AUTHOR="', "")
            #        line2=line2.replace('"',"")
            #        line=line + " [*] Author: " + line2 + " [*]"
            print line

quit_menu=counter+1
print "%s. Return to the previous menu." % (str(quit_menu)) 
choice=raw_input("\nEnter the module you want to use: ")
if choice == str(quit_menu): menu_return="true"

# throw error if not integer
try: 
    choice=int(choice)
except: 
    choice=raw_input("An integer was not used try again: ")

# start a new counter to match choice
counter=0

if menu_return == "false":
    # pull any files in the modules directory that starts with .py
    for name in glob.glob("modules/*.py"):

        counter=counter+1
        
        if counter == int(choice):
            # get rid of .modules extension
            name = name.replace("modules/", "")
            # get rid of .py extension
            name = name.replace(".py", "")
            # changes our system path to modules so we can import the files
            sys.path.append("modules/")
            # this will import the third party module

            try: 
                exec("import " + name)
            except: 
                pass

            # this will call the main() function inside the python file
            # if it doesn't exist it will still continue just throw a warning
            try:
                exec("%s.main()" % (name))
            # handle the exception if main isn't there
            except Exception,e: 
                raw_input("[!] There was an issue with a module: %s.\nPress [enter] to continue." % (e))
