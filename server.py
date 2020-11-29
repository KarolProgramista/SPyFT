import socket
import time
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1246))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    new_msg = True
    full_msg = b''
    while True:
        msg = clientsocket.recv(32)
        if new_msg:
            print("New file size:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        print(f"Getting file: {min(len(full_msg), msglen)}/{msglen}")


        if len(full_msg)-HEADERSIZE >= msglen:
            print("File recived")
            print(full_msg[HEADERSIZE:])
            fp = open("file2.txt", "wb")
            fp.write(full_msg[HEADERSIZE:])
            fp.close()
            new_msg = True
            full_msg = b''
            break

    clientsocket.close()