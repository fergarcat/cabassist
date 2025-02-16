import unittest
import time
from ClassRide import Ride

class TestRide(unittest.TestCase):

    def setUp(self):
        self.ride = Ride()

    def test_initialization(self):
        self.assertIsInstance(self.ride.startTime, float)
        self.assertIsNone(self.ride.endTime)
        self.assertEqual(self.ride.driveMeter, 0)
        self.assertEqual(self.ride.waitMeter, 0)
        self.assertEqual(self.ride.Fare, 0.00)
        self.assertEqual(self.ride.waitcost, 0)
        self.assertEqual(self.ride.drivecost, 0)

    def test_start(self):
        t = time.time()
        self.ride.start(t)
        self.assertEqual(self.ride.startTime, t)

    def test_stop(self):
        t = time.time()
        self.ride.stop(t)
        self.assertEqual(self.ride.stopTime, t)

    def test_reset(self):
        waitfee = 0.02
        drivefee = 0.05
        self.ride.reset(waitfee, drivefee)
        self.assertIsInstance(self.ride.startTime, float)
        self.assertIsNone(self.ride.endTime)
        self.assertEqual(self.ride.driveMeter, 0)
        self.assertEqual(self.ride.waitMeter, 0)
        self.assertEqual(self.ride.Fare, 0.00)
        self.assertEqual(self.ride.waitcost, waitfee)
        self.assertEqual(self.ride.drivecost, drivefee)

if __name__ == '__main__':
    unittest.main()