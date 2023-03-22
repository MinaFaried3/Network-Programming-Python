from socket import *
from threading import *

# 1- host,port
host = gethostname()
port = 12345
client_add = (host, port)

# 2- socket
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(client_add)

# 3- enter name
my_name = input("your name")


# 4- receive messages
def reveive():
    while True:
        try:
            # receive msg if nick send else print to console
            msg = client_socket.recv(1024).decode('ascii')
            if msg == "NICK":
                client_socket.sendall(my_name.encode('ascii'))
            else:
                print(msg)
        except:
            # close to socket
            print("error")
            client_socket.close()
            break


def write():
    while True:
        try:
            msg = my_name + " : " + input()
            client_socket.sendall(msg.encode('ascii'))
        except:
            print('error')


# receive and write thread
# don't forget to start

receive_thread = Thread(target=reveive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()
