class Dispatcher:

DOWN = 0
UP = 1
    def __init__(self):
        self.job_list = [[0 for x in range(NO_FLOORS)] for x in range(2)] # direction is one dimension, no. floors the other
        self.peers = {} # store peer objects, with IP as key and peer-object as value      
        self.dispatcher = True
        self.networking = ""

    def run():
        # TODO:
    
    
    '''        
    check to see if other elevators have problems
    if an elevator has timed out, delete from list
    '''
    def check_others():
        # TODO: if peer is obstructed, wait to see if cleared, if not cleared within set time, redistribute orders
        currentTime = time()
        for peer_id, peer in peers.iteritems():
            if (currentTime - peer.last_alive) < TIMEOUT:
                continue
            else:
                del peers[peer.id]
                if peer.dispatcher:
                    new_dispatcher()
    
    
    '''
    Finds the elevator best suited for a job
    '''     
    def find_best_suited(job):
        best_score = -1
        best_suited = ""
        for peer_id, peer in peers.iteritems():
            if peer.is_obstructed or peer.is_stopped:
                continue
            else:
                score = get_score(peer, job)
                if score < best_score:
                    best_score = score
                    best_suited = peer
        if best_score = 0:
            add_to_backlog(job)
                    
        return best_suited
    
    ''' 
    Gives elevator a score based on how suited it is for the job.
    A score of 1 is best 
    '''
    def get_score(peer, job):
        # TODO: FIGURE OUT HOW BEST TO GIVE A SCORE! THIS IS PROBABLY THE WORST PART LOGIC-WISE!
        score = 0.0
        scaling_factor = 1/NO_FLOORS
        
        # current distance from job
        distance = 0
        if peer.direction == UP and job.floor > peer.floor:
            distance = job.floor - peer.floor
        elif peer.direction == UP and job.floor < peer.floor:
            distance = 0
        elif peer.direction == DOWN and job.floor > peer.floor:
            distance = 0
        elif peer.direction == DOWN and job.floor < peer.floor:
            distance = peer.floor - job.floor
        
        # number of jobs waiting
        no_jobs = 0
        for direction in range(2):
            for floor in range(NO_FLOORS):
                if job_list[direction][floor] == peer.id:
                    no_jobs++
        
        score = distance + no_jobs
        if score == 0:
            return 1
        else:
            return score
        
    '''
    This method takes a dead elevator and redistributes its jobs
    to the other elevators that are still online
    '''
    def redistribute_jobs(peer):
        # TODO: takes in a dead peer, redistributes its jobs to the ones still online
        for direction in range(2):
            for floor in range(NO_FLOORS):
                if job_list[direction][floor] == peer.id:
                    job = Job(direction, floor)
                    dispatch_job(job)
        
    
    '''
    Takes a job and finds an elevator to give it to
    When job list is updated, broadcast to all
    '''    
    def dispatch_job(job):
        if not job_list[job.direction][job.floor]:
            peer = find_best_suited(job)
            network.send_job(peer, job)
        
    
    def start(networking):
        self.networking = networking
        
        
        
