# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print("Socket successfully created")

server_path = "e:\\server\\"
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12347

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode

# a forever loop until we interrupt it or
# an error occurs
def accept_incoming_connection():
    i = 1
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)

        # send a thank you message to the client.
        l = c.recv(1024)
        while (l):
            f = open('file_' + str(i) + ".txt", 'wb')  # Open in binary
            i = i + 1
            print("receiving")
            print(l)
            f.write(l)
            l = c.recv(1024)
        f.close()
        print("received")
        # Close the connection with the client


if __name__ == "__main__":
    s.listen(5)
    print("socket is listening")
    accept_incoming_connection()
