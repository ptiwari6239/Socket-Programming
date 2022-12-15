import socket
import threading 


PORT = 6677
FORMAT = "utf-8"
HEADER = 64
hostname=socket.gethostname()
SERVER = socket.gethostbyname(hostname)
 
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
DISCONNECT_MESSAGE = "!CONNECT"

def handle_cilent(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.. ")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length :
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}]  {msg} ")
            conn.send("msg received: ".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[SERVER] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_cilent,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}" )


print("[SERVER] server is starting...")
start()



