from ipaddress import ip_network

net = ip_network('131.25.181.52/255.255.248.0', False)

k = 0
for ad in net:
    s = ''
    for x in str(ad).split('.'):
        t = int(x)
        h = hex(t)[2:]
        s += h
    if '5' in s:
        k += 1
print(k)
