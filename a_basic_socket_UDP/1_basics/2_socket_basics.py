from socket import *

# SOCK_DGRAM for UDP
my_sock = socket(AF_INET, SOCK_DGRAM)

device_name = gethostname()
print("device name : " + device_name)

ip_address = gethostbyname(device_name)
print("ip address : " + ip_address)

ip_address = gethostbyname("www.google.com")
print("ip address for google : " + ip_address)

# port Functions
service_name = getservbyport(80)
print("service_name for port 80 : " + service_name)

service_port = getservbyname('http')
print("service_port for name(http) : ", service_port)
