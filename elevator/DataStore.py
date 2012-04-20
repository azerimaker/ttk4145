from Elevator import Elevator

__author__ = 'kiro'

#this class holds the elevators for this instance and all the work for all elevators.

# this class does nothing on others, but many do something on this.

class DataStore():

    def __init__(self):
        self.elevatorList = []
        self.workTable = [[],[]]

        print "DataStore Initialized"

    def addPeer(self, peer):
        self.elevatorList.append(peer)
        print "adds a new elevator to the list of elevators. this is necessary for delegating work later. "

    def newWork(self, work, ip):
        # TODO add work to the correct lists.
        print "adding new work to global list"
        elevator = self.getElevator(ip)
        direction = "U/D"
        floor = "1-4"
        self.workTable[[direction],[floor]] = elevator

    def getWork(self):
        return self.workTable

    def workComplete(self, command):
        # TODO remove work from correct list.
        print "removing work from global"

    def getElevatorList(self):
        return self.elevatorList

    def getElevator(self, ip):
        for e in self.elevatorList:
            if e.IP == ip:
                return e

    def setElevatorState(self, state, ip):
        e = self.getElevator(ip)
        if not e:
            if state[0] == "T":
                e = Elevator(ip, 5005, state, True)
            else:
                e = Elevator(ip, 5005, state,)

