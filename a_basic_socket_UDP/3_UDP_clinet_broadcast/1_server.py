from socket import *

# 1 - repair my socket
my_socket = socket(AF_INET, SOCK_DGRAM)

# 2 - server address
host = gethostname()
port = 12345
server_address = (host, port)

# 3 - bind address to socket
my_socket.bind(server_address)

print("waiting....")
while True:
    msg, client_address = my_socket.recvfrom(1024)
    print(msg.decode(), client_address)

    server_msg = "I received your message "
    my_socket.sendto(server_msg.encode(), client_address)
    print("client ip = ", client_address[0], "client port", client_address[1])
