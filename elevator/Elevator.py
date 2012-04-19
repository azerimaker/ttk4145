import time

__author__ = 'kiro'

class Elevator():

    def __init__(self, ip="127.0.0.1", port=5005, status="F", manager=False):
        self.IP = ip
        self.PORT = port
        self.status = status
        self.MANAGER = manager
        # time of last message from this elevator
        self.lastAlive = time.gmtime()
        #initialization time of this elevator.
        self.age = time.gmtime() # has to be changed.

    def setStatus(self, status):
        self.status = status

        #TODO: this has to be checked for validity.
        # sets the time to now
        self.lastAlive = time.gmtime()
