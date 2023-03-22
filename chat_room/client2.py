import threading
from socket import *

# 1- server address
host = gethostname()
port = 1234
server_address = (host, port)

# 2- socket
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_address)

nickname = input("Enter your name :  ")


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == "NICK":
                client_socket.sendall(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("an error occurred ")
            client_socket.close()
            break


def write():
    while True:
        try:
            msg = nickname + " : " + input()
            client_socket.sendall(msg.encode('ascii'))
        except:
            print("write error")
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
