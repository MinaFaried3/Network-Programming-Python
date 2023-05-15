from socket import *

# 1 - repair my socket
my_socket = socket(AF_INET, SOCK_STREAM)

# 2 - set options SO_REUSEADDR
my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 3 - server address
host = gethostname()
port = 672
server_address = (host, port)

# 4 - bind socket to address
my_socket.bind(server_address)

# 5 - start listening
my_socket.listen(1)

while True:
    print("Waiting for client .... ")

    # 6 - accept connection , address
    connection, address = my_socket.accept()
    print("connection value : ", connection)

    # 7 - get connection msg from client
    connection_msg = connection.recv(1024)
    print(connection_msg.decode())

    # 8 - sendall
    connection.sendall("Server : sends message ".encode())

    # 9 - close connection
    connection.close()



