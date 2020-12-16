import enum
HEADERSIZE = 32
DEFAULT_PORT = 1246
DEFAULT_PATH = "./downloaded"
TRANSFER_SPEED = 32


class ErrorCodes (enum.Enum):
    FILENAME_TRANSFER_FAIL = 1
    FILE_TRANSFER_FAIL = 2
