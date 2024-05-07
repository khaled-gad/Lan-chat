import socket

PORT = 5050
SERVER = "192.168.106.22"
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "11                                                              !DISCONNECT"

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")
    connected = True
    while connected:
        msg = connection.recv(1024).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            connection.close()
        else:
            msg = msg[1:]
            print(msg.strip())
            response = input("Enter a message to send to the client: ")
            connection.send(response.encode(FORMAT))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn, addr = server.accept()
    handle_client(conn, addr)

if __name__ == "__main__":
    start_server()