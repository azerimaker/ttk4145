import threading
from time import sleep
from Communicator import Communicator
from DataStore import DataStore
from Controller import Controller
from Elevator import Elevator
from MessageHandler import MessageHandler

__author__ = 'kiro'

# to be the top most file, where we call everything else from.
class Main():

    def __init__(self):
        self.controller = Controller()
        self.messageHandler = MessageHandler(self, self.controller)
        self.communicator = Communicator(self.messageHandler, self.dataStore)
        
        print "MAIN initialize"

        ## test code.
        print "--------------"
        print "start testing"
        sleep(2)
        self.communicator.broadcast("testing, hei hei")
        self.communicator.broadcast("testing11, hei hei")
        self.communicator.broadcast("testing2222, hei hei")
        e = Elevator()
        self.communicator.sendToElevator(e, "message testings over tcp")

    def setManagerState(self, state):
        self.managerState = state

    def setDispatcher(self):
        self.controller.setIsDispatcher(True)
        print "we are now the manager, Wohoo!"

