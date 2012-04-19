import time

__author__ = 'kiro'

class Elevator():

    def __init__(self, ip="127.0.0.1", port=5005, state="F------", manager=False):
        self.IP = ip
        self.PORT = port
        self.state = state
        self.MANAGER = manager
        # time of last message from this elevator
        self.lastAlive = time.gmtime()
        #initialization time of this elevator.
        self.age = time.gmtime() # has to be changed.

    def setState(self, state):
        self.state = state

        #TODO: this has to be checked for validity.
        # sets the time to now
        self.lastAlive = time.gmtime()
