import matplotlib.pyplot as plt
import numpy as np
from . import Point

class PointHandler():
    def __init__(self):
        self.tabPoint=[]
        pass

    def addPoint(self):
        pass

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
    
