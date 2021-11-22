# Author: Justin Cruz
# Date: 11/22/21
# Description: Server file that utilizes two different means
# of data transfer (Network sockets/PyZMQ) to send/receive
# contents of an STL file.

import socket
import zmq

# recieve 4096 bytes each time
BUFFER_SIZE = 4096

# ip address and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

# create the server sockets
s = socket.socket()

context = zmq.Context()
zmqSock = context.socket(zmq.PAIR)

# bind the sockets
s.bind((SERVER_HOST, SERVER_PORT))

zmqSock.bind("tcp://*:5555")

# enabling our server to accept connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept connection if there is any
client_socket, address = s.accept()

# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")

# start sending data back to sender
while True:
    # read 4096 bytes from the socket
    bytes_read = client_socket.recv(BUFFER_SIZE)
    if not bytes_read:
        # done reading file
        break
    # send bytes we just recieved back to sender
    zmqSock.send(bytes_read)
    
# close the server sockets
s.close()
zmqSock.close()