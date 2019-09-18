from scapy.all import *
import sys
    
packets=rdpcap('lbl-internal.20041004-1305.port002.dump.anon')


SYN = {}
SYN_ACK = {}

for pkt in packets:
    if IP in pkt and Ether in pkt and TCP in pkt:
        
        
        F = pkt['TCP'].flags
        SRC = pkt['IP'].src
        DST = pkt['IP'].dst
        if F == 0x12:
	    if not(DST in SYN_ACK):
		SYN_ACK[DST] = 0
	    SYN_ACK[DST] += 1
        elif F == 0x02:
	    if not(SRC in SYN):
	        SYN[SRC]=0
	    SYN[SRC] += 1
            

for IP in SYN_ACK:
    print IP, SYN[IP], SYN_ACK[IP]
    if SYN[IP] > SYN_ACK[IP] * 3:
        print IP
