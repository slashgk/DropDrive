import os
import shutil
import hashlib
import socket

s = socket.socket()
port = 12347
s.connect(('127.0.0.1', port))


client_path = "e:\\sync\\"
server_path = "e:\\server\\"


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
    while True:
        dirFiles_client = os.listdir(client_path)
        dirFiles_server = os.listdir(server_path)
        for file in dirFiles_client:
            if file not in dirFiles_server:
                filename = file
                size = len(filename)
                size = bin(size)[2:].zfill(16)  # encode filename size as 16 bit binary
                #print(type(size))
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
            else:
                if md5(client_path+file) != md5(server_path+file):
                    filename = file
                    size = len(filename)
                    size = bin(size)[2:].zfill(16)  # encode filename size as 16 bit binary
                    # print(type(size))
                    s.send(bytes(size, "utf8"))
                    s.send(bytes(filename, "utf8"))

                    filename = os.path.join(client_path, filename)
                    filesize = os.path.getsize(filename)
                    filesize = bin(filesize)[2:].zfill(32)  # encode filesize as 32 bit binary
                    s.send(bytes(filesize, "utf8"))

                    file_to_send = open(filename, 'rb')

                    l = file_to_send.read()
                    s.sendall(l)
                    file_to_send.close()
                    print("File sent:" + file)

        for file in dirFiles_server:
            if file not in dirFiles_client:
                try:
                    os.remove(server_path+file)
                except FileNotFoundError:
                    continue


if __name__ == "__main__":
    sync()