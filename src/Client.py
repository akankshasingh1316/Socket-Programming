from sys import *
from socket import *
import time
from Tkinter import *
import tkMessageBox
import os
import matplotlib.pyplot as plt

host = gethostname()
r = gethostbyname(host)
port = 9002
pack = 0

s = socket()
s.connect((host,port))









def calc():
	global size
	#size = int(en.get())
	if not en.get():
		tkMessageBox.showinfo("ERROR !!!!","Please Enter The Valid Value")

		#lab = Label(bot,text = "Please enter the value")
		#lab.pack()

	#	size = int(en.get())
	else:
		size = int(en.get())
		top.destroy()


def calc2():
	global req
	#req = int(en1.get())
	if not en1.get():
		tkMessageBox.showinfo("ERROR !!!!","Please Enter The Valid Value")
		#lab = Label(bot1,text = "Please enter the value")
		#lab.pack()

	else:
		req = int(en1.get())

		top2.destroy()



def calc3():
	global res
	#res = str(en2.get())
	if not en2.get():
		tkMessageBox.showinfo("ERROR !!!!","Please Enter The Valid Value")
		#lab = Label(bot2,text = "Please enter the value")
		#lab.pack()
	else:
		res = str(en2.get())
		top3.destroy()

def calc4():
	#lab = Label(up5,text = "press (x) to continue..")
	#lab.pack()	
	top4.destroy()


def calc5():
	global lk
	#lk = int(ent.get())
	if not ent.get():
		tkMessageBox.showinfo("ERROR !!!!","Please Enter The Valid Value")
		#lab = Label(fd,text = "Please enter the value")
		#lab.pack()
	else:
		t = int(ent.get())
		if t != 1 and t != 0:
			tkMessageBox.showinfo("ERROR !!!!","Please Enter 0/1 ")


		else:
			lk = int(ent.get())
			top6.destroy()

def calc6():
	top5.destroy()

def analyse():
	top10.destroy()



re = 1


