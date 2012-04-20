GLOBAL_JOB_LIST = {}    # dictionary to hold the list of all jobs
MY_JOB_LIST = {}        # dictionary to hold this elevators jobs

from control import Control
from Message import Message

'''
Initializes the elevator, broadcasts it's existence on 
the network, and starts the elevator control program
'''
def main():
#    networking = Network()
#    messages = networking.init()
    messages = []
    messages.append(Message("78.91.23.11", "OBSTRUCTED", False))
    messages.append(Message("78.91.23.10", "RUNNING", True))
    networking = "haha"
    controller = ""
    if len(messages) == 0:  # no other elevators, this one becomes dispatcher
        controller = Control("78.91.23.9", "RUNNING", True)
    else:
        controller = Control("78.91.23.9", "RUNNING", False)
    controller.setup(messages)
    
'''
Notifies all online elevators that a new one has
come online
'''    
def broadcast():
    # TODO: broadcast "I'm here" on network
    control.listen() # listen for other elevators
    
    
  
    
