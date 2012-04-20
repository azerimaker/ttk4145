from time import sleep
from Controller_old import Controller
from Message import Message
from MessageHandler import MessageHandler
from Peer import Peer

__author__ = 'kiro'

# to be the top most file, where we call everything else from.
class Main():

    def __init__(self):

        self.messageHandler = MessageHandler()
        self.controller = Controller(self.messageHandler)
        self.messageHandler.setController(self.controller)

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