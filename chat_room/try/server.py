from socket import *
from threading import *

# 1- host,port
host = gethostname()
port = 12345
server_add = (host, port)

# 2- socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(server_add)
server_socket.listen()

# 3- lists
clients = []
names = []


# 4- broadcast
def broadcast(msg: str):
    for client in clients:
        client.send(msg.encode('ascii'))
    return


# 5- receive
def receive(from_cli):
    while True:
        try:
            # accept from one and send to others
            msg = from_cli.recv(1024)
            broadcast(msg.decode('ascii'))
        except:
            # remove from two lists and tell others
            print("server error")
            curr_idx = clients.index(from_cli)
            clients.remove(curr_idx)
            name = names[curr_idx]
            broadcast(name + "has left the group")
            names.remove(name)
            break


def handle():
    # 1- accept
    client, address = server_socket.accept()
    # 2- send nick
    client.send("NICK".encode('ascii'))
    # 3- get name
    name = client.recv(1024).decode('ascii')
    # 4- add to lists
    clients.append(client)
    names.append(name)
    # 5- tell all
    broadcast(name + " join chat")
    # 6- thread
    thread = Thread(target=receive, args=(client,))
    thread.start()


handle()
