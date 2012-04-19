#!/usr/bin/python
# Accepts connections, prints the received messages to stdout.

from socket import *
import threading
from time import sleep

__author__ = 'kiro'

class Receiver( threading.Thread ):
    serverHost="127.0.0.1"
    serverPort=5005

    def __init__(self, ip="127.0.0.1", port=5005, messageHandler=""):
        # initialize the thread.
        super(Receiver, self).__init__()

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
        if self.messageHandler == "":
            print "No messageHandler"
            exit()

        print "RECEIVER initialized"
        print "UDP target IP:", self.serverHost
        print "UDP target port:", self.serverPort

    def run(self):


# test code for running only this file.
#a = UDPReceiver("78.91.5.168", 0, "")
#a.run()
