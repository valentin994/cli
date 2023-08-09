import socket
from websockets.client import ClientProtocol
from websockets.sync.client import ClientConnection
from websockets.uri import parse_uri
from websockets.exceptions import InvalidURI
import threading


def create_connection(uri, timeout: float = 0.1, message: str = None) -> None:
    try:
        uri = parse_uri(uri)
    except InvalidURI:
        # TODO implement error handling
        print("invalid")
        pass
    protocol = ClientProtocol(uri)
    sock = socket.create_connection((uri.host, uri.port))
    connection = ClientConnection(sock, protocol, close_timeout=timeout)
    connection.handshake()
    send_message(connection, message)


def send_message(connection: ClientConnection, message: str) -> None:
    if message:
        connection.send(message)
        connection.close(code=1000, reason="Sent the message")
    data = ""
    while data != "exit()":
        threading.Timer(5, connection.send)
        data = input()
        connection.send(data)
    connection.close(code=1000, reason="No more messages to be sent")
    pass
