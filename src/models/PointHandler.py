import matplotlib.pyplot as plt
import numpy as np
from . import Point

class PointHandler():
    def __init__(self):
        self.tabPoint=[] #tableau de sous tableaux de la forme [[index,posX,posY],...,[index,posX,posY]]
        pass

    # prend en argument un tableau de la forme [index,posX,posY] en tabOfEvent
    # Parcoure le tableau self.tabPoint pour voir si l'index donnée dans tabofEvent existe deja dans self.tabPoint
    # si il existe, remplace les anciennes coordonnées liées à cet index par les nouvelles
    # si il n'existe pas, append le contenu de tabofEvent dans self.tabPoint
    def addPoint(self,tabOfEvent):
        for i in range(len(self.tabPoint)):
            if self.tabPoint[i][0]==tabOfEvent[0]:
                self.tabPoint[i][1]=Point(tabOfEvent[1],tabOfEvent[2])
                print(self.tabPoint[tabOfEvent[0]-1][1].getY())
                return
        self.tabPoint.append([tabOfEvent[0],Point(tabOfEvent[1],tabOfEvent[2])])
        print(self.tabPoint[tabOfEvent[0]-1][1].getY())
        self.tabPoint=sorted(self.tabPoint, key=lambda numero: numero[0]) # trie self.tabPoint en fonction de l'indice 0 des tableaux qui le compose (soit par leur index)

    # rénitialise le tableau en le rendant vide
    def cleanTab(self):
        self.tabPoint=[]

    # créer le graphe et l'affiche avec matplotlib
    def printGraphe():

        # Data for plotting
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='time (s)', ylabel='voltage (mV)',
            title='About as simple as it gets, folks')
        ax.grid()

        fig.savefig("test.png")
        plt.show()

    def getTab(self):
        return self.tabPoint
    
