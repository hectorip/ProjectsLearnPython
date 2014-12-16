import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import TimerClasses

class TimerTest(unittest.TestCase):
    def setUp(self):
        self.timer = TimerClasses.Timer(video='http://vimeo.com/93003441')

    def testClassExists(self):
        self.assertEquals('Timer', self.timer.__class__.__name__)

    def testHasCorrectURL(self):
        self.assertEquals('http://vimeo.com/93003441', self.timer.video)

    def testTimeIs2Hours(self):
        self.assertEquals(7200,self.timer.time)
if __name__ == '__main__':
    unittest.main()