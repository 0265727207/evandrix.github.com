#!/usr/bin/env python
import random
try:
	print ("\n         [****]  Custom Template Generator [****]\n") 
	print ("\n   Always looking for new templates! In the set/src/templates directory send an email\nto davek@social-engineer.org if you got a good template!")
	author=raw_input("\n   Enter the name of the author: ")
	filename=randomgen=random.randrange(1,99999999999999999999)
	filename=str(filename)+(".template")
	subject=raw_input("   Enter the subject of the email: ")
	try:
		body=raw_input("\n   Enter the body of the message, hit return for a new line.\n\nType your body and enter control+c when you are finished: ")
		while body != 'sdfsdfihdsfsodhdsofh':
			try:
				body+=(r"\n")
				body+=raw_input("Next line of the body: ")
			except KeyboardInterrupt: break
	except KeyboardInterrupt: pass
	filewrite=file("src/templates/%s" % (filename), "w")
	filewrite.write("# Author: "+author+"\n#\n#\n#\n")
	filewrite.write('SUBJECT='+'"'+subject+'"\n\n')
	filewrite.write('BODY='+'"'+body+'"\n')
	print "\n"
	filewrite.close()
except Exception, e:
	print "   An error occured, printing error message: "+str(e)
