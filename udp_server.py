import socket
import json
import sys

# temporary hardcoded values
server_host = "172.16.0.20"
dest_port = 8003
# listening_address = input("Enter listening IP address: ")
# listening_port = input("Enter listening port number: ")
# listening_port = int(listening_port)
users = []

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server Starting up on %s port %d" % (listening_address, listening_port))

# bind socket to the port
sock.bind((listening_address, listening_port))

while True:
    # Waiting for data to arrive
    print("\nServer has started. Waiting for new messages.")
    data, address = sock.recvfrom(1024)
    print(data)
    temp = json.loads(data)

    if data:
        users.append(temp['username'])
        print("Users in message board: ", users)
