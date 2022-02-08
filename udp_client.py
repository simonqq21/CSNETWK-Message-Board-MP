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

server_host = input("Enter IP address of message board server: ")
dest_port = int(input("Enter port number of message board server: "))
username = input("Enter preferred username: ")

import socket
import sys
#Set variables for listening address and listening port
listening_address='w.x.y.z' #Put in the IP address of the server computer
listening_port=12345
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
print ("starting up on %s port %d" %(listening_address, listening_port))
sock.bind((listening_address, listening_port))
while True:
#waiting for data to arrive, this is a blocking function
print ('\nwaiting to receive message')
data, address = sock.recvfrom(1024)
print ('received %s bytes from %s' % (len(data), address))
1print (data.decode("utf-8"))
if data:
#echo back received data from connecting client
sent = sock.sendto(data, address)
print ('sent %s bytes back to %s' % (sent, address))
