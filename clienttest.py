import pickle
import socket


s = socket.socket()
port = 12347
s.connect(('127.0.0.1', port))



lp = ['abc','syz','hajsgd']
filename = 'list_of_files'
outfile = open(filename,'wb')
pickle.dump(lp,outfile)
outfile.close()

s.send(bytes(filename,"utf8"))

