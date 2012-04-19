from TCPSender import TCPSender
from TCPReciever import TCPReceiver
from UDPReceiver import UDPReceiver

__author__ = 'kiro'

class Communicator():

    elevators = []

    def __init__(self, messageHandler, dataStore):

        # the tcp listener, that handles incoming connections on tcp.
        self.TCPReceiver = TCPReceiver("78.91.5.168", 5005, messageHandler)
        self.TCPReceiver.start()

        # the udp listener that gets broadcasting messages.
        self.UDPReceiver = UDPReceiver(5005, messageHandler)
        self.UDPReceiver.start()

        # the tcp and udp senders.
        self.TCPSender = TCPSender("78.91.5.168", "")
        self.UDPSender = TCPSender(5005)

        # the DataStore that contains the elevators and the work list.
        self.dataStore = dataStore

    # sends a message to one specific elevator.
    def sendToElevator(self, elevator, message):
        sender = TCPSender(elevator.IP, elevator.Port)
        sender.send(message)

    # Sends messages to all the elevators registered in this instance.
    def sendToAllElevators(self, message):
        for elevator in self.dataStore.getElevators():
            self.sendToElevator(elevator, message)

    # broadcasts messages on UDP, do not expect that It will arrive.
    def broadcast(self, message):
        self.UDPSender.send(message)


# test code for this class.
#main = Main()
#m = messageHandler(main)
#com = Communicator(m)
#com.send()
