# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print("Socket successfully created")

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
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)

        # send a thank you message to the client.
        c.send(bytes("Yo", "utf8"))

        # Close the connection with the client
        c.close()


if __name__ == "__main__":
    s.listen(5)
    print("socket is listening")
    accept_incoming_connection()