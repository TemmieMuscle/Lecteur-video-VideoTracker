import unittest
import sys
import os

path = os.getcwd()  
sys.path.insert(0, path)

from src.models.Point import Point
import random

class Test_Point(unittest.TestCase):

    def setUp(self) -> None:
        # creer instance de Point
        self.randomX = random.randint(0,100)
        self.randomY = random.randint(0,100)
        self.unPoint = Point(self.randomX,self.randomY)

    def tearDown(self):
        pass

    def test_getX(self):
        """Test if X data is correct"""
        self.assertTrue(self.randomX == self.unPoint.getX())

    def test_getY(self):
        """Test if X data is correct"""
        self.assertTrue(self.randomY == self.unPoint.getY())

if __name__ == '__main__':
    unittest.main(verbosity=2)

    tfr = Test_Point()
    tfr.setUp()
    tfr.test_getX()
    tfr.test_getY()

    
    