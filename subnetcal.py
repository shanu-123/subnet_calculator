#Subnet

def net_addr(ip,sub):
	subnet = 32
	mask = sub
	lst = []
	netd = []
	network = []
	for i in range(0,mask): # appending mask value 1
		lst.append("1")
	sp = "".join(lst)
	for  i in range(0,subnet): # appending value 0
		if len(lst) < subnet:
			lst.append("0")
	sp1 ="".join(lst)
	print(ip,"ip")
	for i in range(0,len(sp1),8):
		netd.append(int(sp1[i:i+8],2))
	print(netd,"subnet")
	for j in range(4):
		network.append(ip[j] & netd[j])
	return network

def broad_addr(ip,sub):
	subnet = 32
	mask = sub
	lst = []
	bro = []
	broad = []
	for i in range(0,mask): # appending mask value 0
		lst.append("0")
	sp = "".join(lst)
	for  i in range(0,subnet): # appending value 1
		if len(lst) < subnet:
			lst.append("1")
	sp1 ="".join(lst)
	print(ip,"ip")
	for i in range(0,len(sp1),8):
                bro.append(int(sp1[i:i+8],2))
	print(bro,"subnet")
	for j in range(4):
		broad.append(ip[j] | bro[j])
	return broad

def available_host(ip,sub):
	subnet = 32
	mask = 32 - sub
	no_of_avail_ip_addr= pow(2, mask)
	host_ip_address = no_of_avail_ip_addr - 2
	return no_of_avail_ip_addr,host_ip_address


