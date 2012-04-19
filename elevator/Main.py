import threading
from Communicator import Communicator
from DataStore import DataStore
from Manager import Manager
from MessageHandler import MessageHandler

__author__ = 'kiro'

# to be the top most file, where we call everything else from.
class Main():

    def __init__(self):
        #self.manager = Manager()
        self.dataStore = DataStore()
        self.messageHandler = MessageHandler(self, self.dataStore)
        self.communicator = Communicator(self.messageHandler, self.dataStore)
        #self.elevatorControl = ElevatorControl()

        self.isManager = False

        self.communicator.broadcast("testing, hei hei")


        # see if there is still a manager
        isManagerCheck(self).start()

    def setManagerState(self, state):
        self.managerState = state

    def createManager(self):
        self.manager = Manager()
        self.isManager = True
        print "we are now the manager, Wohoo!"


# thread for checking the manager status.
class isManagerCheck( threading.Thread ):
    def __init__(self, main):
        super(isManagerCheck, self).__init__()
        self.main = main

    def run(self):
        print "Checking manager status\n"
        if not self.main.isManager:
            self.main.createManager()