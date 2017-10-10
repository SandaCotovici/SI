import socket
import time
# client_socket = socket.socket
# socket.gethostname(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(socket.gethostname(), 8080)
# data = client_socket.recv(1024)
# print(data.decode('utf-8')) #pe linux, windows posibil sa fie ascii
# client_socket.sendall('Multumesc')
# client_socket.close()
IP = 'localhost'
PORT = 12344

for x in range(10):
    #initialize the socket with default settings
    client_socket = socket.socket()

    #connect to the server
    client_socket.connect((IP, PORT))
    print('connected successfuly')

    #send a message to the client (and encode it)
    # put in a for loop to send fixed number of messages

    mess = 'message is send'
    client_socket.send(mess.encode())
    time.sleep(5.0)

    #receive a message (1024 bytes) from the client
    # message = client_socket.recv(1024)
    # print(message.decode())

    #close everything
    client_socket.close()

# import socket
#
# def Main():
#         IP = '127.0.0.1'
#         port = 12324
#
#         mySocket = socket.socket()
#         mySocket.connect((IP,port))
#         print('connected successfuly')
#         message = input(" -> ")
#
#         while message != 'exit':
#                 mySocket.send(message.encode())
#                 data = mySocket.recv(1024).decode()
#
#                 print ('Received from server: ' + data)
#
#                 message = input(" -> ")
#
#         mySocket.close()
#
# if __name__ == '__main__':
#     Main()
