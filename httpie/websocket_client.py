import socket
from websockets.client import ClientProtocol 
from websockets.sync.client import ClientConnection 
from websockets.uri import parse_uri
from pprint import pprint as print

WS_URI = "ws://127.0.0.1:8000"

wsuri = parse_uri(WS_URI)

protocol = ClientProtocol(wsuri)
sock = socket.create_connection((wsuri.host, wsuri.port), None)

connection = ClientConnection(sock, protocol)

connection.handshake()
connection.send("Hello from client")
print(connection.request.headers)
print(connection.protocol.connect())
events = connection.recv()
connection.close()