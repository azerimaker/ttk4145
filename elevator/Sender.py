from socket import *

__author__ = 'kiro'

class UDPSender:
    recipientHost = ""
    recipientPort = 0

    def __init__(self, ip, port):
        # Set the ip to default or given value.
        if ip=="":
            self.recipientHost = "127.0.0.1"
        else:
            self.recipientHost = ip

        # Set the port to default or given value.
        if not port:
                self.recipientPort = 5005
        else:
            self.recipientPort = port

        print "SENDER initialized"
        print "UDP target IP:", self.recipientHost
        print "UDP target port:", self.recipientPort

    def send(self, message):

        print "message:", message

        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((self.recipientHost, self.recipientPort))

        sock.send(message)
        #sock.send( message, (self.recipientHost, self.recipientPort) )

        sock.close()


# test code for running only this file.
#a = UDPSender("78.91.5.168", "")
#a.send("testing")