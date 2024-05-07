import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = "192.168.106.22"
ADDRESS = (SERVER, PORT)

def send_message(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    while True:
        msg = input("Enter a message to server: ")
        send_message(client, msg)
        if msg == DISCONNECT_MESSAGE:
            break
    client.close()

if __name__ == "__main__":
    start_client()