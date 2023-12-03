import socket

host = '127.0.0.1'
port = 4000


def server():
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    print("Client Address: ", addr)
    while True:
        data = c.recv(1024)
        d = data.decode('ascii')
        print('Client: ', d)
        x = input('>>> ')
        y = x.encode('ascii')
        c.send(y)


server()