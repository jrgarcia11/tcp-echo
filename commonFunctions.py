import socket
import sys
import os
from time import gmtime, strftime

def receiveMessageOfSize(size, s):
    message = ""
    totalLength = 0
    while 1:                        #this while loop receives the actual message
        data = s.recv(1)
        if(data != ''):
            message += data
            dataLength = len(data)
            totalLength += dataLength
            if(totalLength == size): #while loop breaks once all characters... 
                break                     #...are received from client  
    return message

def commandExists(message):
    if isGETCommand(message) or isPUSHCommand(message):
        return True
    return False

def isGETCommand(message):
    command = message[0:3]
    if(command == "GET"):
        return True
    return False

def isPUSHCommand(message):
    command = message[0:4]
    if(command == "PUSH"):
        return True
    return False

def executeCommand(actor, command, sock): 
    if isPUSHCommand(command):
        fileString = command[5:]
        if(actor == "client"):
            push(actor, fileString, sock)
        if(actor == "server"):
            get(actor, fileString, sock)
        
    if isGETCommand(command):
        fileString = command[4:]
        if(actor == "client"):
            get(actor, fileString, sock)
        if(actor == "server"):
            push(actor, fileString, sock)
        
def push(actor, fileString, sock):
    try:
        myFile = open(actor + "/" + fileString, "rb")
        print 'sending ' + fileString + '...'
        filePath = actor + "/" + fileString
        fileSize = os.path.getsize(filePath)
        iterations = fileSize/100
        if(fileSize%100 > 0):
            iterations += 1
        for i in range(0,iterations):
            packetToSend = myFile.read(100)
            sock.send(packetToSend)
        myFile.close()
        print 'file sent\n'
    except (IOError, OSError):
        print 'ERROR: could not find file\n'
    
def get(actor, fileString, sock):
    try:
        timePrefix = strftime("%H%M%S")
        newFile = open(actor + "/" + timePrefix + fileString, "wb+")
        filePath = actorSwitch(actor) + "/" + fileString
        fileSize = os.path.getsize(filePath)
        print 'incoming file of size ' + str(fileSize)
        receivedSize = 0
        while receivedSize < fileSize:
            packetToReceive = sock.recv(128)
            newFile.write(packetToReceive)
            receivedSize += len(packetToReceive)
            print 'received %d of %d bytes' % (receivedSize, fileSize)
        newFile.close()
        print 'file transfer for ' + fileString + ' complete\n'

    except (IOError, OSError):
        print 'ERROR: could not find file\n'
        
def actorSwitch(actor):
    if (actor == 'server'):
        return 'client'
    if (actor == 'client'):
        return 'server'
