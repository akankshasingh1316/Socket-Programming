from sys import *
from socket import *
import thread
import time
import os
from threading import *


host = gethostname()
port =  9002
lock = Lock()


s = socket()
s.bind((host,port))
s.listen(5)
ch = 0
port_no = []
ip = []
valu = os.path.getsize("song.mp3")
val = valu * 5
val2 = val



print "SERVER STARTED \n"


def func(c,addr,ch):
	#val = len(port_no)
	global val
	item = addr[1]
	ipt = addr[0]
	seek = 0
	com = 0


	#if val < 65536:
	c.send("ok")   ##for the connection
	#value = value + 1


	if item not in port_no:
		port_no.append(item)
		#print "here"
		print "The Incoming Ports : "
		print port_no


	if ipt not in ip:
		ip.append(ipt)
		print " The Incoming IPs are : "
		print ip

	print "SERVER Connected to :" + str(addr)
	packet = 0
	pk = 1


	while pk == 1 and val <= val2:
		#print " here"

		atck = (c.recv(1024))
		#size = int(atck) 


		if atck[:6] == "attack":
			c.send("ok")
			flood = c.recv(1024)
			attack_size = len(flood)
			val = val - attack_size
			while flood != '':
				flood = c.recv(1024)
				attack_size = len(flood)
				val = val - attack_size
				
			break




		 # recvng size of packet
		
		else:
			size = int(atck)
			file_si = os.path.getsize("song.mp3")
			print "Size Received"
			if file_si > val :
				c.send("no")
				pk = 0
				seek = 1
				print " This Client Can Not Be Handled"
				print "---------xxxxxxxx--------Client Connection Closed -------xxxxxxx-------"
				port_no.pop()
				c.close()

			else:
				c.send("ok")
				req = int(c.recv(1024))  # recvng no of req
				print "Requests Received"
				com1 = (int(file_si)*int(req))
				if com1 > val :
					c.send("no")
					pk = 0
					seek = 1
					print " This Client Can Not Be Handled"
					print "---------xxxxxxxx--------Client Connection Closed -------xxxxxxx-------"
					port_no.pop()
					c.close()

				else:
					com = com + com1
					c.send("ok")
					lock.acquire()
					val = val - com1 
					lock.release()
					res = c.recv(1024)
					k = int(req)
					#if res[:3] == "yes":


					if res[:3] == "yes":
						filesize = os.path.getsize("song.mp3")
						#print "here"
						c.send(str(filesize))
						#print "here2"
						#loop = (filesize * req)/(size)
						#print "no of packets will be" + str(loop)

						while k > 0:
							#print "here3"

							f = open("song.mp3","rb")
							#print "here4"
							datatosend = f.read(size)
							c.send(datatosend)
							
							while datatosend != '':
								#datatosend = f.read(size)
								print "Data Sent of Size : " + str(len(datatosend)) 
								#c.send(datatosend)
								
								packet = packet + 1
								print "Packet No. : " + str(packet) + " is sent. " 
								datatosend = f.read(size)
								c.send(datatosend)



							k = k - 1
							

						print " No. of Proccessed Requests :" + str(req) + "\n"
						#print "aaya?"
						res = 'a'
						#c.send("$")
						print " Executed "
						#c.send("done")
						pk = int(c.recv(1024))
						if pk == 1:
							lock.acquire()
							val = val + com1
							com = com - com1
							lock.release()
							c.send("ok")




						#lock.release()


					elif res[:2] == "no":
						print "Waiting For User Response....."
						pk = int(c.recv(1024))
						lock.acquire()
						val = val + com1
						com = com - com1
						lock.release()
						print "Value Received " + str(pk)
						c.send("ok")
						




					else:
						print " Invalid Input "
						pk = int(c.recv(1024))
						lock.acquire()
						val = val + com1
						com = com - com1
						lock.release()
						c.send("ok")
						




		


	if seek == 0:
		print "---------xxxxxxxx--------Client Connection Closed -------xxxxxxx-------"
		lock.acquire()
		val = val + com
		lock.release()

		port_no.pop()
		c.close()



	elif seek == 1:
		lock.acquire()
		val = val + com
		lock.release()







while True:
	#val = 0
	c,addr = s.accept()
	ch = ch + 1
	thread.start_new_thread(func,(c,addr,ch))


#c.close()
