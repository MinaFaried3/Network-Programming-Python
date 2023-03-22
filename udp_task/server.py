from socket import *


def connect_server(server_add_param):
    my_socket = socket(AF_INET, SOCK_DGRAM)
    my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    my_socket.bind(server_add_param)
    while True:
        print("Waiting for messages from client : .......")
        massage, cl_add = my_socket.recvfrom(2048)
        print(massage.decode('ascii'))
        my_socket.sendto("your message is received successfully".encode('ascii'), cl_add)


host = "0.0.0.0"
port = 99
server_add = (host, port)
connect_server(server_add)
print("========== DONE ==============")
