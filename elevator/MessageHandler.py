__author__ = 'kiro'

class messageHandler():

    def __init__(self, main):
        self.main = main

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
        if command == state:
            if state[0] == "T":
                self.main.setManagerState()
        elif command == request:
            print command
        elif command == work:
            print command
        elif command == complete:
            print command
        elif command == alive:
            print command
        else:
            print "Command not valid! - " + ip + ":" + str(port) + " com: " + command