from socket import *


def receive_from_server(_socket: socket) -> str:
    data = ""
    expected_len = len("Server : sends message ")
    while len(data) < expected_len:
        _msg = _socket.recv(4).decode()
        print(_msg)
        if not _msg:
            print("done")
            break
        data += _msg

    return data


# 1 - repair my socket
my_socket = socket(AF_INET, SOCK_STREAM)

# 2 - server address
host = gethostname()
port = 672
server_address = (host, port)

# 3 - connect with address
my_socket.connect(server_address)

my_socket.sendall("Client Hello".encode())

# msg = my_socket.recv(1024)
# print(msg.decode())

msg = receive_from_server(my_socket)
print(msg)
