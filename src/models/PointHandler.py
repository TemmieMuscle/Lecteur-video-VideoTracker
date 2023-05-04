import matplotlib.pyplot as plt
import numpy as np
from . import Point
from tkinter import messagebox as mb

class PointHandler():
    def __init__(self):
        self.tabPoint=[] #tableau de sous tableaux de la forme [[index,posX,posY],...,[index,posX,posY]]
        pass

    # prend en argument un tableau de la forme [index,posX,posY] en tabOfEvent
    # Parcoure le tableau self.tabPoint pour voir si l'index donnée dans tabofEvent existe deja dans self.tabPoint
    # si il existe, remplace les anciennes coordonnées liées à cet index par les nouvelles
    # si il n'existe pas, append tabofEvent dans self.tabPoint
    def addPoint(self,tabOfEvent):
        for i in range(len(self.tabPoint)):
            if self.tabPoint[i][0]==tabOfEvent[0]:
                self.tabPoint[i]=tabOfEvent
                print(self.tabPoint)
                return
        self.tabPoint.append(tabOfEvent)
        self.tabPoint=sorted(self.tabPoint, key=lambda numero: numero[0]) # trie self.tabPoint en fonction de l'indice 0 des tableaux qui le compose (soit par leur index)
        print(self.tabPoint)

    # rénitialise le tableau en le rendant vide
    def cleanTab(self):
        self.tabPoint=[]

    # créer le graphe et l'affiche avec matplotlib
    def printGraphe(self):

        ####################################
        import random as rd
        def randomPoints(n:int) -> list: # creates and returns a list of 10 random points for testing
            l = []
            for i in range(n) : # Creating n random points
                tempPoint = Point(rd.randint(0,100), rd.randint(0,100))
                l.append(tempPoint)
            return l
        
        pointList = randomPoints(10)
        timeList = [i for i in range(10)]
        fake_tabPoint = [[pointList[i], timeList[i]] for i in range(10)] ## [[Point(x,y), frame],[Point(x,y), frame],[Point(x,y), frame],etc ...]

        #print(fake_tabPoint)
        ################################""""""""#"""

        # Data for plotting
        xValues, yValues, timeValues = [], [], []
        for i in range(10) :
            xValues.append(fake_tabPoint[i][0].getX())
            yValues.append(fake_tabPoint[i][0].getY())
            timeValues.append(fake_tabPoint[i][1])
        #print(xValues, yValues, timeValues)

        answer = mb.askyesnocancel("Question", "Voulez-vous les graphiques dans des fenêtres séparées ?")

        if answer is None:
            print("User canceled action")
        elif answer == True:
            fig, ax1 = plt.subplots()
            ax1.plot(timeValues, xValues)
            ax1.set(xlabel='t', ylabel='x',title='x(t)')
            ax1.grid()

            fig, ax2 = plt.subplots()
            ax2.plot(timeValues, yValues)
            ax2.set(xlabel='t', ylabel='y',title='y(t)')
            ax2.grid()

            fig, ax3 = plt.subplots()
            ax3.plot(xValues, yValues)
            ax3.set(xlabel='x', ylabel='y',title='y(x)')
            ax3.grid()

            plt.show()
        else :
            fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

            ax1.plot(timeValues, xValues)
            ax1.set(xlabel='t', ylabel='x',title='x(t)')
            ax1.grid()

            ax2.plot(timeValues, yValues)
            ax2.set(xlabel='t', ylabel='y',title='y(t)')
            ax2.grid()

            ax3.plot(xValues, yValues)
            ax3.set(xlabel='x', ylabel='y',title='y(x)')
            ax3.grid()

            plt.tight_layout()
            plt.show()

    def getTab(self):
        return self.tabPoint
    
