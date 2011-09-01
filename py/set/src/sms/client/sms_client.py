#!/usr/bin/env python

import sys

while 1:
	attack_option=raw_input("""
SMS Attack Menu

There are diferent attacks you can launch in the context of SMS spoofing, 
select your own.

What do you want to do:

1. SMS Attack Single Phone Number
2. SMS Attack Mass SMS
3. Return to SMS Spoofing Menu

Enter your choice: """)

	# exit 
	if attack_option == '1':
		print("\nSingle SMS Attack")
		to = raw_input("\nEnter who you want to send sms to: ")
		phones = list()
		phones.append(to)
		sys.path.append("src/sms/client/")
	  	try:
	  		# ugly but "compliant" with SET architecture 
	  		reload(sms_launch)
	  		sms_launch.phones = phones
	  		sms_launch.launch()
	  	except: 
	  		import sms_launch
	  		sms_launch.phones = phones
	  		sms_launch.launch() 
		break	
	if attack_option == '2':
		# TO DO: MASS SMS ATTACK
		print("\nMass SMS Attack")
		try:
			address_book_path = raw_input("\nEnter the phones address book absolute path: ")
			address_book = open(address_book_path, "r")
			phones = list()
			phone = address_book.readline()
			while phone:
				phones.append(phone)
				print("\n" + phone)
				phone = address_book.readline()
		except:
			break
		sys.path.append("src/sms/client/")
	  	try:
	  		# ugly but "compliant" with SET architecture 
	  		reload(sms_launch)
	  		sms_launch.phones = phones
	  		sms_launch.launch()
	  	except: 
	  		import sms_launch 
	  		sms_launch.phones = phones
	  		sms_launch.launch()
		break	
	if attack_option == '3': 
		break
