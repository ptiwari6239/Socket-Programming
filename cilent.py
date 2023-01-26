import socket

PORT = 5050
FORMAT = "utf-8"
HEADER = 64
SERVER = "20.0.2.149"  # ip address of server 
ADDR = (SERVER,PORT)
cilent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cilent.connect(ADDR)
DISCONNECT_MESSAGE = "!CONNECT"

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    cilent.send(send_length)
    cilent.send(message)
    print(cilent.recv(2048).decode(FORMAT))

send("Hello SERVER, from CILENT")