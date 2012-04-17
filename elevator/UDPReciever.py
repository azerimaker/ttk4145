import socket
import threading

__author__ = 'kiro'

class UDPReceiver( threading.Thread ):
    UDP_IP="127.0.0.1"
    UDP_PORT=5005

    def __init__(self, ip):
        super(UDPReceiver, self).__init__()
        if ip == "":
            self.UDP_IP = "127.0.0.1"
        else:
            self.UDP_IP = ip
        print "RECEIVER initialized"
        print "UDP target IP:", self.UDP_IP
        print "UDP target port:", self.UDP_PORT

    def run(self):

        sock = socket.socket( socket.AF_INET, # Internet
            socket.SOCK_DGRAM ) # UDP
        sock.bind( (self.UDP_IP,self.UDP_PORT) )

        while True:
            print "receiving"
            data, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes
            if data[0]=="5":
                print "number 5"
            print "received message:", data
