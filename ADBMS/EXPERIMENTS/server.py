import socket
host = "127.0.0.1"
port = 8000

s = socket.socket()
s.bind((host,port))
s.listen(3)
print("SERVER IS RUNNING")

msg = "PREPARE"
log=msg

over = 0

while True:
    replies = []
    print(f"COORDINATOR: {msg.upper()}")
    for i in range(3):
        c,adrr = s.accept()
        c.send(msg.encode())
        data = c.recv(1024).decode()
        replies.append(data.upper())
        print(f"Subordinator {i} {adrr} : {data.upper()}")
    if over == 1:
        break
    if "ABORT" in replies:
        msg = "ABORT"
        print(f"TRANSACTION LOG : {log} {msg}")
        over = 1
    elif "SUCCESS" in replies:
        msg = "COMPLETE"
        print(f"TRANSACTION LOG : {log} {msg}")
        over = 1
    else:
        msg = "COMMIT"
        log += " "+msg
    