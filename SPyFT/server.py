import socket

HEADERSIZE = 32
DEFAULT_PORT = 1246


def start_server(port=DEFAULT_PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), port))
    s.listen(5)

    downloading_new_file = True
    full_file = b''
    file_len = 0
    while True:
        # now our endpoint knows about the OTHER endpoint.
        client_socket, address = s.accept()
        print(f"Connection from {address} has been established.")
        while True:
            # TODO: Add adjustable transfer speed
            msg = client_socket.recv(32)
            if downloading_new_file:
                print("New file size:", msg[:HEADERSIZE])
                file_len = int(msg[:HEADERSIZE])
                downloading_new_file = False

            full_file += msg

            print(f"Getting file: {min(len(full_file), file_len)}/{file_len}")

            if len(full_file)-HEADERSIZE >= file_len:
                print("File received")
                print(full_file[HEADERSIZE:])
                fp = open("file2.txt", "wb")
                fp.write(full_file[HEADERSIZE:])
                fp.close()
                downloading_new_file = True
                full_file = b''
                break

        client_socket.close()
