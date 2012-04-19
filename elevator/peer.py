class Peer:

    def __init__(self, IP, status, manager, last_alive, age):
        self.id = IP
        self.status = status
        self.manager = manager
        self.last_alive = last_alive
        self.age = age
        self.is_obstructed = False
        self.is_stopped = False
        
    
    def send_message(message):
        # TODO:spawn thread to open ports and send message
        
        
