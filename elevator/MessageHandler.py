from time import sleep
from Elevator import Elevator
import re

__author__ = 'kiro'

class MessageHandler():

    def __init__(self, controller=""):
        self.controller = controller

        print "MessageHandler initialized"

    def setController(self, controller):
        self.controller = controller

    def evaluateCommand(self, ip, port, command):
        ## MESSAGES

        # message format
        # "dispatcher" + "elevator" + "direction" + "floor"
        #pattern= re.compile("[TF]"+"[0-9][0-9]"+"[UD]"+"[0-9][0-9]")

        #broad cast to everyone
        helloWorld = re.compile("HelloWorld")

        # broadcast to all
        newOrder = re.compile("newOrder")

        # broadcast to everyone.
        stillAlive = re.compile("StillAlive")

        # broadcast to everyone.
        jobComplete = re.compile("")

        # broadcast to everyone.
        obstructed = re.compile("")

        # broadcast to everyone.
        elevatorState = re.compile("")

        # broadcast to everyone
        newManager = re.compile("")

        # receive from manager elevator
        workOrder = re.compile("")

        ## end MESSAGES

        print "----------------"
        print "message sorting"
        # command sorter.
        if re.match(helloWorld, command):
            # new elevator in the network
            e = Elevator(ip, port, command[0], False, )
            self.controller.getDataStore().addElevator(e)
        #
        elif re.match(newOrder, command):
            self.controller.newWork(newOrder, ip)
            print newOrder
        #
        elif re.match(stillAlive, command):
            print "Alive"
        #
        elif re.match(jobComplete, command):
            self.controller.dataStore.workComplete(command)
        #
        elif re.match(obstructed, command):
            if self.controller.isDispatcher:
                print "manager is obstructed"
            print command
        #
        elif re.match(elevatorState, command):
            self.controller.setElevatorState(elevatorState, ip)

            # if you do not get a reply from the manager in 3 seconds, the oldest elevator still responding takes over.
            if command[0] == "T":
                print "MANAGER STATE"

            print elevatorState
        #
        elif re.match(newManager, command):
            self.controller.setManager(newManager)
        #
        elif re.match(workOrder, command):
            self.controller.doWork(command)
            print workOrder
        #
        else:
            print "Command not valid! - " + ip + ":" + str(port) + " com: " + command
        #
        print command