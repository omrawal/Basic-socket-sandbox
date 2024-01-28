import socket
import threading
from file_transaction import receive_file,send_file


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
ONE_MB_SIZE = 1024

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SENDING_FILE_MESSAGE = "!SENDING_FILE"
REQUESTING_FILE_MESSAGE = "!REQUESTING_FILE"

FILE_PATH_1= "file_transfer_socket\\assets\\one.txt"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
# print(server)

# Create different function for send_file, receive_file


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        data = conn.recv(ONE_MB_SIZE).decode(FORMAT)
        if data:
            if data == DISCONNECT_MESSAGE:
                connected = False

            elif data == SENDING_FILE_MESSAGE:
                receive_file(conn)

            elif data == REQUESTING_FILE_MESSAGE:
                send_file(file_path=FILE_PATH_1,conn = conn)
            
            else:
                print(f"The message received is[{addr}] {data}.")
    conn.close()


def start():
    print(f"[STARTING] Server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn ,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

start()