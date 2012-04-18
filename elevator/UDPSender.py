import socket

__author__ = 'kiro'

class UDPSender:
    UDP_IP = ""
    UDP_PORT = 0

    def __init__(self, ip, port):
        # Set the ip to default or given value.
        if ip=="":
            self.UDP_IP = "127.0.0.1"
        else:
            self.UDP_IP = ip

        # Set the port to default or given value.
        if port=="":
                self.UDP_PORT = 5005
        else:
            self.UDP_PORT = port

        print "SENDER initialized"
        print "UDP target IP:", self.UDP_IP
        print "UDP target port:", self.UDP_PORT

    def send(self, message):

        print "message:", message

        sock = socket.socket( socket.AF_INET, # Internet
            socket.SOCK_DGRAM ) # UDP

        sock.sendto( message, (self.UDP_IP, self.UDP_PORT) )


# test code for running only this file.
#a = UDPSender("78.91.5.168")
#a.send("testing")