from Elevator import Elevator

__author__ = 'kiro'

class messageHandler():

    def __init__(self, main, dataStore):
        self.main = main
        self.dataStore = dataStore

    def evaluateCommand(self, ip, port, command):
        ## MESSAGES

        # message format
        # "elevator" + "direction" + "floor"
        # "[1-9][1-9]" + "[UD]" + "[1-9][1-9]"

        #broad cast to everyone
        helloWorld = ""

        # broadcast to all
        newOrder = ""

        # broadcast to everyone.
        stillAlive = ""

        # broadcast to everyone.
        jobDone = ""

        # broadcast to everyone.
        obstructed = ""

        # broadcast to everyone.
        elevatorState = ""

        # broadcast to everyone
        newManager = ""

        # receive from manager elevator
        workOrder = ""

        ## end MESSAGES

        # command sorter.
        if command == helloWorld:
            e = Elevator(ip, port, command[0], False, )
            self.dataStore.newElevator(e)
        elif command == newOrder:
            self.dataStore.newWork(newOrder, ip)
            print newOrder
        elif command == stillAlive:
            # if you do not get a reply from the manager in 3 seconds, the oldest elevator still responding takes over.
            if state[0] == "T":
                self.main.setManagerState()
            e = self.dataStore.getElevator(ip)
            e.setStatus(command)
        elif command == jobDone:
            print jobDone
        elif command == obstructed:
            print command
        elif command == elevatorState:
            print elevatorState
        elif command == newManager:
            print newManager
        elif command == workOrder:
            print workOrder
        else:
            print "Command not valid! - " + ip + ":" + str(port) + " com: " + command