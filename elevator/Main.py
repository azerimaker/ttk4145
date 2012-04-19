import threading
from Manager import Manager

__author__ = 'kiro'

# to be the top most file, where we call everything else from.

class Main():
    #self.Manager
    #sself.Communicator
    #self.DataStore
    #self.MessageHandler
    #self.ElevatorControl

    def __init__(self):
        self.managerState = "F"

        # see if there is still a manager
        isManagerCheck(self).start()

    def setManagerState(self, state):
        self.managerState = state

    def createManager(self):
        self.manager = Manager()
        print "we are now the manager, Wohoo!"


# thread for checking the manager status.
class isManagerCheck( threading.Thread ):
    def __init__(self, main):
        super(isManagerCheck, self).__init__()
        self.main = main

    def run(self):
        print "checking manager status"
        if self.main.managerState[0]!="T":
            self.main.createManager()