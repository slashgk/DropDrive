# first of all import the socket library
import socket
import pickle
import os
# next create a socket object
s = socket.socket()
print("Socket successfully created")

server_path = "e:\\server\\"

port = 12347

s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode

# a forever loop until we interrupt it or
# an error occurs
def accept_incoming_connection():
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        while True:
            dirFiles_server= os.listdir(server_path)
            filename = 'list_of_files'
            outfile = open(filename, 'wb')
            pickle.dump(dirFiles_server, outfile)
            outfile.close()
            c.send(bytes(filename, "utf8"))
            size = c.recv(16)  # Note that you limit your filename length to 255 bytes.
            if not size:
                break
            size = int(size, 2)
            filename = c.recv(size).decode("utf8")
            filesize = c.recv(32).decode("utf8")
            filesize = int(filesize, 2)
            file_to_write = open(server_path+filename, 'wb')
            chunksize = 4096
            while filesize > 0:
                if filesize < chunksize:
                    chunksize = filesize
                data = c.recv(chunksize)
                file_to_write.write(data)
                filesize -= len(data)

            file_to_write.close()
            print('File received successfully'+filename)
        # Close the connection with the client


if __name__ == "__main__":
    s.listen(5)
    print("socket is listening")
    accept_incoming_connection()