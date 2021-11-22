# Author: Justin Cruz
# Date: 11/22/21
# Description: Client file that utilizes two different means
# of data transfer (Network sockets/PyZMQ) to send/recieve
# contents of an STL file.

import socket
import zmq

# send 4096 bytes each time step
BUFFER_SIZE = 4096 
# the name of the file we want to send
old_filename = "cad_mesh.stl"
# the name of the file we want to write to
new_filename = "output.stl"

# the ip address or hostname of the server (socket)
host = socket.gethostname()
# the port (socket)
port = 5001

# create the client sockets 
s = socket.socket()

context = zmq.Context()
zmqSock = context.socket(zmq.PAIR)

# connect sockets
print(f"[+] Connecting to {host}:{port} (socket)")
s.connect((host, port))
print("[+] Connected.")

print(f"[+] Connecting to tcp://localhost:5555 (zmq)")
zmqSock.connect("tcp://localhost:5555")
print("[+] Connected.")

# open files
old_file = open(old_filename, "rb")
new_file = open(new_filename, "wb")

# start sending the file
while True:
    # read the bytes from the file
    bytes_read = old_file.read(BUFFER_SIZE)
    if not bytes_read:
        # done reading the file
        break
    s.sendall(bytes_read)

    # wait to recieve bytes back amd write to file
    bytes_recieved = zmqSock.recv()
    new_file.write(bytes_recieved)

# close files
old_file.close()
new_file.close()

# close the sockets
s.close()
zmqSock.close()