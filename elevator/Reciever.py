#!/usr/bin/python
# Accepts connections, prints the received messages to stdout.

from socket import *
import threading
from time import sleep

__author__ = 'kiro'

class UDPReceiver( threading.Thread ):
    serverHost="127.0.0.1"
    serverPort=5005

    def __init__(self, ip, port, messageHandler):
        # initialize the thread.
        super(UDPReceiver, self).__init__()

        # Set the ip to default or given value.
        if ip=="":
            self.serverHost = "127.0.0.1"
        else:
            self.serverHost = ip

        # Set the port to default or given value.
        if not port:
            self.serverPort = 5005
        else:
            self.serverPort = port

        self.messageHandler = messageHandler

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
            print 'Connection accepted from %s' % str(address)
            # Receive data
            while 1:
                data = connection.recv(2 ** 16)
<<<<<<< HEAD
                ip = connection.getsockname
                print 'Received: %s' % str(data)
                self.messageHandler.evaluateCommand(ip, data)
=======
                print 'Received: %s' % str(data)
                self.messageHandler.evaluateCommand(data)
>>>>>>> f251ea31986342f57ba64e55dff37d1f702fc74c
                # Acknowledge reception of data
                r = 'ACK\n'
                connection.send(r)
                connection.close()
                break

# test code for running only this file.
#a = UDPReceiver("78.91.5.168", 0, "")
#a.run()
