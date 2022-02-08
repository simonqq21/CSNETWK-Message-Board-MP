import socket
import sys


listening_address = input("Enter listening IP address: ")
listening_port = input("Enter listening port number: ")
listening_port = int(listening_port)

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind socket to the port
s.bind((listening_address, listening_port))

while True:
    # Waiting for data to arrive
    data, address = s.recvfrom(1024)
