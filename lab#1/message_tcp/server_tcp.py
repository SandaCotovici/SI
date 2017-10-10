import socket
# ip and port that will be used to create the server
# '127.0.0.1' would do the same thing
IP = 'localhost'
PORT = 12344

#initialize the socket with default settings
tcp_server = socket.socket()

#bind the socket to an interface
tcp_server.bind((IP, PORT))
print('bind successful')
#make it listen
tcp_server.listen(5)

print('server is listening')
while True:
    #accept an incoming connection
    client_socket, addr = tcp_server.accept()

    #display some data about the connected client
    print('connection from:', addr)

    #receive a message (1024 bytes) from the client
    message = client_socket.recv(1024)
    print(message.decode())

    #send a message to the client
    mess = 'message is received'
    client_socket.send(mess.encode())

#close everything
client_socket.close()
tcp_server.close()
