from socket import *

# 1 - repair my socket
my_socket = socket(AF_INET, SOCK_DGRAM)

# 2 - set socket option
my_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# 3 - server address
host = '<broadcast>'
port = 12345
server_address = (host, port)

msg = "Hi server"
my_socket.sendto(msg.encode(), server_address)

server_msg, address = my_socket.recvfrom(1024)
print(server_msg.decode(), address)
