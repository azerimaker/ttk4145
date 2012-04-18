__author__ = 'kiro'

#this class holds the elevators for this instance and all the work for all elevators.

# this class does nothing on others, but many do something on this.

class DataStore():

    def __init__(self):
        self.elevatorList = []
        self.workQueue = []

    def newElevator(self):
        self.elevatorList.append("elevator")
        print "adds a new elevator to the list of elevators. this is necessary for sending delegating work later. "

    def newWork(self, work):
        self.workQueue.append(work)

        # to be removed.
        self.workQueue.append("F01D04")
        print "adds a new job to the work list."

    def getWork(self):
        return self.workQueue