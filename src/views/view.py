import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import ttk

class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Video Tracker")  
        self.parent=parent
        

        """Définition des menus"""
        menuBarre = tk.Menu(self.parent)

        self.fileMenu=tk.Menu(menuBarre, tearoff=0) # labels are indexed in fileMenu (to be used with entry config in controller)
        self.fileMenu.add_command(label="Charger Vidéo") #0
        self.fileMenu.add_command(label="Lire Vidéo")#1
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exporter CSV")#3
        self.fileMenu.add_command(label="Quitter")#4
        menuBarre.add_cascade(label="File",menu=self.fileMenu)
    
        viewMenu=tk.Menu(menuBarre, tearoff=0)
        viewMenu.add_command(label="Afficher Graphes")
        menuBarre.add_cascade(label="View",menu=viewMenu)

        editMenu=tk.Menu(menuBarre, tearoff=0)
        editMenu.add_command(label="Tableau Valeurs")
        editMenu.add_separator()
        editMenu.add_command(label="Définir Echelle X")
        editMenu.add_command(label="Définir Echelle Y")
        menuBarre.add_cascade(label="Edit",menu=editMenu)

        self.parent.config(menu=menuBarre)


        """Définition du widget qui contiendra les images"""
        self.cadreMilieu=tk.Canvas(self.parent)
        self.cadreMilieu.create_text((100,50),text="Chargez une vidéo pour commencer") #### bien positioner
        self.cadreMilieu.pack()


        """Définition des widget boutons et label liés aux vidéos, contenu dans un widget frame"""
        cadreBas=tk.Frame(self.parent)

        self.frameActuelle_lbl = tk.Label(cadreBas,font = ('Arial', 15))
        self.frameActuelle_lbl.pack(padx=15,pady=25,side="left")
        self.frameActuelle_lbl.config(text = "Frame actuelle sur frame max")

        self.play_btn = tk.Button(cadreBas, text ='⏵',font = ('Arial', 15))
        self.play_btn.pack(side='left',padx=40, pady=20)

        self.skipBackward_btn = tk.Button(cadreBas, text ='⏮',font = ('Arial', 15))
        self.skipBackward_btn.pack(side='left',padx=5, pady=20)
        self.skipForward_btn = tk.Button(cadreBas, text ='⏭',font = ('Arial', 15))
        self.skipForward_btn.pack(side='left',padx=5, pady=20)

        self.espace = tk.Label(cadreBas,font = ('Arial', 15))
        self.espace.pack(padx=20,pady=5,side="left")

        self.back_btn = tk.Button(cadreBas, text ='⏪',font = ('Arial', 15))
        self.back_btn.pack(side='left',padx=5, pady=20)
        self.next_btn = tk.Button(cadreBas, text ='⏩',font = ('Arial', 15))
        self.next_btn.pack(side='left',padx=5, pady=20)       
        cadreBas.pack(side='bottom',fill="x")

    def setController(self, controller):
        self.controller = controller