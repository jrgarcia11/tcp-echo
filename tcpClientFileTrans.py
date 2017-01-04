# Echo client program
import socket
import sys
from commonFunctions import receiveMessageOfSize, commandExists, executeCommand

serverHost = 'localhost'
serverPort = 50006

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print "creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto)
        s = socket.socket(af, socktype, proto)
    except socket.error, msg:
        print " error: %s" % msg
        s = None
        continue
    try:
        print " attempting to connect to %s" % repr(sa)
        s.connect(sa)
    except socket.error, msg:
        print " error: %s" % msg
        s.close()
        s = None
        continue
    break

if s is None:
    print 'could not open socket'
    sys.exit(1)
print 'Connected'

while 1:
    outMessage = raw_input("message: ")
    strLength = len(outMessage)
    outSize = "%d" % strLength
    sentinel = "~"
    s.send(outSize)
    s.send(sentinel)
    print 'client sending %d bytes' % (strLength)
    print "client sending '%s'\n" % outMessage
    s.send(outMessage)

    if commandExists(outMessage):
        executeCommand("client", outMessage, s)
    
s.close()

