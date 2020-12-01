import socket

HEADERSIZE = 32
DEFAULT_PORT = 1246


def start_client(ip=socket.gethostname(), port=DEFAULT_PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    fp = open("../file1.txt", "rb")

    msg = fp.read()
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg

    s.send(msg)
    s.close()
    fp.close()
