from enum import Enum


class ClientHeaders(Enum):
    BASIC_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    SEND_FILE_HEADERS = {
        "Content-Type": "multipart/form-dada",
    }