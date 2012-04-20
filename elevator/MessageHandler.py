import pickle

__author__ = 'kiro'

class MessageHandler():

    def __init__(self, controller=""):
        self.controller = controller

        print "MessageHandler initialized"

    def setController(self, controller):
        self.controller = controller

    def evaluateCommand(self, ip, port, messageStr):
        message = pickle.loads(messageStr)

        if message.type == "newOrder":
            self.controller.newOrder(message)
            print "newOrder"
        elif message.type == "orderComplete":
            self.controller.orderComplete(message)
            print "orderComplete"
        elif message.type == "updateOrders":
            self.controller.updateOrders(message)
            print "updateOrders"
        elif message.type == "updateStatus":
            self.controller.updateStaturs(message)
            print "updateStatus"