totalrecv = 0
lk = 0
l = 1
p = 0
while  l == 1:
	pack = 0
	totalrecv = 0
	tym = []
	val = []

	resp = s.recv(1024)    ##### for the connection

	if resp[:2] == "ok":
		print "Connected To The Server : " + str(r) + "\n"
		
		
		
		os.startfile(r'C:\Users\desir\Desktop\Minor2\Sniffer.py')
		os.startfile(r'C:\Users\desir\Desktop\Minor2\TraceRoute.py')
		
		top10 = Tk()
		msg = Label(top10,text = " First Fill in the Details for the Packet Analyser")
		msg.pack()
		labell = Label(top10, text = "Press Continue After Entering Details ")
		labell.pack()
		butt = Button(top10,text = "Continue",command = analyse)
		butt.pack(side = BOTTOM)
		top10.mainloop()
		



		top = Tk()

		up = Frame(top,width = 55,height = 10)
		up.pack()


		la = Label(up,text = " Enter the Packet Size :")
		la.pack(side = LEFT)

		en = Entry(up)
		en.pack()



		bot = Frame(top,width = 55,height = 10)
		bot.pack(side = BOTTOM)

		sub = Button(bot,text = "PROCEED",command = calc)
		sub.pack(side = BOTTOM)

		 
		top.mainloop()

		s.send(str(size)) #### sending the size of packet
		d = s.recv(1024)
		if d[:2] == "ok":
			#req = raw_input("Enter the number of requests: ")





			top2 = Tk()

			up1 = Frame(top2,width = 55,height = 10)
			up1.pack()


			la1 = Label(up1,text = " Enter No. of Requests : ")
			la1.pack(side = LEFT)

			en1 = Entry(up1)
			en1.pack()



			bot1 = Frame(top2,width = 55,height = 10)
			bot1.pack(side = BOTTOM)

			sub1 = Button(bot1,text = "PROCEED",command = calc2)
			sub1.pack(side = BOTTOM)

			 
			top2.mainloop()

			s.send(str(req))  ### for the no of requests
			d = s.recv(1024)
			if d[:2] == "ok":
				#print "do you want to start the test? \n"
				top3 = Tk()

				up2 = Frame(top3,width = 55,height = 10)
				up2.pack()


				la2 = Label(up2,text = 'Enter "yes" to START the Test : ' )
				la2.pack(side = LEFT)

				en2 = Entry(up2)
				en2.pack()



				bot2 = Frame(top3,width = 55,height = 10)
				bot2.pack(side = BOTTOM)

				sub2 = Button(bot2,text = "PROCEED",command = calc3)
				sub2.pack(side = BOTTOM)

				 
				top3.mainloop()
				#res = raw_input("Enter yes or no:")
				s.send(str(res))
				if res == "yes":
					

					
					filesize = long(s.recv(1024))
					#print "total file size is : " + str(filesize) + "\n"
					
					print "NOW TRANSFERING :"

					start = time.clock()
					lk = filesize * int(req)
					#print " total transfer has to be " + str(lk) + "\n"
					#print "start tym :" + str(start) + "\n"
					k = 1


					top4 = Tk()

					up3 = Frame(top4,width = 55,height = 10)
					up3.pack()


					la3 = Label(up3,text = "Total File Size is : " + str(filesize) )
					la3.pack(side = TOP)

					up4 = Frame(top4)
					up4.pack()

					la4 = Label(up4,text = " Total transfer to be done :  " + str(lk))
					la4.pack(side = TOP)


					up5 = Frame(top4)
					
					up5.pack()

					la5 = Label(up5,text = "Start time is :" + str(start) )
					la5.pack(side = TOP)

					but = Button(up5,text = "Continue",command = calc4)
					but.pack(side = BOTTOM)


					#top4.mainloop()


					
					#loop = int((filesize * int(req))/int(size))    ##packet sizes
					#print "loop value is " + str(loop)
					loop = int(req)
					
					while loop > 0 :
						
						packets = filesize/int(size)       ###### no of packets 
						if (filesize % int(size)) != 0 :
							packets = packets + 1 

							print "Total no. of packets should be : " + str(packets) + "\n"

		             

					
						#datarecv = s.recv(size)
						#s.send("ok")
					
						
						

						while  totalrecv < lk:
							datarecv = s.recv(size)
							io = time.clock()
							tym.append(io)
							val.append(len(datarecv))
							#packets = packets - 1
							#if len(datarecv) < size:
								#sz = int(size) - len(datarecv)
								#sm = s.recv(sz)


								#if sm == '':
							pack = pack + 1
							print "Packet No. :" + str(pack) 
							
							print "Packet Size RECEIVED : " + str(len(datarecv)) + "\n"
							

							totalrecv = totalrecv + len(datarecv)


							print "Total No. of Bytes Received :" + str(totalrecv) + "\n"




