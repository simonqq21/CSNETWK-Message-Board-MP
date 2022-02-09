import socket
import sys
import json
from common import commands, codes, code_definitions

# deregister_cmd = {"command": "deregister", "username": ""}
# msg_cmd = {"command": "msg", "username": "", "message": ""}
# ret_cmd = {"command": "ret_code", "code_no": 0}


def register(username):
    # create register command to be sent to server
    register_cmd = {"command": commands["register"], "username": username}
    jsondata = json.dumps(register_cmd)
    print(f"Registering username {username}")
    sent = sock.sendto(bytes(jsondata, "utf-8"), (server_host, dest_port))
    data, server = sock.recvfrom(1024)

    #
    if data["code_no"] == codes["USER_NOT_REGISTERED"]:
        print("You have been registered!")
    elif data["code_no"] == codes["USER_ALREADY_EXISTS"]:
        print(f"Username {username} is already taken, please provide another unique username.")

def deregister():
    pass

def message():
    pass

# temporary hardcoded values
server_host = "172.16.0.20"
dest_port = 8003
# server_host = input("Enter IP address of message board server: ")
# dest_port = int(input("Enter port number of message board server: "))
username = input("Enter preferred username: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
register(username)
