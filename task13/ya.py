from ipaddress import ip_network

net1 = ip_network('192.168.56.192/255.255.255.192', False)
net2 = ip_network('192.168.56.208/255.255.255.240', False)

s1 = set()
for ad in net1:
    s1.add(ad)
s2 = set()
for ad in net2:
    s2.add(ad)

print(len(s1.symmetric_difference(s2)))
