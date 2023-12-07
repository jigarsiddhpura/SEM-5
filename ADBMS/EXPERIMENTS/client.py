#Client

import socket
host = "127.0.0.1"
port = 8000
log = ""
over = 0
msg =""

while True:
    try:
        s = socket.socket()
        s.connect((host,port))
        data = s.recv(1024).decode().upper()
        print(f"COORDINATOR: {data}")
        if data == "ABORT":
            msg = "OK"
            print("TRANSACTION ABORTED!")
            print("END OF TRANSACTION\n final log is: ",log+" "+data)
            over =1
        elif data =="COMPLETE":
            msg="OK"
            print("TRANSACTION COMPLETED!")
            print("END OF TRANSACTION\n final log is: ",log+" "+data)
            over =1
        else:
            data = input("SYSTEM STATUS: ").upper()
            s.send(data.encode())
            log += data+" "
        if over == 1:
            break
    except:
        print("END OF TRANSACTION\n final log is: ",log+" "+data)
        break