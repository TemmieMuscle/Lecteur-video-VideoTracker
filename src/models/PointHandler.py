import matplotlib.pyplot as plt
import numpy as np
from . import Point
from .Video import Video
from tkinter import messagebox as mb

class PointHandler:
    def __init__(self):
        self.tabPoint=[] #tableau de sous tableaux de la forme [[posX,posY, index],...,[posX,posY, index]]

    # prend en argument un tableau de la forme [index,Point(posX,posY)] en tabOfEvent
    # Parcoure le tableau self.tabPoint pour voir si l'index donnée dans tabofEvent existe deja dans self.tabPoint
    # si il existe, remplace les anciennes coordonnées liées à cet index par les nouvelles
    # si il n'existe pas, append le contenu de tabofEvent dans self.tabPoint
    def addPoint(self,tabOfEvent):
        index = tabOfEvent[2]
        x = tabOfEvent[0]
        y = tabOfEvent[1]
        for i in range(len(self.tabPoint)):
            if self.tabPoint[i][1]==index:
                self.tabPoint[i][1]=Point(x,y)
                #print(self.tabPoint[index-1][0].getY())
                return
            
        self.tabPoint.append([Point(x,y), index])
        #print(self.tabPoint[index-1][0].getY())
        self.tabPoint=sorted(self.tabPoint, key=lambda numero: numero[1]) # trie self.tabPoint en fonction de l'indice 0 des tableaux qui le compose (soit par leur index)

    # rénitialise le tableau en le rendant vide
    def cleanTab(self):
        self.tabPoint=[]

    # créer le graphe et l'affiche avec matplotlib
    def printGraph(self, fps):
        if len(self.tabPoint) < 2: # Exits if not enough data created by user
            mb.showerror("Erreur", "Aucune donnée disponible. Avez vous au moins crée deux points ?")
            return

        # Data for plotting
        timeValues = []
        xValues = []
        yValues = []
        for i in range(len(self.tabPoint)) :
            xValues.append(self.tabPoint[i][0].getX())
            yValues.append(self.tabPoint[i][0].getY())
            timeValues.append(self.tabPoint[i][1] / fps) # time in seconds
        #print(xValues, yValues, timeValues)

        answer = mb.askyesnocancel("Choix décisif", "Voulez-vous les graphiques dans des fenêtres séparées ?")

        if answer is None:
            print("User canceled action")
        elif answer == True:
            fig, ax1 = plt.subplots()
            ax1.plot(timeValues, xValues)
            ax1.set(xlabel='Temps (en s)', ylabel='Position horizontale (en m)',title='x(t)')
            ax1.grid()

            fig, ax2 = plt.subplots()
            ax2.plot(timeValues, yValues)
            ax2.set(xlabel='Temps (en s)', ylabel='Position verticale (en m)',title='y(t)')
            ax2.grid()

            fig, ax3 = plt.subplots()
            ax3.plot(xValues, yValues)
            ax3.set(xlabel='Position horizontale (en m)', ylabel='Position verticale (en m)',title='y(x)')
            ax3.grid()

            plt.show()
        else :
            fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

            ax1.plot(timeValues, xValues)
            ax1.set(xlabel='Temps (en s)', ylabel='Position horizontale (en m)',title='x(t)')
            ax1.grid()

            ax2.plot(timeValues, yValues)
            ax2.set(xlabel='Temps (en s)', ylabel='Position verticale (en m)',title='y(t)')
            ax2.grid()

            ax3.plot(xValues, yValues)
            ax3.set(xlabel='Position horizontale (en m)', ylabel='Position verticale (en m)',title='y(x)')
            ax3.grid()

            plt.tight_layout()
            plt.show()

    def getTab(self):
        return self.tabPoint
    
