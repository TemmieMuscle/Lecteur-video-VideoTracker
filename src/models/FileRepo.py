# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog as fd

class FileRepo : 
    def __init__(self, view) :
        self.view = view
        
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
        if filename :
            return filename
        else :
            return None
    
    def save_data(self, tabPoints) : ### BEWARE -> x and y are in PIXELS AND timestamp is in FRAME
        if len(tabPoints) < 1 :
            self.view.DIALOG_NODATA()
            return
        
        pointList = []
        timeList = []
        for i in range(len(tabPoints)) :
            pointList.append(tabPoints[i][0])
            timeList.append(tabPoints[i][1])

        data = self.transformDataToCsv(pointList, timeList) # converting data to csv
        self.save(data, False)
        print("Data saved !")