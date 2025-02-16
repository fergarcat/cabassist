import unittest
from ClassTimer import Timer
import time

class TestTimer(unittest.TestCase):

    def setUp(self):
        self.timer = Timer()

    def test_initialization(self):
        self.assertIsInstance(self.timer.start, float)

    def test_restart(self):
        old_start = self.timer.start
        time.sleep(0.1)
        self.timer.restart()
        new_start = self.timer.start
        self.assertNotEqual(old_start, new_start)
        self.assertGreater(new_start, old_start)

    def test_get_time(self):
        time.sleep(0.1)
        elapsed_time = self.timer.get_time()
        self.assertGreater(elapsed_time, 0.1)
        self.assertLess(elapsed_time, 0.2)

if __name__ == '__main__':
    unittest.main()