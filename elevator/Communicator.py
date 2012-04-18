from Sender import Sender
from Reciever import Receiver

__author__ = 'kiro'

class Communicator():

    elevators = []

    def __init__(self, messageHandler, dataStore):

        # my ip is the ip of this computer.
        # 5005 is the standard port for communication.
        self.receiver = Receiver("78.91.5.168", 5005, messageHandler)
        self.receiver.start()

        self.sender = Sender("78.91.5.168", "")

        self.dataStore = dataStore

    def send(self, elevator, message):
        sender = Sender(elevator.IP, elevator.Port)
        sender.send(message)

    def sendToAll(self, message):
        for elevator in self.dataStore.getElevators():
            self.send(elevator, message)


# test code for this class.
#main = Main()
#m = messageHandler(main)
#com = Communicator(m)
#com.send()
