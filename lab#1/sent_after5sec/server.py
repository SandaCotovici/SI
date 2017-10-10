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
    # client_socket.send(mess.encode())

#close everything
client_socket.close()
tcp_server.close()

# import socket
#
# def Main():
#     IP = "127.0.0.1"
#     port = 12324
#
#     mySocket = socket.socket()
#     mySocket.bind((IP,port))
#
#     mySocket.listen(5)
#     print('server is listening')
#     conn, addr = mySocket.accept()
#     print ("Connection from: " + str(addr))
#     while True:
#             data = conn.recv(1024).decode()
#             if not data:
#                     break
#             print ("from connected  user: " + str(data))
#
#             data = str(data).upper()
#             print ("sending: " + str(data))
#             conn.send(data.encode())
#
#     conn.close()
#
# if __name__ == '__main__':
#     Main()
