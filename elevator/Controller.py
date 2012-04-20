import threading
from time import sleep
from Communicator import Communicator
from DataStore import DataStore

__author__ = 'kiro'

# the file that manages jobs from the job queue, and dispatches them to the other elevators.


# thread that gets now jobs from the DataStore and directs them to the right elevator.

class Controller():

    def __init__(self, messageHandler):

        self.dataStore = DataStore()
        self.communicator = Communicator(messageHandler, self)
        self.isDispatcher = False
        self.lastState = "F-----"

        print "Controller Initialization"

        #run the checking thread to see if there is a dispatcher.
        isDispatcherCheck(self).start()

    def getDataStore(self):
        return self.dataStore

    def newOrder(self):
        print "new Order, not impl"

    def doWork(self, order):
        print order

    def setElevatorState(self, state, ip):
        self.dataStore.setElevatorState(state,ip)

    def setDispatcher(self, ip):
        self.dispatcher = ip

    def setIsDispatcher(self, bool):
        self.isDispatcher = bool

    def getIsDispatcher(self):
        return self.isDispatcher

# thread for checking the manager status.
class isDispatcherCheck( threading.Thread ):
    def __init__(self, controller):
        super(isDispatcherCheck, self).__init__()
        self.controller = controller

    def run(self):
        sleep(5)
        while True:
            print "Checking manager status"
            if self.controller.lastState[0]!="T" and not self.controller.getIsDispatcher():
                self.controller.setIsDispatcher(True)
                print "I'm the dispatcher"
            sleep(3)