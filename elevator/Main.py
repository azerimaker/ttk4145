__author__ = 'kiro'

# to be the top most file, where we call everything else from.

class Main():

    # see if there is still a manager

    def setManagerState(self, state):
        self.managerState = state

    # thread
        # if self.state[0] != "T":
            # communicator.send("T-----")
            # createManager()

    def createManager(self):
        print "we are now the manager, Wohoo!"