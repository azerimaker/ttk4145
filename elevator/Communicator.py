from TCPSender import TCPSender
from TCPReciever import TCPReceiver

__author__ = 'kiro'

class Communicator():

    elevators = []

    def __init__(self, messageHandler, dataStore):

        # my ip is the ip of this computer.
        # 5005 is the standard port for communication.
        self.receiver = TCPReceiver("78.91.5.168", 5005, messageHandler)
        self.receiver.start()

        self.sender = TCPSender("78.91.5.168", "")

        self.dataStore = dataStore

    def send(self, elevator, message):
        sender = TCPSender(elevator.IP, elevator.Port)
        sender.send(message)

    def sendToAll(self, message):
        for elevator in self.dataStore.getElevators():
            self.send(elevator, message)

    def broadcast(self):
        print "broadcasting to TCP/IP"


# test code for this class.
#main = Main()
#m = messageHandler(main)
#com = Communicator(m)
#com.send()
