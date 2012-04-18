__author__ = 'kiro'

class messageHandler():

    def __init__(self, main):
        self.main = main

    def evaluateCommand(self, ip, port, command):
        ## MESSAGES

        com = "elevator" + "direction" + "floor"
        regex = "[1-9][1-9]" + "[UD]" + "[1-9][1-9]"

        newJob = ""
        state = "" # I'm alive message
        # if state == "------" this elevator is

        helloWorld = ""
        doWork = ""

        state    = "01D01"
        request  = "--U03"
        work     = "01U02"
        complete = "03---"
        alive    = "00---"
        newManager = ""

        # # ! MESSAGES

        # command sorter.
        if command == state:
            if state[0] == True:
                self.main.setManagerState()
            print command
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