import socket


def server():
    # 1- server address
    host = socket.gethostname()
    port = 333
    server_address = (host, port)

    # 2- create socket object
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 3- bind my_socket with server address and listen
    my_socket.bind(server_address)
    my_socket.listen(1)

    while True:
        print('Waiting for client ........')

        # 1- accept from clients
        connection, add = my_socket.accept()
        print('connection : ')
        print(connection)
        print('address : ')
        print(add)

        # 2- receive message
        msg = connection.recv(2048)
        print(msg.decode())

        # 3- send to client
        connection.sendall('SERVER: message received'.encode())

        # 4- close connection
        connection.close()


# print(len('SERVER: message received'))
# call the function
server()
