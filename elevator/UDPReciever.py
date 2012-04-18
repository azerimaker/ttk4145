import socket
import threading
from time import sleep

__author__ = 'kiro'

class UDPReceiver( threading.Thread ):
    UDP_IP="127.0.0.1"
    UDP_PORT=5005

    def __init__(self, ip, port, messageHandler):
        # initialize the thread.
        super(UDPReceiver, self).__init__()

        # Set the ip to default or given value.
        if ip=="":
            self.UDP_IP = "127.0.0.1"
        else:
            self.UDP_IP = ip

        # Set the port to default or given value.
        if not port:
            self.UDP_PORT = 5005
        else:
            self.UDP_PORT = port

        self.messageHandler = messageHandler

        print "RECEIVER initialized"
        print "UDP target IP:", self.UDP_IP
        print "UDP target port:", self.UDP_PORT

    def run(self):

        sock = socket.socket( socket.AF_INET, # Internet
            socket.SOCK_DGRAM ) # UDP
        sock.bind( (self.UDP_IP,self.UDP_PORT) )

        while True:
            data, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes
            print "received message:", data
            # messageHandler.evaluateCommand(data)
            sleep(1)


# test code for running only this file.
#a = UDPReceiver("78.91.5.168")
#a.receive()