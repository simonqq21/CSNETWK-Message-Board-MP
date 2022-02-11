import socket
import sys
import json
from common import commands, codes, code_definitions, deregister_message

def register(username):
    # create register command to be sent to server
    register_cmd = {"command": commands["register"], "username": username}
    jsondata = json.dumps(register_cmd)
    print(f"Registering username {username}")
    sent = sock.sendto(bytes(jsondata, "utf-8"), (server_host, dest_port))
    data, server = sock.recvfrom(1024)

    returnedCmd = json.loads(data)
    # interpret the returned code from the server
    if returnedCmd["code_no"] == codes["USER_ALREADY_EXISTS"]:
        print(f"User account already exists in chatroom!")
        return 666
    elif returnedCmd["code_no"] == codes["USER_NOT_REGISTERED"]:
        print("Registered successfully!")
    elif returnedCmd["code_no"] == codes["INCOMPLETE_COMMAND_PARAMETERS"]:
        print("Incomplete parameters were passed.")
    return 0

def deregister(username):
    # create deregister command to be sent to server
    deregister_cmd = {"command": commands["deregister"], "username": username}
    jsondata = json.dumps(deregister_cmd)
    print(f"Deregistering username {username}")
    sent = sock.sendto(bytes(jsondata, "utf-8"), (server_host, dest_port))
    data, server = sock.recvfrom(1024)

    returnedCmd = json.loads(data)
    # interpret the returned code from the server
    if returnedCmd["code_no"] == codes["USER_NOT_REGISTERED"]:
        print(f"User account is not registered yet.")
        return 666
    elif returnedCmd["code_no"] == codes["INCOMPLETE_COMMAND_PARAMETERS"]:
        print("Incomplete parameters were passed.")
        return 667
    elif returnedCmd["code_no"] == codes["COMMAND_ACCEPTED"]:
        print("Disconnected.")
    return 0

def send_message(username, message):
    if message == deregister_message:
        return
    # create message command to be sent to server
    msg_cmd = {"command": commands["message"], "username": username, "message": message}
    jsondata = json.dumps(msg_cmd)
    print(f"Sending message")
    sent = sock.sendto(bytes(jsondata, "utf-8"), (server_host, dest_port))
    data, server = sock.recvfrom(1024)

    returnedCmd = json.loads(data)
    # interpret the returned code from the server
    if returnedCmd["code_no"] == codes["INCOMPLETE_COMMAND_PARAMETERS"]:
        print("Incomplete parameters were passed.")
        return 666
    elif returnedCmd["code_no"] == codes["COMMAND_ACCEPTED"]:
        print("Message sent successfully.")
    return 0


# temporary hardcoded values
server_host = "172.16.0.20"
dest_port = 8003
# server_host = input("Enter IP address of message board server: ")
# dest_port = int(input("Enter port number of message board server: "))
username = input("Enter preferred username: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result = register(username)
# continue if registration successful, exit otherwise
if result == 0:
    message = ""
    while message != deregister_message:
        message = input("Enter message: ")
        send_message(username, message)
else:
    print("Unsuccessful registration, exiting")
    exit()
deregister(username)
