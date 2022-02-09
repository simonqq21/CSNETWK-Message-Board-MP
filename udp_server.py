import socket
import sys
import json
from common import commands, codes

def register(username):
    if username in users:

        ret_cmd = {"command": "ret_code", "code_no": 0}
    users.append(username)
    print("Users in message board: ", users)


def deregister():
    pass

# temporary hardcoded values
listening_address = "172.16.0.20"
listening_port = 8003
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
    # print(data)
    temp = json.loads(data)

    # get command and perform action
    command = temp["command"]
    if command == "register":
        newUsername = temp['username']
        register(newUsername)
