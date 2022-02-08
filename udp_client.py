import socket
import sys
import json

deregister_cmd = {"command": "deregister", "username": ""}
msg_cmd = {"command": "msg", "username": "", "message": ""}
ret_cmd = {"command": "ret_code", "code_no": 0}
codes = {201: "Command parameters incomplete",
    301: "Command unknown",
    401: "Command accepted",
    501: "User not registered",
    502: "User account exists"}

def register(username):
    register_cmd = {"command": "register", "username": username}
    jsondata = json.dumps(register_cmd)
    print(f"Registering username {username}")
    sent = sock.sendto(bytes(jsondata, "utf-8"), (server_host, dest_port))
    data, server = sock.recvfrom(1024)
    print(codes[data["code_no"]])

def deregister():
    pass

def message():
    pass

server_host = "172.16.11.59"
dest_port = 12345
# server_host = input("Enter IP address of message board server: ")
# dest_port = int(input("Enter port number of message board server: "))
username = input("Enter preferred username: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
register(username)
