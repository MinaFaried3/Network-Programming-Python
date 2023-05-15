from socket import *
from threading import *

ascii_ = "Ascii"
# 1 - repair socket
my_socket = socket(AF_INET, SOCK_STREAM)

# 2 - server address
host = gethostname()
port = 26145
server_add = (host, port)

# 3 - connect to server
my_socket.connect(server_add)

# 4 - taking nickname from user
nickname = input("Enter your name: ")


# 5- receive from sever
def receive():
    while True:
        try:
            msg = my_socket.recv(1024).decode(ascii_)
            if msg == "NICK":
                my_socket.sendall(nickname.encode(ascii_))
            else:
                print(msg)
        except:
            print("error occurred")
            my_socket.close()
            break


def write():
    while True:
        try:
            msg = nickname + " :: " + input("")
            my_socket.sendall(msg.encode(ascii_))
        except:
            print("error occurred")


thread1 = Thread(target=receive)
thread2 = Thread(target=write)
thread1.start()
thread2.start()
