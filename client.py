import os
import shutil
import hashlib
import socket
import pickle

s = socket.socket()
port = 12347
c=s.connect(('127.0.0.1', port))
print(c)

client_path = "e:\\sync\\"


def md5(fname):
    try:
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
            return 0


def sync():
    dirFiles_client = os.listdir(client_path)
    
    while True:
        for file in dirFiles_client:
            print("hhasdg")
            if file not in dirFiles_server:
                filename = file
                size = len(filename)
                size = bin(size)[2:].zfill(16)  # encode filename size as 16 bit binary
                s.send(bytes(size,"utf8"))
                s.send(bytes(filename,"utf8"))

                filename = os.path.join(client_path, filename)
                filesize = os.path.getsize(filename)
                filesize = bin(filesize)[2:].zfill(32)  # encode filesize as 32 bit binary
                s.send(bytes(filesize,"utf8"))

                file_to_send = open(filename, 'rb')

                l = file_to_send.read()
                s.sendall(l)
                file_to_send.close()
                print("File sent:"+file)


if __name__ == "__main__":
    sync()