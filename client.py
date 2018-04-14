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
                try:
                    s.send(bytes(file, "utf8"))
                    f = open(client_path + file, "rb")
                    l = f.read(1024)
                    while(l):
                        s.send(l)
                        l=f.read(1024)
                        print("Sending file")
                    print("File sent")
                except FileNotFoundError:
                    continue
            else:
                if md5(client_path+file) != md5(server_path+file):
                    try:
                        s.send(bytes(file, "utf8"))
                        f = open(client_path + file, "rb")
                        l = f.read(1024)
                        while (l):
                            s.send(l)
                            l = f.read(1024)
                            print("Sending file")
                        print("File sent")
                    except FileNotFoundError:
                        continue

        for file in dirFiles_server:
            if file not in dirFiles_client:
                try:
                    os.remove(server_path+file)
                except FileNotFoundError:
                    continue


if __name__ == "__main__":
    sync()