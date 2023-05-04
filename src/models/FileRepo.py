# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog as fd

class FileRepo : 
    def __init__(self) :
        pass
        
    def transformDataToCsv(self,points,time) :
        csvString = "posX;posY;timestamp\n" # adding names to variables to follow / needed for csv
        for i in range(len(time)) : # adding line for each point / like posX;posY;timestamp
            csvString += f"{points[i].getX()};{points[i].getY()};{time[i]}\n" 
        return csvString
    
    def save(self,csvData, debug) : # this method has to have a debug argument or it messes up the tests
        #print(f"Debug = {debug}")
        if debug == True : # this line only activates when triggered by the test script
            file = open("debug.csv", "w") # it avoid using tkinter during testing phases
        elif debug == False :
            file = fd.asksaveasfile(mode='w', defaultextension=".csv")
            if file == None : # if canceled by user
                return
        
        file.write(csvData) # writing formatted data to new file
        file.close()
        
    def getFile(self) : # gets path of wanted file by using a file dialog
        filetypes = (
        ('MP4 files', '*.mp4'),
        ('WAV files', '*.wav'),
        ('MOV files', '*.mov'),
        ('AVI files', '*.avi'),
        ('FLV files', '*.flv'),
        ('WEBM files', '*.webm'))

        filename = fd.askopenfilename(title='Choose the video',filetypes=filetypes)
        if filename == None : # if canceled by user
            return

        return filename
    
    #########################################################################################
    def save_data(self) : ######## TO BE DISCONTINUED mais on verra quand on fera les points etc.
        import random as rd
        from . import Point

        fr = FileRepo()

        def randomPoints(n:int) -> list: # creates and returns a list of 10 random points for testing
            l = []
            for i in range(n) : # Creating n random points
                tempPoint = Point(rd.randint(0,100), rd.randint(0,100))
                l.append(tempPoint)
            return l
        
        pointList = randomPoints(10)
        timeList = [i for i in range(10)]

        data = fr.transformDataToCsv(pointList, timeList) # converting data to csv
        fr.save(data, False)
        print("Data saved !")
    #########################################################################################
