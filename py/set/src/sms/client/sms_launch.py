#!/usr/bin/env python

from SMSProviders import *
import re
import glob
import os

def launch():
	while 1:
		template_choice=raw_input("""
Do you want to use a predefined template or craft
a one time SMS. 

1. Pre-Defined Template
2. One-Time Use SMS
3. Cancel and return to SMS Spoofing Menu

Enter your choice: """)
	
		# if predefined template go here
		if template_choice == '1':
			# set path for
			path = 'src/templates/sms/'
			filewrite=file("src/program_junk/sms.templates", "w")
			counter=0
			# Pull all files in the templates directory
			for infile in glob.glob(os.path.join(path, '*.template')):
				infile=infile.split("/")
				# grab just the filename
				infile=infile[3]
				counter=counter+1
				# put it in a format we can use later in a file
				filewrite.write(infile+" "+str(counter)+"\n")
			# close the file
			filewrite.close()
			# read in formatted filenames
			fileread=file("src/program_junk/sms.templates","r").readlines()
			print "Below is a list of available templates:\n"
			for line in fileread:
				line=line.rstrip()
				line=line.split(" ")
				filename=line[0]
				# read in file
				fileread2=file("src/templates/sms/%s" % (filename),"r").readlines()
				for line2 in fileread2:
					match=re.search("SUBJECT=", line2)
					if match:
						line2=line2.rstrip()
						line2=line2.split("=")
						line2=line2[1]
						# strip double quotes
						line2=line2.replace('"', "")
						# display results back
						print line[1]+": "+line2
	
			# allow user to select template
			choice=raw_input("\nEnter the number you want to use: ")
			for line in fileread:
				# split based off of space
				line=line.split(" ")
				# search for the choice
				match=re.search(str(choice), line[1])
				if match:
					extract=line[0]
					fileopen=file("src/templates/sms/"+str(extract), "r").readlines()
					for line2 in fileopen:
						match2=re.search("ORIGIN=", line2)
						if match2:
							origin=line2.replace('"', "")
							origin=origin.split("=")
							origin=origin[1]
						match3=re.search("SUBJECT=", line2)
						if match3:
							subject=line2.replace('"', "")
							subject=subject.split("=")
							subject=subject[1]
						match4=re.search("BODY=", line2)
						if match4:
							body=line2.replace('"', "")
							body=body.replace(r'\n', " \n ")
							body=body.split("=")
							body=body[1]
	
	  		break;
		if template_choice == '2':
			try:
				origin = raw_input("\nEnter the source number phone: ")
				body = raw_input("\nEnter the body of the message, hit return for a new line.\n\nType your body and enter control+c when finished: ")
				while body != 'sdfsdfihdsfsodhdsofh':
					try:
						body+=("\n")
						body+=raw_input("Next line of the body: ")
					except KeyboardInterrupt: break
			except KeyboardInterrupt: pass
			break;
	
	
		if template_choice == '3': 
			break;
	
	if template_choice != '3':
		while 1:
			service_option=raw_input("""
Service Selection

There are diferent services you can use for the SMS spoofing, select
your own.

What do you want to do:

1. SohoOS (buggy)
2. Lleida.net (pay)
3. SMSGANG (pay)
4. Android Emulator (need to install Android Emulator)
5. Cancel and return to SMS Spoofing Menu

Enter your choice: """)
		
			# exit 
			if service_option == '1':
				break
			if service_option == '2':
				break
			if service_option == '3': 
				break
			if service_option == '4':
				break
			if service_option == '5':
				break
			
	if template_choice != '3' and service_option != '5':
		#sohoOS service
		if service_option == '1':
			for to in phones:		
				send_sohoos_sms(to.rstrip(), origin.rstrip(), body.rstrip())
			# Finish here then return to main menu
			pause=raw_input("\nSET has completed.\nPress enter to return to the SMS Spoofing menu.")
		
		#Lleida.net service
		if service_option == '2':
			user = raw_input("\nEnter your Lleida.net user: ")
			password = raw_input("\nEnter your Lleida.net password: ")
			email = raw_input("\nEnter an email for the receipt (optional): ")
			for to in phones:
				send_lleidanet_sms(to.rstrip(), origin.rstrip(), body.rstrip(), user, password, email)
			# Finish here then return to main menu
			pause=raw_input("\nSET has completed.\nPress enter to return to the SMS Spoofing menu.")

		#SMSGANG service
		if service_option == '3':
			pincode = raw_input("\nEnter your SMSGANG pincode: ")
			for to in phones:
				send_smsgang_sms(to.rstrip(), origin.rstrip(), body.rstrip(), pincode)
			# Finish here then return to main menu
			pause=raw_input("\nSET has completed.\nPress enter to return to the SMS Spoofing menu.")

		#Andriod Emulator service
		if service_option == '4':
			for to in phones:		
				send_android_emu_sms(origin.rstrip(), body.rstrip())
			# Finish here then return to main menu
			pause=raw_input("\nSET has completed.\nPress enter to return to the SMS Spoofing menu.")
