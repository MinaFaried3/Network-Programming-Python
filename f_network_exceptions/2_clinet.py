from socket import *


class MessageError(Exception):
    def __str__(self):
        return '%s: %s' % (self.args[0], self.__cause__.strerror)


sock = socket(AF_INET, SOCK_STREAM)

sock.settimeout(10)

try:
    sock.connect((gethostname(), 435))
    print(sock.recv(1024).decode())
except timeout as err:
    print("timeout error ", err.errno, err.strerror)
    raise MessageError('message not received')
