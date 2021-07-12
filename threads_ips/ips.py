import ipaddress

ip = '192.168.0.1'
ip2 = '192.168.0.0/24'

address = ipaddress.ip_address(ip)
print(address + 256)

net = ipaddress.ip_network(ip2, strict=False)

for ip2 in net:
    print(ip2)