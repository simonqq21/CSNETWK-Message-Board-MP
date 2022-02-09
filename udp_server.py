import socket
import json
import sys


listening_address = input("Enter listening IP address: ")
listening_port = input("Enter listening port number: ")
listening_port = int(listening_port)
users = []

# 201 - parameters incomplete; 301 - command unkown; 401 - command accepted
# 501 - user not registered; 502 - User account exists
ret_codes = [{"command": "ret_code", "code_no": 201},
             {"command": "ret_code", "code_no": 301},
             {"command": "ret_code", "code_no": 401},
             {"command": "ret_code", "code_no": 501},
             {"command": "ret_code", "code_no": 502}]

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server Starting up on %s port %d" % (listening_address, listening_port))

# Bind socket to the port
sock.bind((listening_address, listening_port))
print("\nServer has started. Waiting for new messages.")

while True:
    # Waiting for data to arrive
    data, address = sock.recvfrom(1024)
    print("#############")
    print("Data sent: ")
    print(data)
    print("Type of data: ", type(data))
    print("#############")
    data_sent = json.loads(data)
    print("#############")
    print("Data sent: ")
    print(data_sent)
    print("Type of data: ", type(data_sent))
    print("#############")

    if data:
        cmd = data_sent['command']
        uname = data_sent['username']
        print("Address: \n", address)

        if cmd == "register":
            users.append(uname)
            print("Users in message board: ", users)
            jsondata = json.dumps(ret_codes[2])
            sent = sock.sendto(bytes(jsondata, "utf-8"), address)

        if cmd == "deregister":
            print("User %s exiting...", uname)
            users.remove(uname)
            print("Users in message board: ", users)
            jsondata = json.dumps(ret_codes[2])
            sent = sock.sendto(bytes(jsondata, "utf-8"), address)
