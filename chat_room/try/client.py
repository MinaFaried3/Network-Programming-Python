from socket import *

# 1- host,port
host = gethostname()
port = 12345
client_add = (host, port)

# 2- socket
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(client_add)

# 3- enter name
my_name = input("your name")
