import unittest
import sys
sys.path.append("../")
from ..src.models.FileRepo import FileRepo

class Test_liste(unittest.TestCase):

    def setUp(self) -> None:
        self.csvData = "posX; posY; timestamp\n11;12;0\n21;22;1\n31;32;2"

    def tearDown(self):
        pass

    def test_save(self) :
        """Check if a file is created correctly"""
        FileRepo.save(self.csvData, True) # calling save method in debug mode

    def test_transformDataToCsv(self) :
        pass         ## léonard

    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    