import socket
import time
IP = 'localhost'
PORT = 12344

for x in range(10):
    #initialize the socket with default settings
    client_socket = socket.socket()

    #connect to the server
    client_socket.connect((IP, PORT))
    print('connected successfuly')

    mess = 'message is send'
    client_socket.send(mess.encode())
    time.sleep(5.0)

    #close everything
    client_socket.close()
