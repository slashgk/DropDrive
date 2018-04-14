# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12347

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
f = open ("e:\\sync\\testing.txt", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
    print("Sending")
print("Sent")
# close the connection
s.close()