import unittest
import sys
sys.path.append("../")

from FileRepo import FileRepo
from Point import Point
import random

class Test_FileRepo(unittest.TestCase):

    def setUp(self) -> None:
        self.csvData = "posX; posY; timestamp\n"
        for i in range(10) :
            randomValue = random.randint(0,100)
            self.csvData += f"{randomValue}; {randomValue}; {i}\n"

        self.point =[Point(1,0),Point(9,0),Point(1,4),Point(6,0)]
        self.temps=[0,1,2,3]

    def tearDown(self):
        pass

    def test_save_is_file_created(self) :
        """Check if a file is created correctly"""
        FileRepo.save(self.csvData, True) # calling save method in debug mode -> creating a file called debug.csv
        # An error pops out if the file is not createdgit c

    def test_save_is_file_content_correct(self) :
        FileRepo.save(self.csvData, True) # creating file to test

        """Check if file contains the same data than what was given"""
        file = open("debug.csv", "r") # open file 
        lines = self.csvData.split('\n')# get list of original data
        fileLines = [line.replace("\n", "") for line in file]  # get lines of file data
        for i in range(len(lines)-1) :
            self.assertTrue(lines[i] == fileLines[i]) # check that every line is equal to original data
            #print(lines[i], "\n",  fileLines[i], "\n") # debug line
        
        # check if each line of the file is equal to each line of csvData
            #self.assertTrue(line)

    def test_transformDataToCsv(self) :
        expectedResult = "posX;posY;timestamp\n1;0;0\n9;0;1\n1;4;2\n6;0;3\n" # define in this variable the expected result
        obtainResult = FileRepo.transformDataToCsv(self.point,self.temps) #define in this variable the return of the tested function
        self.assertTrue(expectedResult == obtainResult) # Assert that the expected result is the same that the result of the tested function
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

    tfr = Test_FileRepo()
    tfr.setUp()
    tfr.test_save()
    tfr.test_transformDataToCsv()
    
    