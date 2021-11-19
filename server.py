import socket
import os

# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

# recieve 4096 bytes each time
BUFFER_SIZE = 4096

# create the server socket
s = socket.socket()

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept connection if there is any
client_socket, address = s.accept()

# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")

# name of output file
filename = "output.stl"

# start receiving the file from the socket and
# writing to the file stream
with open(filename, "wb") as f:
    while True:
        # read 4096 bytes from the socket
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            # done reading file
            break
        # write to the file the bytes we just recieved
        f.write(bytes_read)

# close the client socket
client_socket.close()

# close the server socket
s.close()