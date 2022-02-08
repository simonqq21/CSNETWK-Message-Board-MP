import socket
import sys
import json

register_cmd = {"command": "register", "username": ""}
deregister_cmd = {"command": "deregister", "username": ""}
msg_cmd = {"command": "msg", "username": "", "message": ""}
ret_cmd = {"command": "ret_code", "code_no": 0}
codes = {201: "Command parameters incomplete",
    301: "Command unknown",
    401: "Command accepted",
    501: "User not registered",
    502: "User account exists"}

def register():
    pass

def deregister():
    pass

def message():
    pass

server_host = input("Enter IP address of message board server: ")
dest_port = int(input("Enter port number of message board server: "))
username = input("Enter preferred username: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
