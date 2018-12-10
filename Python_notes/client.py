
import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 123
server_socket.connect((host,port))
while True : 
    c_msg = server_socket.recv(1024)
    print("\t\t\tserver->",c_msg.decode())
    if c_msg.decode().strip().lower() == 'bye' :
        print("Connection Closed by Server")
        server_socket.close()
        break
    msg = input("\nclient->")
    server_socket.send(msg.encode())
    if msg.strip().lower() == 'bye' : 
        server_socket.send(msg.encode())
        print("Connection is closed by client")
        server_socket.close()
        break
