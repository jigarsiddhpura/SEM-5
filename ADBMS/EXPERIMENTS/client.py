import socket


def client():
    port = 8000
    host = "127.0.0.1"
    log = ""
    over = 0

    while 1:
        try:
            sock = socket.socket()
            sock.connect((host, port))
            rec_data = sock.recv(1024).decode().lower()
            print("Coordinator : ", rec_data)
            if rec_data == "abort":
                over = 1
                msg = "ok"
                print("trans ends as aborted")
            elif rec_data == "success":
                over = 1
                msg = "ok"
                print("trans complete")
            else:
                msg = input("System status : ").lower()
                log += " " + msg
            sock.send(msg.encode())
            if over == 1:
                break
            sock.close()
        except Exception as e:
            print(f"Transaction ends log : {log}")
            break


client()
