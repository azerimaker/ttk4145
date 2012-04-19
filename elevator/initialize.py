GLOBAL_JOB_LIST = {}    # dictionary to hold the list of all jobs
MY_JOB_LIST = {}        # dictionary to hold this elevators jobs

'''
Initializes the elevator, broadcasts it's existence on 
the network, and starts the elevator control program
'''
def main():
    networking = Network()
    messages = networking.init()
    if len(messages) == 0:  # no other elevators, this one becomes dispatcher
        dispatcher = Dispatcher()
        dispatcher.start(networking)
    else:
        controller = Control()
        controller.setup(messages, networking)
    
'''
Notifies all online elevators that a new one has
come online
'''    
def broadcast():
    # TODO: broadcast "I'm here" on network
    control.listen() # listen for other elevators
    
    
  
    
