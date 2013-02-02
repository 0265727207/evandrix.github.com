#!/usr/bin/env python
import smtplib
import os
import getpass
import sys
import thread
import subprocess
import re
import glob
import random
import time
import base64
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

message_flag="plain"

from src.core.core import *

# DEFINE SENDMAIL CONFIG and WEB ATTACK
sendmail=0
sendmail_file=file("config/set_config","r").readlines()
for line in sendmail_file:
	# strip carriage returns
	line=line.rstrip()
	match=re.search("SENDMAIL=",line)
	if match: 
        	# if match and if line is flipped on continue on
        	if line == ("SENDMAIL=ON"):
           		print ("\n\nSendmail is a Linux based SMTP Server, this can be used to spoof email addresses.")
          		print ("Sendmail can take up to three minutes to start FYI.")
          		print ("Sendmail is set to ON. Would you like to start the server now?\n")
          		sendmail_choice=raw_input("Would you like to start Sendmail yes or no: ")
          		# if yes, then do some good stuff
          		if sendmail_choice == "yes" or sendmail_choice == "y":
             			print "Be patient, it takes up to 3-5 minutes to start sometimes."
             			subprocess.Popen("/etc/init.d/sendmail start", shell=True).wait()
             			smtp = ("localhost")
             			port = ("25")
             			# Flip sendmail switch to get rid of some questions             
             			sendmail=1 
             			# just throw user and password to blank, needed for defining below
             			user=''
             			pwd=''

	# Search for SMTP provider we will be using
	match1=re.search("EMAIL_PROVIDER=", line)
	if match1:

		# if we hit on EMAIL PROVIDER
		email_provider=line.replace("EMAIL_PROVIDER=", "").lower()

		# support smtp for gmail
		if email_provider == "gmail":
			smtp = ("smtp.gmail.com")
			port = ("587")

		# support smtp for yahoo
		if email_provider == "yahoo":
			smtp = ("smtp.mail.yahoo.com")
			port = ("25")

		# support smtp for hotmail
		if email_provider == "hotmail":
			smtp = ("smtp.hotmail.com")
			port = ("25")

            
option1=raw_input("""
   Social Engineer Toolkit Mass E-Mailer

   There are two options on the mass e-mailer, the first would
   be to send an email to one individual person. The second option
   will allow you to import a list and send it to as many people as
   you want within that list.

   What do you want to do:

    1. E-Mail Attack Single Email Address
    2. E-Mail Attack Mass Mailer
    3. Return to main menu.

   Enter your choice: """)

# single email
if option1 == '1':
   to = raw_input("Enter who you want to send email to: ")

# mass emailer
if option1 == '2':
   filepath=raw_input("""
   The mass emailer will allow you to send emails to multiple 
   individuals in a list. The format is simple, it will email
   based off of a line. So it should look like the following:

   john.doe@ihazemail.com
   jane.doe@ihazemail.com
   wayne.doe@ihazemail.com

   This will continue through until it reaches the end of the
   file. You will need to specify where the file is, for example
   if its in the SET folder, just specify filename.txt (or whatever
   it is). If its somewhere on the filesystem, enter the full path, 
   for example /home/relik/ihazemails.txt

    Enter the path to the file to import into SET: """)

# exit mass mailer menu
if option1 == '3': 
	print "Returning to main menu..."
	sys.exit(1)
relay=raw_input("""
   What option do you want to use?

    1. Use a %s Account for your email attack.
    2. Use your own server or open relay

   Enter your choice: """ % (email_provider))
counter=0
# Specify mail Option Here
if relay == '1':
   user = raw_input("   Enter your %s email address: " % (email_provider))
   user1 = user
   pwd = getpass.getpass("Enter your password for gmail (it will not be displayed back to you): ")
   #smtp = ("smtp.gmail.com")
   #port = ("587")

# Specify Open-Relay Option Here
if relay == '2':
   user1 = raw_input("   Enter the email address you want to come from (ex: moo@example.com): ")
   if sendmail==0:
      user = raw_input("   Enter username for open-relay (hit return for blank): ")
      pwd =  getpass.getpass("   Enter password for open-relay (hit return for blank): ")
      #if user == '':
       #  counter=1
   if sendmail==0:
      smtp = raw_input("   Enter the smtp email server address (ex. smtp.youremailserveryouown.com): ")
      port = raw_input("   Enter the port number for the SMTP server (hit enter for default 25): ")
      if port == "":
         port = ("25")

# specify if its a high priority or not
highpri=raw_input("\n   Do you want to flag this message/s as high priority? yes or no: ")
if not "y" in highpri:
	prioflag1 = ""
	prioflag2 = ""
else:
        prioflag1 = ' 1 (Highest)'
        prioflag2 = ' High'

subject=raw_input("\nEnter the subject of the email: ")
try:
    html_flag=raw_input("\n   Do you want to send the message as html or plain?\n\n1. HTML\n2. Plain\n\nEnter your choice (enter for plain): ")
    if html_flag == "" or html_flag == "2":
       message_flag="plain"
    if html_flag == "1":
       message_flag="html"

    body=raw_input("\n   Enter the body of the message, hit return for a new line.\n\nType your body and enter control+c when you are finished: ")
    while body != 'exit':
       try:
          body+=("\n")
          body+=raw_input("   Next line of the body: ")
       except KeyboardInterrupt: break
except KeyboardInterrupt: pass

def mail(to, subject, prioflag1, prioflag2, text):

      msg = MIMEMultipart()
      msg['From'] = user1
      msg['To'] = to
      msg['X-Priority'] = prioflag1
      msg['X-MSMail-Priority'] = prioflag2
      msg['Subject'] = subject

      body_type=MIMEText(text, "%s" % (message_flag))
      msg.attach(body_type)

      mailServer = smtplib.SMTP(smtp, port)
      #mailServer.ehlo()

      if sendmail == 0:
	 if email_provider == "gmail":
		 try:
		         mailServer.starttls()
		 except: pass
	         mailServer.ehlo()
	 else: mailServer.ehlo()

         if counter == 0:

            try:

               mailServer.login(user, pwd)
               thread.start_new_thread(mailServer.sendmail,(user, to, msg.as_string()))

            except:

               import base64

               try:

                  mailServer.docmd("AUTH LOGIN", base64.b64encode(user))
                  mailServer.docmd(base64.b64encode(pwd), "")

               except Exception, e: 

                   print "\n   It appears your password was incorrect.\nPrinting response: "+(str(e))
                   pause=raw_input("   Press enter to continue.")

      if sendmail == 1: 
		thread.start_new_thread(mailServer.sendmail,(user, to, msg.as_string()))    

if option1 == '1':
   mail("%s" % (to),
   subject,
   prioflag1,
   prioflag2,
   body)

if option1 == '2':
      email_num=0
      fileopen=file(filepath, "r").readlines()
      for line in fileopen:
          to = line.rstrip()
          mail("%s" % (to),
          subject,
          prioflag1,
          prioflag2,
          body)
          email_num=email_num+1
          print "Sent e-mail number: " + (str(email_num))

question1=raw_input(bcolors.RED + "\n\n   [*] SET has finished sending the emails. \nPress <enter> when your all done...\n\n" + bcolors.ENDC)
