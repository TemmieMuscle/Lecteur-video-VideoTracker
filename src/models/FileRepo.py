# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog as fd

class FileRepo : 
    def __init__(self) :
        pass
        
    def transformDataToCsv(points, time) :
        csvString = "posX;posY;timestamp\n" # adding names to variables to follow / needed for csv
        for i in range(len(time)) : # adding line for each point / like posX;posY;timestamp
            csvString += f"{points[i].getX()};{points[i].getY()};{time[i]}\n" 
        return csvString
    
    def save(csvData) :
        file = fd.asksaveasfile(mode='w', defaultextension=".csv")
        if file == None : # if canceled by user
            return
        
        file.write(csvData) # writing formatted data to new file
        file.close()
        
    def getFile() :
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