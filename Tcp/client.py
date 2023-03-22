import socket

# 1- server address
host = socket.gethostname()
port = 333
server_address = (host, port)

expected_len = 24


def receive_all(sock: socket.socket) -> str:
    final_msg = ''
    while len(final_msg) < expected_len:
        msg = sock.recv(3).decode()
        if not msg:
            break
        else:
            print(msg)
            final_msg += msg
    return final_msg


def client():
    # 2- socket object
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 3- connect to address
    my_socket.connect(server_address)

    # 4- sendall
    my_socket.sendall('Client : HELLO'.encode())

    # 5- receive
    # msg = my_socket.recv(2084)
    # print(msg.decode())
    msg = receive_all(my_socket)
    print(msg)


client()
