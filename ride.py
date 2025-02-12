### Ride Class for every ride the cab drives
import time
class Ride():
    def __init__(self) -> None:
        self.startTime = time.time()
        self.endTime : time.time = None
        self.driveMeter = 0
        self.waitMeter = 0
        self.Fare : float = 0.00
        self.waitcost = waitfee
        self.drivecost = drivefee
    def start(self,t : time.time):
        self.startTime = t
    def stop(self,t: time.time):
        self.stopTime = t
