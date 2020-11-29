import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1246))
fp = open("file1.txt", "rb")

msg = fp.read()
# msg = pickle.dumps(d)
msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg

s.send(msg)
s.close()
fp.close()