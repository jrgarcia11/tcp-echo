# tcp-echo
Includes a tcpClient, tcpServer, and a "stuttering" proxy. Server echoes messages sent by the client. I wrote parts of commonFunctions.py, tcpClient, and tcpServer as part of an assignment. Professor and TAs wrote proxy.

PURPOSE:
Creating a solution to dropped or delayed packets from scratch. Client is the sender, Server is the receiver, and stutter-forwarder simulates network congestion. Answers: How to reliably send information when packets can be dropped or delayed?

TO RUN:
After downloading, type 
$sudo bash ./autoRun.sh
which will open 3 windows: Client, Server, Proxy
(If there's a connection error, close the 3 windows and try running autoRun.sh again. Sometimes proxy doesnt create sockets fast enough)

TO TEST:
Type a message in the Client window when prompted. "Hello World!" will do fine as a test case.
Client will send message through proxy, and the proxy will "stutter" the message to the server.
The server will print the message once it has received all of it.

HOW IT WORKS:
Client is programmed to send messages in the format:
  message size in bytes~message
Example:
  12~Hello World!
The Client sends the size first, 
the server receives size integers until the sentinel character '~' is received, 
then the server receives bytes until bytes received equals the size.
