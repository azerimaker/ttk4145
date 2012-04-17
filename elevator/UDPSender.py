import socket

__author__ = 'kiro'

class UDPSender:
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    def __init__(self, ip):
        if ip=="":
            self.UDP_IP = "127.0.0.1"
        else:
            self.UDP_IP = ip

        print "SENDER initialized"
        print "UDP target IP:", self.UDP_IP
        print "UDP target port:", self.UDP_PORT

    def send(self, message):

        print "message:", message

        sock = socket.socket( socket.AF_INET, # Internet
            socket.SOCK_DGRAM ) # UDP

        for x in xrange(1,10):
            sock.sendto( str(x)+message, (self.UDP_IP, self.UDP_PORT) )

