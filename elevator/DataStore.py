__author__ = 'kiro'

#this class holds the elevators for this instance and all the work for all elevators.

# this class does nothing on others, but many do something on this.

class DataStore():

    def __init__(self):

        self.elevatorList = []
        self.workTable = [][]

    def newElevator(self, elevator):
        self.elevatorList.append(elevator)
        print "adds a new elevator to the list of elevators. this is necessary for sending delegating work later. "

    def newWork(self, work, ip):

        print "figure out the necessities of this"
        elevator = self.getElevator(ip)
        direction = "U/D"
        floor = "1-4"
        self.workTable[direction][floor] = elevator

    def getWork(self):
        return self.workTable

    def getElevatorList(self):
        return self.elevatorList

    def getElevator(self, ip):
        for e in self.elevatorList:
            if e.IP == ip:
                return e

    #