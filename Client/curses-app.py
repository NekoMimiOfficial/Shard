import common
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 10039))
data = "2837c9a98"*1000
data = data.encode()
datLen = len(data)
print(datLen)
payload = b''.join([
    int(1).to_bytes(1),
    int(1).to_bytes(1),
    int(datLen).to_bytes(4),
    data
])
print(len(payload))
sock.send(payload)
