import socket
from struct import *
import datetime
import pcapy
import sys
fl = None
prev_ack = 0
prev_seq = 0
global retransmit
retransmit = 0

def main(argv):
    #list all devices
    devices = pcapy.findalldevs()
    #print devices
     
    #ask user to enter device name to sniff
    #print "Available devices are :"
    #for d in devices :
     #   print d
     
    #dev = raw_input("Enter device name to sniff : ")
    #dev = raw_input("Enter device name to sniff : ")
    dev = "\Device\NPF_{D095B278-15B0-44C3-81A4-07B227B4BF2E}"
	#dev = "\Device\NPF_{A70AD96F-5C5D-4F3A-A7FA-D2F6E44FEDAD}" #for ethernet
	#dev = "\Device\NPF_{D095B278-15B0-44C3-81A4-07B227B4BF2E}" #for wifi
    print "SNIFFING DEVICE " + dev
	
    global fl
    fl = open("new.txt","w+")

    
    
    cap = pcapy.open_live(dev , 65536 , 1 , 0)
 
    #start sniffing packets
    while(1) :
        (header, packet) = cap.next()
        #print ('%s: captured %d bytes, truncated to %d bytes' %(datetime.datetime.now(), header.getlen(), header.getcaplen()))
        parse_packet(packet)
 
#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b
 
#function to parse a packet
def parse_packet(packet) :
     
    #parse ethernet header
    eth_length = 14
    global fl
    global prev_ack
    global prev_seq
     
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
    #print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)
 
    #Parse IP packets, IP Protocol number = 8
    if eth_protocol == 8 :
        #Parse IP header
        #take first 20 characters for the ip header
        ip_header = packet[eth_length:20+eth_length]
         
        #now unpack them :)
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
 
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
 
        iph_length = ihl * 4
 
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);
 
        #print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
        #print "IP Header length : " + str(ihl) + " Protocol :" + str(protocol) + "\n"
        #TCP protocol
        if protocol == 6 :
            t = iph_length + eth_length
            tcp_header = packet[t:t+20]
 
            #now unpack them :)
            tcph = unpack('!HHLLBBHHH' , tcp_header)
             
            source_port = tcph[0]
            dest_port = tcph[1]
            sequence = tcph[2]
            acknowledgement = tcph[3]
            doff_reserved = tcph[4]
            tcph_length = doff_reserved >> 4
            if source_port == 9002:
				if prev_seq == 0 and prev_ack == 0:
					prev_ack = acknowledgement
					prev_seq = sequence
					#global fl
					print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length) + "\n"
					fl.write("Source_port is: " + str(source_port) + "  Destination port is: " + str(dest_port) + "  Sequence Number is: " + str(sequence) + " Acknowledgement number is: " + str(acknowledgement) + "\n")
						

				else:
					#prev_seq = sequence
					#prev_ack = acknowledgement

					if prev_seq == sequence and prev_ack == acknowledgement:
						#global fl
						print "THIS IS RETRANMISSION OF PACKET NO : " + str(sequence) + "\n"
						fl.write("THIS IS RETRANMISSION OF PACKET NO : " + str(sequence) + "\n")
						global retransmit
						retransmit = retransmit + 1

					else:

						#global fl
						fl.write("Source_port is: " + str(source_port) + "  Destination port is: " + str(dest_port) + "  Sequence Number is: " + str(sequence) + " Acknowledgement number is: " + str(acknowledgement) + "\n")
						print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length) + "\n"
						prev_ack = acknowledgement
						prev_seq = sequence
                    
            h_size = eth_length + iph_length + tcph_length * 4
            data_size = len(packet) - h_size
             
            #get data from the packet
            data = packet[h_size:]
             
            #print 'Data : ' + data
 
        #ICMP Packets
	#print "TOTAL RETRANSMISSIONS "+ str(retransmit)
       
 
if __name__ == "__main__":
  main(sys.argv)