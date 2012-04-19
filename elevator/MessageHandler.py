from Elevator import Elevator

__author__ = 'kiro'

class MessageHandler():

    def __init__(self, main, controller):
        self.main = main
        self.controller = controller

        print "MessageHandler initialized"

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
            # new elevator in the network
            e = Elevator(ip, port, command[0], False, )
            self.controller.addElevator(e)
        elif command == newOrder:
            self.controller.newWork(newOrder, ip)
            print newOrder
        elif command == stillAlive:
            # if you do not get a reply from the manager in 3 seconds, the oldest elevator still responding takes over.
            if state[0] == "T":
                self.main.setManagerState()
            e = self.controller.getElevator(ip)
            e.setStatus(command)
        elif command == jobDone:
            self.controller.workDone(command)
        elif command == obstructed:
            if self.main.isManager:
                print "manager is obstructed"
            print command
        elif command == elevatorState:
            self.controller.setElevatorState(elevatorState, ip)
            print elevatorState
        elif command == newManager:
            self.controller.setManager(newManager)
        elif command == workOrder:
            self.controller.doWork(workOrder)
            print workOrder
        else:
            print "Command not valid! - " + ip + ":" + str(port) + " com: " + command