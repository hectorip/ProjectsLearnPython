import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import TimerClasses

class TimerTest(unittest.TestCase):
    def setUp(self):
        self.timer = TimerClasses.Timer()

    def testClassExists(self):
        self.assertEquals('Timer', self.timer.__class__.__name__)

if __name__ == '__main__':
    unittest.main()