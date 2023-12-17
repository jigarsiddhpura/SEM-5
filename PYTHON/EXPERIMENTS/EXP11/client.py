import socket

host = '127.0.0.1'
port = 4000


def client():
    s = socket.socket()
    s.connect((host, port))
    while True:
        x = input("Enter New Message: ")
        y = x.encode('ascii')
        s.send(y)
        data = s.recv(1024).decode('ascii')
        if not data:
            s.close()
            break
        print('Server: ', data)

client()