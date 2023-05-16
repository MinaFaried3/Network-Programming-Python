from socket import *
from struct import *

header_struct = Struct('!I')

my_socket = socket(AF_INET, SOCK_STREAM)

host = gethostname()
port = 5421
server_address = (host, port)

my_socket.connect(server_address)
my_socket.shutdown(SHUT_RD)


def send_block(msg: str):
    # send length
    length = header_struct.pack(len(msg))
    my_socket.sendall(length)
    # send message
    my_socket.sendall(msg.encode())


send_block('HI CLIENT DOF')
send_block('HIsdf sdfCLIENT DOF')
send_block('HdhfgfdI CLIENTdfs DOF')
send_block('')  # must send to done
