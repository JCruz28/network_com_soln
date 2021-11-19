import socket
import os

BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server
host = socket.gethostname()

# the port
port = 5001

# the name of the file we want to send
filename = "cad_mesh.stl"

# create the client socket
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# start sending the file
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # done reading the file
            break
        s.sendall(bytes_read)

# close the socket
s.close()    