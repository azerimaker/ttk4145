__author__ = 'kiro'

class Elevator():

    def __init__(self, ip="127.0.0.1", port=5005, status="F", manager=False, lastAlive=""):
        self.IP = ip
        self.PORT = port
        self.status = status
        self.manager = manager
        # time of last message from this elevator
        self.lastAlive =lastAlive
        #initialization time of this elevator.
        self.age = 0 # has to be changed.
