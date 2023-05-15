from socket import *
from threading import *

# 1 - repair socket
my_socket = socket(AF_INET, SOCK_STREAM)

# 2 - server address
host = gethostname()
port = 26145
server_add = (host, port)

# 3 - bind
my_socket.bind(server_add)

# 4 - listen
my_socket.listen()

# 5 - lists
clients = []
nicknames = []


# 6 - send msg for all clients
def broadcast(msg: str):
    for client in clients:
        client.send(msg.encode("Ascii"))


# 7 - send msg from all clients and send it to all clients
def receive_msg(client: socket):
    while True:
        try:
            msg = client.recv(1024).decode("Ascii")
            broadcast(msg)
        except:
            print("error receive")
            # 1- find idx and remove client , nickname from list
            idx = clients.index(client)
            nickname = nicknames[idx]
            print(nickname + " has left the chat ")
            clients.remove(client)
            nicknames.remove(nickname)
            break


def handle():
    while True:
        # 6 - accept
        client, address = my_socket.accept()

        # 7 - send NICK
        client.send("NICK".encode("Ascii"))

        # 9 - recv
        nickname = client.recv(1024).decode()

        # 10 - append to clients and nicknames
        clients.append(client)
        nicknames.append(nickname)

        # 11 - call broadcast (nickname +'join')
        broadcast(nickname + " has joined to the chat")

        thread_recv = Thread(target=receive_msg, args=(client,))
        thread_recv.start()


print("server listening")
handle()
