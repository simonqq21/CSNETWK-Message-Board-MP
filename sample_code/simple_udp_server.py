import socket
import sys

#Set variables for listening address and listening port
listening_address="172.16.0.20" #Put in the IP address of server CSNET01
listening_port=8003

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
    print (data.decode("utf-8"))
    
    if data:
        #echo back received data from connecting client
        sent = sock.sendto(data, address)
        print ('sent %s bytes back to %s' % (sent, address))
