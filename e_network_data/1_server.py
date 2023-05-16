from socket import *
from struct import *

header_struct = Struct('!I')

my_socket = socket(AF_INET, SOCK_STREAM)

my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

host = gethostname()
port = 5421
server_address = (host, port)

my_socket.bind(server_address)
my_socket.listen(1)

print("waiting....")
connection, address = my_socket.accept()
connection.shutdown(SHUT_WR)


def get_block() -> str:
    # get length
    length = connection.recv(header_struct.size)
    (length,) = header_struct.unpack(length)
    # get message
    data_ = connection.recv(length)
    return data_.decode()


while True:
    data = get_block()
    if not data:
        break
    print(data)
