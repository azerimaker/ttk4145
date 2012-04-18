from time import sleep
from UDPSender import UDPSender
from UDPReciever import UDPReceiver

__author__ = 'kiro'

class Communicator():

    receiver = UDPReceiver
    elevators = []

    def __init__(self, messageHandler):

        # my ip is the ip of this computer.
        # 5005 is the standard port for communication.
        self.receiver = UDPReceiver("my ip", 5000, messageHandler)
        self.receiver.run()

        sender = UDPSender("78.91.5.168")

    def addElevator(self, elevator):
        self.elevators.append(elevator)

    def send(self):



    for i in range(1, 10):
        sender.send("test"+str(i))
        sleep(1)
