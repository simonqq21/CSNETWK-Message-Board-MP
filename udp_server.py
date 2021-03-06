import socket
import sys
import json
from common import commands, codes, code_definitions


def register(username, users):
    # If username isn't empty string
    if username:
        if username in users:
            code = codes["USER_ALREADY_EXISTS"]
            print(f"Username {username} already exists.")
        else:
            users.append(username)
            code = codes["COMMAND_ACCEPTED"]
            print(f"Username {username} just registered now.")
        print("Users in message board:", users)
    else:
        code = codes["INCOMPLETE_COMMAND_PARAMETERS"]
        print("Incomplete parameters were passed. Enter a valid username.")

    ret_cmd = {"command": "ret_code", "code_no": code}
    return ret_cmd


def deregister(username, users):
    # If username isn't an empty string
    if username:
        if username in users:
            users.remove(username)
            code = codes["COMMAND_ACCEPTED"]
            print(f"User {username} exiting...")
        else:
            code = codes["USER_NOT_REGISTERED"]
            print("No account will be unregistered...")
    else:
        code = codes["INCOMPLETE_COMMAND_PARAMETERS"]
        print("Incomplete parameters were passed.")

    ret_cmd = {"command": "ret_code", "code_no": code}
    if (len(users) > 0):
        print("Users in message board:", users)
    else:
        print("There are no users in the message board.")

    return ret_cmd


def msg(username, message, users):
    if username:
        if username in users:
            if message:
                code = codes["COMMAND_ACCEPTED"]
                print(f"from {username}:", message)
            else:
                code = codes["INCOMPLETE_COMMAND_PARAMETERS"]
                print("Incomplete parameters were passed.")
        else:
            # If client sent a message but the user is not registered
            code = codes["USER_NOT_REGISTERED"]
            print("An unregistered user is attempting to send a message. Please register before sending a message.")
    else:
        code = codes["INCOMPLETE_COMMAND_PARAMETERS"]
        print("Incomplete parameters were passed.")

    ret_cmd = {"command": "ret_code", "code_no": code}
    return ret_cmd


# temporary hardcoded values
# listening_address = "172.16.0.20"
# listening_port = 8003
listening_address = input("Enter listening IP address: ")
listening_port = input("Enter listening port number: ")
listening_port = int(listening_port)
users = []

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server Starting up on %s port %d" % (listening_address, listening_port))

# Bind socket to the port
sock.bind((listening_address, listening_port))
print("\nServer has started. Waiting for new messages.")

while True:
    # Waiting for data to arrive
    data, address = sock.recvfrom(1024)
    temp = json.loads(data)

    # get command and perform action
    command = temp["command"]

    if not command:
        code = codes["INCOMPLETE_COMMAND_PARAMETERS"]
        ret_cmd = {"command": "ret_code", "code_no": code}
        jsondata = json.dumps(ret_cmd)
        sent = sock.sendto(bytes(jsondata, "utf-8"), address)

    elif command == "register":
        newUsername = temp['username']
        newUsername = newUsername.lower()
        ret_cmd = register(newUsername, users)
        jsondata = json.dumps(ret_cmd)
        sent = sock.sendto(bytes(jsondata, "utf-8"), address)

    elif command == "deregister":
        deleteUser = temp['username']
        deleteUser = deleteUser.lower()
        print(f"from {deleteUser}: bye")
        ret_cmd = deregister(deleteUser, users)
        jsondata = json.dumps(ret_cmd)
        sent = sock.sendto(bytes(jsondata, "utf-8"), address)

    elif command == "msg":
        message = temp["message"]
        username = temp["username"]
        username = username.lower()
        ret_cmd = msg(username, message, users)
        jsondata = json.dumps(ret_cmd)
        sent = sock.sendto(bytes(jsondata, "utf-8"), address)

    else:
        code = codes["COMMAND_UNKNOWN"]
        ret_cmd = {"command": "ret_code", "code_no": code}
        jsondata = json.dumps(ret_cmd)
        sent = sock.sendto(bytes(jsondata, "utf-8"), address)
