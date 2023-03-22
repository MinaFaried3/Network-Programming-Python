from socket import *


def server():
    # 1- server address
    host = gethostname()
    port = 789
    server_address = (host, port)

    # 2- socket object and set option
    my_socket = socket(AF_INET, SOCK_STREAM)
    my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 3- start bind address to socket and start listen
    my_socket.bind(server_address)
    my_socket.listen(1)

    while True:
        print('Waiting FROM SERVER !')

        # 1- accept the connection
        connection, address = my_socket.accept()
        print(connection)
        print(address)

        # 2- receive data
        msg = connection.recv(1023)
        print(msg.decode())

        # 3- send all
        connection.sendall('RECEIVED FROM SERVER !@@@'.encode())

        # 4- close
        connection.close()


print(len('RECEIVED FROM SERVER !@@@'))
server()
