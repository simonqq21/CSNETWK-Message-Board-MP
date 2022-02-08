import socket

HOST = '172.16.0.20'  # The server's hostname or IP address
PORT = 8003        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received data: ', data.decode('utf-8'))
