import socket
from datetime import datetime

# print(datetime.now().isoformat())

server_address = ('localhost', 6789)
max_size = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)

if data == b'time':
    server.sendto(datetime.now().isoformat().encode('utf-8'), client)
else:
    server.sendto(b'Please, send (time).')

server.close()