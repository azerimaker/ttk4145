__author__ = 'kiro'

# the file that manages jobs from the job queue, and dispatches them to the other elevators.


# thread that gets now jobs from the DataStore and directs them to the right elevator.

class Manager():
    def __init__(self):
        print "Manager Initialization \n"