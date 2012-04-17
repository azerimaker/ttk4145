GLOBAL_GOING_UP = set()     # set to hold list of all jobs up
GLOBAL_GOING_DOWN = set()   # set to hold list of all jobs down
GOING_UP = set()            # set to hold this elevators jobs going up
GOING_DOWN = set()          # set to hold this elevators jobs going down
CURRENT_JOBS = set()        # set to hold this elevators current jobs
DIRECTION = 'UP'            # U or D; direction elevator is moving
CURRENT_FLOOR = 3           # elevators current floor and direction
STOP_NEXT = False           # should elevator stop on next floor?

'''
Dictionary to hold the list of all other elevators
key = elevator no.
value = time of last still-alive-signal
example entry: 'elevator1': '18:31:37'
'''
ELEVATORS = {}
                        
from time import time


# go through job list to see if any available jobs in same direction
# as the elevator is headed, if so, add them to current job list
def get_jobs():
    if DIRECTION == 'UP':
        for job in GOING_UP:
            if job >= current_floor:
                CURRENT_JOBS.add(job)                 
    elif DIRECTION == 'DOWN':
        for job in GOING_DOWN:
            if job <= current_floor:
                CURRENT_JOBS.add(job)         

# when passing a floor, check if there are people waiting on the next floor
# if there are, raise flag so the elevator stops when reaching the floor
def check_next_floor():
    if CURRENT_FLOOR+1 in CURRENT_JOBS:
        STOP_NEXT = True
        
# check to see if other elevators have problems
def check_others:
    for key, value in ELEVATORS:
        currentTime = time()
        if (currentTime - value) < 3:
            continue
        else:
            # elevator[key] is dead! DO SOMETHING!
            # add the dead elevators job list to private list
            # send private list to other elevators
            
    

    
