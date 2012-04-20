from time import sleep
from Controller import Controller
from Elevator import Elevator
from MessageHandler import MessageHandler

__author__ = 'kiro'

# to be the top most file, where we call everything else from.
class Main():

    def __init__(self):
        self.messageHandler = MessageHandler()
        self.controller = Controller(self.messageHandler)
        self.messageHandler.setController(self.controller)

        print "MAIN initialize"

        ## test code.
        print "--------------"
        print "start testing"
        sleep(2)
        self.controller.communicator.broadcast("testing, hei hei")
        self.controller.communicator.broadcast("testing11, hei hei")
        self.controller.communicator.broadcast("testing2222, hei hei")
        e = Elevator()
        self.controller.communicator.sendToElevator(e, "message testings over tcp")
        self.controller.communicator.sendToElevator(e, "T01D05")


