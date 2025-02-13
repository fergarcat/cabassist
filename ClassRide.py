### Ride Class for every ride the cab drives
import time
class Ride:
    def __init__(self) -> None:
        self.startTime = time.time()
        self.endTime : time.time = None
        self.driveMeter = 0
        self.waitMeter = 0
        self.Fare : float = 0.00
        self.waitcost = 0
        self.drivecost = 0
    def start(self,t : time.time):
        self.startTime = t
    def stop(self,t: time.time):
        self.stopTime = t
    def reset(self,waitfee,drivefee):
        self.startTime = time.time()
        self.endTime = None
        self.driveMeter = 0
        self.waitMeter = 0
        self.Fare = 0.00
        self.waitcost = waitfee
        self.drivecost = drivefee
