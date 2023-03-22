import threading
from socket import *

# 1- server address
host = gethostname()
port = 1234
server_address = (host, port)

# 2- socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen()

# 3- lists
clients = []
nicknames = []


# 4- send messages for all persons


def broadcast(message: str):
    for client in clients:
        client.send(message.encode('ascii'))
    return


def receive(from_client):
    while True:
        try:
            message = from_client.recv(1024)
            broadcast(message.decode('ascii'))
        except:
            print("======== SERVER RECEIVER ERROR =======")
            current_client_idx = clients.index(from_client)
            clients.remove(current_client_idx)
            current_nickname_idx = nicknames[current_client_idx]
            broadcast(current_nickname_idx + " has left the group")
            nicknames.remove(current_nickname_idx)
            break


def handle():
    while True:
        client, address = server_socket.accept()
        client.send("NICK".encode('ascii'))

        nickname = client.recv(1024).decode('ascii')
        clients.append(client)
        nicknames.append(nickname)

        broadcast(nickname + " join the chat room")

        thread = threading.Thread(target=receive, args=(client,))
        thread.start()


print("Server is listening")
handle()
