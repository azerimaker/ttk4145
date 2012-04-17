GLOBAL_JOB_LIST = {}    # dictionary to hold the list of all jobs
MY_JOB_LIST = {}        # dictionary to hold this elevators jobs

'''
Initializes the elevator, broadcasts it's existence on 
the network, and starts the elevator control program
'''
def main():
    initalize_datastructures()
    broadcast()
    control.start() # elevator is now ready to run
    
'''
Notifies all online elevators that a new one has
come online
'''    
def broadcast():
    # TODO: broadcast "I'm here" on network
    control.listen() # listen for other elevators
    
def initialize_datastructure():
    # these are in a file of their own
    # so perhaps no need for this method?
    
  
    
