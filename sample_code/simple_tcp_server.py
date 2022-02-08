import socket               # Import socket module

s = socket.socket()
host='172.16.0.20'	    #Listening IP address
port=8003		    #Reserve a port number for your service

s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   msg=b'Thank you for connecting'
   c.send(msg)
   c.close()                # Close the connection

