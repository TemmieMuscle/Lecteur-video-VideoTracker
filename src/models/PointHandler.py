import numpy as np
from . import Point
from .Video import Video
import math

class PointHandler:
    def __init__(self, view):
        self.view = view

        self.tabPoint=[] #tableau de sous tableaux de la forme [[posX,posY, index],...,[posX,posY, index]]
        self.tabScale = [] # tableau des points utilisés pour l'échelle
        self.scale = 1 / 100  # définit l'échelle des points, ici, 100 pixel = 1m -> a utiliser comme un scalaire : k pixels -> k*scale metres

    # prend en argument un tableau de la forme [index,Point(posX,posY)] en tabOfEvent
    # Parcoure le tableau self.tabPoint pour voir si l'index donnée dans tabofEvent existe deja dans self.tabPointw
    # si il existe, remplace les anciennes coordonnées liées à cet index par les nouvelles
    # si il n'existe pas, append le contenu de tabofEvent dans self.tabPoint
    def addPoint(self,tabOfEvent):
        index = tabOfEvent[2]
        x = round(tabOfEvent[0], 3)
        y = round(tabOfEvent[1], 3)
        for i in range(len(self.tabPoint)):
            if self.tabPoint[i][1]==index:
                self.tabPoint[i][1]=Point(x,y)
                #print(self.tabPoint[index-1][0].getY())
                return
            
        self.tabPoint.append([Point(x,y), index])
        #print(self.tabPoint[index-1][0].getY())
        self.tabPoint=sorted(self.tabPoint, key=lambda numero: numero[1]) # trie self.tabPoint en fonction de l'indice 0 des tableaux qui le compose (soit par leur index)

    # same as above but puts the points in tabScale and checks if tab is full
    def addScalePoint(self, tabOfEvent) :
        x = tabOfEvent[0]
        y = tabOfEvent[1]

        self.tabScale.append(Point(x,y))
        if len(self.tabScale) >= 2 :
            self.setScale(self.tabScale[0], self.tabScale[1]) # calls setscale with
            self.tabScale = []

    # rénitialise le tableau en le rendant vide
    def cleanTab(self):
        self.tabPoint=[]
        self.view.DIALOG_TABPOINTCLEARED()

    # define scale of pixels to meter
    def setScale(self, point1, point2) :
        x1, y1 = point1.getX(), point1.getY()
        x2, y2 = point2.getX(), point2.getY()

        pixelLength = int(math.dist([x1,y1], [x2,y2])) # get distance between points clicked by user

        realLength = 0
        while realLength <= 0 :
            answer = self.view.DIALOG_SETSCALE()
            if answer==None:
                return
            else:
                realLength=answer
        self.scale = realLength / pixelLength # set self.scale to updated scale
        

    # créer le graphe et l'affiche avec matplotlib
    def printGraph(self, fps): # could possibly go into view
        if len(self.tabPoint) < 2: # Exits if not enough data created by user
            self.view.DIALOG_NOTENOUGHPOINTS()
            return

        # Data for plotting
        timeValues = []
        xValues = []
        yValues = []
        for i in range(len(self.tabPoint)) :
            xValues.append(self.tabPoint[i][0].getX()*self.scale) # x in meters ######### ROUND TO 3 WHEN FORMATTING
            yValues.append(self.tabPoint[i][0].getY()*self.scale) # y in meters
            timeValues.append(self.tabPoint[i][1] / int(fps)) # time in seconds
        #print(xValues, yValues, timeValues)

        answer = self.view.DIALOG_SEPARATEDWINDOWS()
        if answer is None:
            #print("User canceled action")
            pass
        elif answer == True:
            self.view.showSeparatedGraphs(xValues, yValues, timeValues)
        else :
            self.view.showGraphs(xValues, yValues, timeValues)

    def showTable(self):
        timeValues = ["Temps en secondes"] # Mise en forme du tableau
        xValues = ["Position horizontale en mètres"] 
        yValues = ["Position verticale en mètres"]

        if len(self.tabPoint) == 0:
            self.view.DIALOG_NODATA()
            return

        for i in range(len(self.tabPoint)) :
            xValues.append(self.tabPoint[i][0].getX()*self.scale) # x in meters
            yValues.append(self.tabPoint[i][0].getY()*self.scale) # y in meter
            timeValues.append(self.tabPoint[i][1] ) # time in frame
        #print(xValues, yValues, timeValues)

        self.view.showTable(xValues, yValues, timeValues)
    
