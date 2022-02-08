import socket
import sys

#Set variables for server address and destination port
server_host='172.16.0.20' #IP address of the server CSNET01
dest_port=8003

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = 'This is the message.  It will be repeated.'

try:

    # Send data, string has to be sent as 'bytes' as string in Python is in Unicode format
    print('sending "%s"' % message)
    sent = sock.sendto(bytes(message,"utf-8"), (server_host,dest_port))

    # waiting for server to send data back, this is blocking function
    print ('waiting to receive')
    data, server = sock.recvfrom(1024)
    print ('received "%s"' % data.decode("utf-8"))

finally:
    #close socket
    print ('closing socket')
sock.close()
