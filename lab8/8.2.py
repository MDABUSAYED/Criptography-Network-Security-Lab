import dpkt

syn = {}
syn_ack = {}

pcap = raw_input("Give Your File Name: ")
f = open(pcap)
pcap = dpkt.pcap.Reader(f)

i = 0
for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = dpkt.tcp.data
    print "Source : %d Destinition : %d" % (tcp.sport,tcp.dport)
    i+=1
    if i==10: break

f.close()
