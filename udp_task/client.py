from socket import *

my_socket = socket(AF_INET, SOCK_DGRAM)
my_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
host = "255.255.255.255"
port = 99
# while True:
server_add = (host, port)
my_socket.sendto("mina is connecting server".encode('ascii'), server_add)
message, server_result = my_socket.recvfrom(1024)
print(message.decode('ascii'), server_result)
