import socket

host = '127.0.0.1'
port = 4000


def server():
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print("Client Address: ", addr)
    while True:
        data = conn.recv(1024).decode('ascii')
        print('Client: ', data)
        if "exit" in data:
            conn.close()
            break
        x = input('>>> ')
        y = x.encode('ascii')
        conn.send(y)


server()