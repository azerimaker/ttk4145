#!/usr/bin/python
# Accepts connections, prints the received messages to stdout.

from socket import *
import threading
from time import sleep

__author__ = 'kiro'

class TCPReceiver( threading.Thread ):
    serverHost="127.0.0.1"
    serverPort=5005

    def __init__(self, ip="127.0.0.1", port=5005, messageHandler=""):
        super(TCPReceiver, self).__init__()
        if ip == "":
            self.serverHost = "127.0.0.1"
        else:
            self.serverHost = ip

        if not port:
            self.serverPort = 5005
        else:
            self.serverPort = port
        self.messageHandler = messageHandler
        if self.messageHandler == "":
            print "No messageHandler"
            exit()
        print "RECEIVER initialized"
        print "UDP target IP:", self.serverHost
        print "UDP target port:", self.serverPort

    def run(self):
        # Open socket to listen on
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.serverHost, self.serverPort))
        sock.listen(1024)

        # Process connections
        while 1:
            # Accept connections
            connection, address = sock.accept()
            #print 'Connection accepted from %s' % str(address)
            # Receive data
            while 1:
                data = connection.recv(2 ** 16)
                ip = connection.getsockname()[0]
                port = connection.getsockname()[1]
                #print 'Received: %s' % str(data)
                self.messageHandler.evaluateCommand(ip, port, data)
                # Acknowledge reception of data
                #r = 'ACK\n'
                #connection.send(r)
                connection.close()
                break

# test code for running only this file.
#a = UDPReceiver("78.91.5.168", 0, "")
#a.run()
