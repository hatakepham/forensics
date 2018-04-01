from scapy.all import *

r = rdpcap("data.pcap")

flagL = []

for i in range(0, len(r)):
	if ICMP in r[i]:
		print 'OK'
		if not "ICMP 10.136.255.127" in r[i][ICMP].summary():
			continue
		print r[i]
		d = str(r[i]).encode('hex')
		if d not in flagL:
			flagL.append(d[68:70])

f = open('flag.gif', 'w')
f.write(''.join(flagL).decode('hex'))
f.close()