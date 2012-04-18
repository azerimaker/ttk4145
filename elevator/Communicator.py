from time import sleep
from Sender import UDPSender
from Reciever import UDPReceiver
from messageHandler import messageHandler

__author__ = 'kiro'

class Communicator():

    elevators = []

    def __init__(self, messageHandler):

        # my ip is the ip of this computer.
        # 5005 is the standard port for communication.
        self.receiver = UDPReceiver("78.91.23.120", 5005, messageHandler)
        self.receiver.start()

        self.sender = UDPSender("78.91.5.168", "")

    def addElevator(self, elevator):
        self.elevators.append(elevator)

    def send(self):
        for i in range(1, 10):

            self.sender.send("test"+str(i))
            sleep(1)

# test code for this class.
m = messageHandler()
com = Communicator(m)
com.send()
