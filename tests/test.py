# -*- coding: utf-8 -*-

### IMPORTS ###
from random import *
import model.Point as pt # PATH OUTDATED
import model.FileRepo as fr # PATH OUTDATED 


### FUNCTIONS ###
def randomPoints(n:int) -> list: # creates and returns a list of 10 random points for testing
    l = []
    for i in range(n) : # Creating n random points
        tempPoint = pt.Point(randint(0,100), randint(0,100))
        l.append(tempPoint)
    return l
  
    
### MAIN ###
def main() :
    pointList = randomPoints(10)
    timeList = [i for i in range(10)]

    data = fr.FileRepo.transformDataToCsv(pointList, timeList) # converting data to csv
    fr.FileRepo.save(data) # saving data
    
    print("Un fichier csv comportant les données de 10 points aléatoires a été crée.")
       
if __name__ == "__main__" :
    main()
  
    

    
