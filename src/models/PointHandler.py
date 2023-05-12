import numpy as np
from . import Point
from .Video import Video
import math

class PointHandler:
    def __init__(self, view):
        self.view = view

        self.tabPoint=[] #tableau de sous tableaux de la forme [[index,Point(posX,posY)] ...]
        self.tabScale = [] # tableau des points utilisés pour l'échelle
        self.scale = 1 / 100  # définit l'échelle des points, ici, 100 pixel = 1m -> a utiliser comme un scalaire : k pixels -> k*scale metres
        self.orthonormalPoint = Point(0,0) # coordonnée du repere orthonomal

    # prend en argument un tableau de la forme [index,Point(posX,posY)] en tabOfEvent
    # Parcoure le tableau self.tabPoint pour voir si l'index donnée dans tabofEvent existe deja dans self.tabPointw
    # si il existe, remplace les anciennes coordonnées liées à cet index par les nouvelles
    # si il n'existe pas, append le contenu de tabofEvent dans self.tabPoint
    def addPoint(self,tabOfEvent):
        index = tabOfEvent[2]
        x = round(tabOfEvent[0], 3)
        y = round(tabOfEvent[1], 3)
        for i in range(len(self.tabPoint)): # if point already in tab replace it
            if self.tabPoint[i][1]==index:
                self.tabPoint[i][0]=Point(x,y)
                #print(self.tabPoint[index-1][0].getY())
                return
            
        self.tabPoint.append([Point(x,y), index])
        #print(self.tabPoint[index-1][0].getY())
        #print(self.tabPoint)
        self.tabPoint=sorted(self.tabPoint, key=lambda n: n[1]) # trie self.tabPoint en fonction de l'indice 1 des tableaux qui le compose (soit par leur index)

    # same as above but puts the points in tabScale and checks if tab is full
    def addScalePoint(self, tabOfEvent) :
        x = tabOfEvent[0]
        y = tabOfEvent[1]

        self.tabScale.append(Point(x,y))
        if len(self.tabScale) >= 2 :
            self.setScale(self.tabScale[0], self.tabScale[1]) # calls setscale with
            self.tabScale = []

    # function who set the orthonormal point to new coordinate in arguments
    def setOrthonormalPoint(self,tabOrtho):
        self.orthonormalPoint = Point(tabOrtho[0],tabOrtho[1])

    # function who return the self.tabPoint formatted with the orthonormal and the scale
    def getTabFormattedPoint(self,event=None):
        formattedArray = [] # array of array who contain formatted point coordinates and frame
        for array in self.tabPoint: # adding each content of self.tabPoint in formattedArray, then format x and y with scale and orthonormal
            formattedPoint=Point((array[0].getX()-self.orthonormalPoint.getX())*self.scale,(array[0].getY()-self.orthonormalPoint.getY())*self.scale)
            formattedArray.append([formattedPoint,array[1]])
        return formattedArray

    # rénitialise le tableau en le rendant vide
    def cleanTab(self):
        self.tabPoint=[]
        self.orthonormalPoint=Point(0,0)
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
        formattedArrayOfPoint = self.getTabFormattedPoint() # get the array of formated coordinate
        timeValues = []
        xValues = []
        yValues = []
        for i in range(len(formattedArrayOfPoint)) : # append every point/frame of formattedArrayOfPoint in xValues, yValues and timeValues
            xValues.append(formattedArrayOfPoint[i][0].getX())
            yValues.append(formattedArrayOfPoint[i][0].getY())
            timeValues.append(formattedArrayOfPoint[i][1] / int(fps)) # time in seconds
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
        formattedArrayOfPoint=self.getTabFormattedPoint()
        timeValues = ["Temps en secondes"] # Mise en forme du tableau
        xValues = ["Position horizontale en mètres"] 
        yValues = ["Position verticale en mètres"]

        if len(formattedArrayOfPoint) == 0:
            self.view.DIALOG_NODATA()
            return

        for i in range(len(formattedArrayOfPoint)) : # append every point/frame of formattedArrayOfPoint in xValues, yValues and timeValues
            xValues.append(formattedArrayOfPoint[i][0].getX())
            yValues.append(formattedArrayOfPoint[i][0].getY())
            timeValues.append(formattedArrayOfPoint[i][1]) # number of the frame
        #print(xValues, yValues, timeValues)

        self.view.showTable(xValues, yValues, timeValues)
    
