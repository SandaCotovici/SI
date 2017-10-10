import socket
import time

IP = 'localhost'
PORT = 12344

#initialize the socket with default settings
client_socket = socket.socket()

#connect to the server
client_socket.connect((IP, PORT))
print('connected successfuly')

#send a message to the client (and encode it)
mess = 'message is send to server'
client_socket.send(mess.encode())

#receive a message (1024 bytes) from the client
message = client_socket.recv(1024)
print(message.decode())

#close everything
client_socket.close()
