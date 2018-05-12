# first of all import the socket library
import socket
import pickle
# next create a socket object
s = socket.socket()
print("Socket successfully created")


port = 12347

s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
c, addr = s.accept()
print('Got connection from', addr)

filename = c.recv(13)
print(type(filename))
infile = open(filename,'rb')
new_lp = pickle.load(infile)
infile.close()

print(new_lp)