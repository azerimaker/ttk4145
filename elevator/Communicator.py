from UDPSender import UDPSender
from UDPReciever import UDPReceiver
import threading

__author__ = 'kiro'


receiver = UDPReceiver("")
sender = UDPSender("")

receiver.run()

sender.send("test")
sender.send("hei hei")