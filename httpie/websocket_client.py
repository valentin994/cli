import socket
from websockets.client import ClientProtocol
from websockets.sync.client import ClientConnection
from websockets.uri import parse_uri
from websockets.exceptions import InvalidURI


def create_connection(uri, timeout: float = None) -> None:
    try:
        uri = parse_uri(uri)
    except InvalidURI:
        #TODO implement error handling
        print("invalid")
        pass
    protocol = ClientProtocol(uri)
    sock = socket.create_connection((uri.host, uri.port))
    connection = ClientConnection(sock, protocol, close_timeout=0.1)
    connection.handshake()
    send_message(connection, "hello")


def send_message(connection: ClientConnection, message: str) -> None:
    connection.send(message)

    print(f"sent message {message}")
    connection.close(reason="Message sent")
    pass
