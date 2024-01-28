'''Module for sending and receiving file'''

ONE_MB_SIZE = 1024

# sending algo 
'''
Send file name
Send file size
Send file data
'''
def send_file(file_path,conn,FORMAT):
    print("sending file at path",file_path)
    filename = file_path.split('/')[-1]
    print("filename ",filename)

    conn.send(str(filename).encode(FORMAT))
    file = open(file_path,'r')
    data = file.read()
    conn.send(str(len(data)).encode(FORMAT))
    conn.send(str(data).encode(FORMAT))
    print("File sent")
    file.close()




# receiving algo
'''
Receive file name 
Create the file with the given name
Receive file size
Receive file data and write to created file and close 
'''
def receive_file(conn,FORMAT):
    print("Receiving file")
    file_name = conn.recv(ONE_MB_SIZE).decode(FORMAT)
    print("file name is",file_name)

    file_size = conn.recv(ONE_MB_SIZE).decode(FORMAT)
    print("file size is",int(file_size))
    
    file_data = conn.recv(int(file_size)).decode(FORMAT)
    file = open(file_name.split('.')[0]+"_Received"+file_name.split('.')[1],'w+')
    file.write(file_data)
    file.close()
    print("file received")