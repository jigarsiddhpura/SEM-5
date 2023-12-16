import socket


def server():
    port = 8000
    host = "127.0.0.1"
    msg = "Prepare"
    log = msg
    over = 0
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(2)
    while 1:
        replies = []
        print(f"Co ordinator : {msg.lower()}")

        for i in range(3):
            conn, address = sock.accept()
            conn.send(msg.encode())
            data = conn.recv(1024).decode()
            replies.append(data.lower())
            print(f"subordinator {i} {address} : {data.lower()}")
        if over == 1:
            break
        if ("abort") in replies or len(replies) < 3:
            msg = "abort"
            print(f"trans abort \n final log : {log} {msg}")
            over = 1
        elif "success" in replies:
            msg = "complete"
            print(f"Transaction Complete\n {log} {msg}")
            over = 1
        else:
            msg = "commit"
        log += " " + msg


server()
