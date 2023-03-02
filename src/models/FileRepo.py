# -*- coding: utf-8 -*-

class FileRepo : 
    def __init__(self) :
        pass
        
    def transformDataToCsv(points, time) :
        csvString = "posX;posY;timestamp\n" # adding names to variables to follow / needed for csv
        for i in range(len(time)) : # adding line for each point / like posX;posY;timestamp
            csvString += f"{points[i].getX()};{points[i].getY()};{time[i]}\n" 
        return csvString
    
    def save(csvData) :
        file = open("output.csv", "w")
        file.write(csvData) # writing formatted data to new file
        file.close()
        
    