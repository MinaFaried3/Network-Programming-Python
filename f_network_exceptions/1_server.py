from socket import *

sock = socket(AF_INET, SOCK_STREAM)

# try:
#     sock.bind(("INVALID", 435))
# except OSError as err:
#     print("OSErrr in any error in network ", err.errno, err.strerror)
#
# try:
#     sock.bind(("INVALID", 435))
# except gaierror as err:
#     print("gaierror in any error in bind or connect ", err.errno, err.strerror)
#     # raise mean show error with all details
#     # raise

print("continue")

sock.bind((gethostname(), 435))
sock.listen()

while True:
    print("waiting....")
    conn, add = sock.accept()
    data = conn.recv(1024).decode()
    print(data)
    conn.sendall('hi can get me'.encode())
