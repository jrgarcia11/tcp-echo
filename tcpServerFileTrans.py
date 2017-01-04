# Echo server program
import socket
from commonFunctions import receiveMessageOfSize, commandExists, executeCommand

clientHost = ''
clientPort = 50007              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((clientHost, clientPort))
s.listen(1)
conn, addr = s.accept()  # wait until incoming request (and accept it)
print 'Connected by', addr

while 1:
    fullString = ""
    charReceived = ""
    while 1:                      #this while loop receives size of the message
        charReceived = conn.recv(1)
        if(charReceived == "~"):   #"~" separates size of message from actual message
            break
        fullString += charReceived
    stringSize = int(fullString)    #convert message size from string to int
    print 'Incoming string of size %d'% (stringSize)
    message = receiveMessageOfSize(stringSize, conn)
    print 'received: %s\n' % (message)

    if commandExists(message):
        executeCommand("server", message, conn)

    
conn.send(message.upper())
conn.close()
        
    
