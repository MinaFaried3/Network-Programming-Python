from socket import *

expected_len = 25


def receive_all(sock: socket) -> str:
    final_msg = ''
    while len(final_msg) < expected_len:
        msg = sock.recv(4).decode()
        if msg:
            final_msg += msg
            print(msg)
        else:
            break
    return final_msg


def client():
    # 1- server address
    host = gethostname()
    port = 789
    server_address = (host, port)

    # 2- socket object and set option
    my_socket = socket(AF_INET, SOCK_STREAM)

    # 3- start connection
    my_socket.connect(server_address)

    # 4- send all
    my_socket.sendall('HI CLIENT 1'.encode())

    # 5- receive
    msg = receive_all(my_socket)
    print(msg)


client()