#									print "here reached "
								

								




									#packets = packets - 1	
									#f = open ("tesing.txt","ab")				
									#f.write(datarecv)
								
			     

						
						loop = int(loop) - 1

					end = time.clock()

					top4.mainloop()

						
					
					top5 = Tk()
					labe = Label(top5,text = " No. Of Bytes Exchanged :" + str(totalrecv),width = 30,height = 10)
					labe.pack()
					bto = Button(top5,text = "Continue",command = calc6)
					bto.pack(side = BOTTOM)
					


					#print "total file received --->>>>" + str(totalrecv) + "\n"
						

					#print "out of while"
					#end = time.clock() 
					#lac = Label(top5,text = "Click (x) to continue..")
					#lac.pack(side = BOTTOM)
					#top5.destroy()
					top5.mainloop()

					delay = end - start





					#print "delay was " + str(delay) + "seconds" + "\n"

					throughput = (lk/(delay))/1000000
					#print "speed was " + str(throughput) + " MBps " + " with packet size " + str(size) + "\n"
					plt.plot(tym,val)
					plt.xlabel('TIME ----->>>>')
					plt.ylabel('THROUGHPUT ----->>>>')
					plt.title('RESPONSEs')
					#plt.axis([0,end,0,totalrecv])
					plt.show()


					top6 = Tk()
					fup = Frame(top6)
					fup.pack(side = TOP)
					lab1 = Label(fup,text = "DELAY was " + str(delay) + " seconds")
					lab1.pack(side = TOP)

					lab2 = Label(fup,text = " THROUGHPUT was " + str(throughput) + "MBps with PACKET SIZE " + str(size) )
					lab2.pack()







							
				elif res == "no":
					#print "Refused checking ................."
					top6 = Tk()
					fup = Frame(top6)
					fup.pack(side = TOP)
					lab1 = Label(fup,text = "TESTING REFUSED....")
					lab1.pack(side = TOP)
					#val = val + com




					#l = int(raw_input("do u wanna recheck? 1. YES 0. NO ---->>>>"))
					
					#s.send(str(l))

				else:
					#val = val + com
					top6 = Tk()
					lol = Label(top6,text = "RE-Enter Value",width = 20,height = 5)
					lol.pack()
					tkMessageBox.showinfo("ERROR !!!"," INVALID INPUT ... !!!!")

					
					
			else:
				top7 = Tk()
				fup1 = Frame(top7)
				fup1.pack(side = TOP)
				lab2 = Label(fup1,text = " SERVER REFUSED THE REQUEST ")
				lab2.pack(side = TOP)
				lab3 = Label(fup1,text = " CONNECTION CLOSED BY THE SERVER ")
				lab3.pack(side = BOTTOM)
				top7.mainloop()
				#print "server refused the request \n"
				#print " connection closed by server\n"
				#s.close()
				l = 0
				print "Connection Closed "
				top8 = Tk()
				lab5 = Label(top8,text = "CONNECTION CLOSED ")
				lab5.pack()
				lab5 = Label(top8,text = "Click (x) to FINISH")
				lab5.pack()
				p = 1
				s.close()
				top8.mainloop()
				break 




					



			#l = int(raw_input("do u wanna recheck? 1. YES 0. NO ---->>>>"))
			fd = Frame(top6)
			fd.pack(side = BOTTOM)

			lab3 = Label(fd,text = "RETEST/RESTART The TEST ? : 0.NO  1.YES ")
			lab3.pack(side = LEFT)

			ent = Entry(fd)
			ent.pack(side = RIGHT)

			bt = Button(fd,command = calc5 , text = "PROCEED")
			bt.pack(side = BOTTOM)

			top6.mainloop()

			l = lk

			s.send(str(l))
		
		else:

			top7 = Tk()
			fup1 = Frame(top7)
			fup1.pack(side = TOP)
			lab2 = Label(fup1,text = " SERVER REFUSED THE REQUEST ")
			lab2.pack(side = TOP)
			lab3 = Label(fup1,text = " CONNECTION CLOSED BY THE SERVER ")
			lab3.pack(side = BOTTOM)
			top7.mainloop()
			#print "server refused the request \n"
			#print " connection closed by server\n"
			#s.close()
			l = 0
			print "Connection Closed "
			top8 = Tk()
			lab5 = Label(top8,text = "CONNECTION CLOSED ")
			lab5.pack()
			lab5 = Label(top8,text = "Click (x) to FINISH")
			lab5.pack()
			p = 1
			s.close()
			top8.mainloop()
			break 










	else:
		top7 = Tk()
		fup1 = Frame(top7)
		fup1.pack(side = TOP)
		lab2 = Label(fup1,text = " SERVER REFUSED THE REQUEST ")
		lab2.pack(side = TOP)
		lab3 = Label(fup1,text = " CONNECTION CLOSED BY THE SERVER ")
		lab3.pack(side = BOTTOM)
		top7.mainloop()
		#print "server refused the request \n"
		#print " connection closed by server\n"
		#s.close()
		l = 0





if p == 0:

	print "Connection Closed "
	top8 = Tk()
	lab5 = Label(top8,text = "CONNECTION CLOSED ")
	lab5.pack()
	lab5 = Label(top8,text = "Click (x) to FINISH")
	lab5.pack()

	s.close()
	top8.mainloop()






