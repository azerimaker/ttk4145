class Peer:

    def __init__(self, IP, status, dispatcher, last_alive):
        self.id = IP
        self.status = status
        self.dispatcher = dispatcher
        self.last_alive = last_alive
        self.is_obstructed = False
        self.is_stopped = False
        
    
    def send_message(message):
        # TODO:spawn thread to open ports and send message
        return null
        
        
