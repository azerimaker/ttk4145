__author__ = 'kiro'

#this class holds the elevators for this instance and all the work for all elevators.

# this class does nothing on others, but many do something on this.

class DataStore():

    def __init__(self):

        self.elevatorList = []
        self.workTable = [][]

    def newElevator(self):
        self.elevatorList.append("elevator")
        print "adds a new elevator to the list of elevators. this is necessary for sending delegating work later. "

    def newWork(self, work, elevator):
        print "figure out the nicities of this"
        direction = "U/D"
        floor = "1-4"
        self.workTable[direction][floor] = elevator

    def getWork(self):
        return self.workTable

    def getElevators(self):
        return self.elevatorList