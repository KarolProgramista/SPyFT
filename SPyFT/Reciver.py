import socket
from SPyFT.settings import *


# TODO: Add return codes
class Receiver(object):
    def __init__(self, port=DEFAULT_PORT, save_path=DEFAULT_PATH):
        self.port = port
        self.save_path = save_path
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), self.port))
        self.socket.listen(5)

    def receiver_mainloop(self):
        while True:
            self.receive_file()

    def receive_file(self):
        file_content, file_name = self.receive_file_as_string()
        fp = open(f"{self.save_path}/{file_name}", "wb")
        fp.write(file_content)
        fp.close()

    def receive_file_as_string(self):
        downloading_new_file = True
        full_file = b''
        file_len = 0

        client_socket, address = self.socket.accept()
        print(f"Connection from {address} has been established.")
        file_name = self.__receive_file_name(client_socket)
        while True:
            # TODO: Add adjustable transfer speed
            msg = client_socket.recv(32)
            if downloading_new_file:
                print(f"New file {file_name} size:", msg[:HEADERSIZE])
                file_len = int(msg[:HEADERSIZE])
                downloading_new_file = False

            full_file += msg

            print(f"Getting file: {min(len(full_file), file_len)}/{file_len}")

            if len(full_file) - HEADERSIZE >= file_len:
                print(f"File {file_name} received")
                client_socket.close()
                return [full_file[HEADERSIZE:], file_name]

    def __receive_file_name(self, client_socket):
        receiving_new_file_name = True
        full_file_name = b''
        file_name_len = 0

        while True:
            # TODO: Add adjustable transfer speed
            msg = client_socket.recv(32)
            if receiving_new_file_name:
                print("New file name size:", msg[:HEADERSIZE])
                file_name_len = int(msg[:HEADERSIZE])
                receiving_new_file_name = False

            full_file_name += msg

            print(f"Getting file name")

            if len(full_file_name) - HEADERSIZE >= file_name_len:
                print("File name received")
                return full_file_name[HEADERSIZE:].decode('utf-8')
