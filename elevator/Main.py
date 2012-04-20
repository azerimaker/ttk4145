from time import sleep
from Communicator import Communicator
from Controller import Controller
from Message import Message
from MessageHandler import MessageHandler
from Peer import Peer

__author__ = 'kiro'

# to be the top most file, where we call everything else from.
class Main():

    def __init__(self):

        self.controller = Controller()
        self.messageHandler = MessageHandler(self.controller)
        self.communicator = Communicator(self.messageHandler)


        print "MAIN initialize"



        ## test code.
        print "--------------"
        sleep(2)
        print "testing start"

        peer = Peer()
        message = Message()
        self.controller.communicator.sendToOne(peer, message)

        print "testing complete"
        print "--------------"
        exit()

Main()