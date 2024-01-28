import socket
import threading
from file_transaction import receive_file,send_file


PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '192.168.56.1'
ADDR = (SERVER,PORT)
ONE_MB_SIZE = 1024

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SENDING_FILE_MESSAGE = "!SENDING_FILE"
REQUESTING_FILE_MESSAGE = "!REQUESTING_FILE"

FILE_PATH_1= "file_transfer_socket\\assets\\one.txt"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)



def request_file_from_server():
    pass

def send_file_to_server():
    pass


send("Hello World !!!")
send("Second Message !!!")
send("Last message !!!")
# send(REQUESTING_FILE_MESSAGE)
# send(SENDING_FILE_MESSAGE)

send(DISCONNECT_MESSAGE)