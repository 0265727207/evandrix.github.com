#!/usr/bin/env python
import random
try:
	print ("\n         [****]  Custom Template Generator [****]\n") 
	author=raw_input("\nEnter the name of the author: ")
	filename=randomgen=random.randrange(1,99999999999999999999)
	filename=str(filename)+(".template")
	origin=raw_input("Enter the source phone of the template: ")
	subject=raw_input("Enter the subject of the template: ")
	body=raw_input("Enter the body of the message: ")
	filewrite=file("src/templates/sms/%s" % (filename), "w")
	filewrite.write("# Author: "+author+"\n#\n#\n#\n")
	filewrite.write('ORIGIN='+'"'+origin+'"\n\n')
	filewrite.write('SUBJECT='+'"'+subject+'"\n\n')
	filewrite.write('BODY='+'"'+body+'"\n')
	print "\n"
	filewrite.close()
except Exception, e:
	print "An error occured, printing error message: "+str(e)
