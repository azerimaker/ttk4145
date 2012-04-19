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
import constants


class Control:

    '''
    Initialize the control object
    '''
    def __init__(self):
        self.job_list = [[0 for x in range(NO_FLOORS)] for x in range(2)] # direction is one dimension, no. floors the other
        self.peers = {} # store peer objects, with IP as key       
        self.dispatcher = False
        self.networking = "" 
        self.age = time()

    '''
    setup elevator to be ready
    '''
    def setup(messages, networking):
        self.networking = networking
        networking.do_stuff()
        # spawn networking thread
        # this thread sets up all the necessary connections
        # and listens for incoming messages for a set time period
        for message in messages:
            last_alive = time()
            peers[message.id] = Peer(message.id, message.status, message.dispatcher, last_alive, message.age)
        networking.set_peers(peers) # give networking thread the list of peers so that it can update them
        networking.broadcast_existence()
        start()
           
    
    '''
    when passing a floor, check if there are people waiting on the next floor
    if there are, raise flag so the elevator stops when reaching the floor
    '''
    def check_next_floor():
        if CURRENT_FLOOR+1 in CURRENT_JOBS:
            STOP_NEXT = True
   
    '''        
    check to see if other elevators have problems
    if an elevator has timed out, delete from list
    '''
    def check_others():
        currentTime = time()
        for peer_id, peer in peers.iteritems():
            if (currentTime - peer.last_alive) < TIMEOUT:
                continue
            else:
                del peers[peer.id]
                if peer.dispatcher:
                    new_dispatcher()
                
    '''
    listen for other elevators
    add these to system overview
    '''            
    def listen():
        # TODO: networking class takes care of this
        

    '''
    Method to decide which elevator becomes dispatcher
    if dispatcher has died. Oldest elevator is dispatcher
    '''
    def new_dispatcher():
        elder = self
        for peer_id, peer in peers.iteritems():
            if peer.age > elder.age:
                elder = peer
        if elder == self:
            become_dispatcher()

    
    '''
    Turns this elevator into dispatcher
    '''
    def become_dispatcher():
        dispatcher = Dispatcher()
        # TODO: set relevant datafields in dispatcher object
        # TODO: stop control loop, give control to dispatcher
        
    
    
    '''
    Start the elevator
    '''
    def start():
        
