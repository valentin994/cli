import socket
from websockets.client import ClientProtocol
from websockets.sync.client import ClientConnection
from websockets.uri import parse_uri
from websockets.exceptions import InvalidURI


def create_connection(uri, timeout: int = None):
    print(uri)
    try:
        uri = parse_uri(uri)
    except InvalidURI:
        #TODO implement error handling
        print("invalid")
        pass
    protocol = ClientProtocol(uri)
    sock = socket.create_connection((uri.host, uri.port), timeout)
    connection = ClientConnection(sock, protocol)
    connection.handshake()
    print(connection)
    return connection

#connection.send("Hello from client")
#print(connection.request.headers)
#print(connection.protocol.connect())
#events = connection.recv()
#connection.close()
