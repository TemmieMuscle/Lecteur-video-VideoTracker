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

        fileMenu=tk.Menu(menuBarre, tearoff=0)
        fileMenu.add_command(label="Charger Vidéo")
        fileMenu.add_command(label="Lire Vidéo")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exporter CSV")
        menuBarre.add_cascade(label="File",menu=fileMenu)
    
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
        cadreMilieu=tk.Canvas(self.parent)
        cadreMilieu.create_text((100,50),text="Canvas qui contiendra l'image")
        cadreMilieu.pack()


        """Définition des widget boutons et label liés aux vidéos, contenu dans un widget frame"""
        cadreBas=tk.Frame(self.parent)

        self.temperature_lbl = tk.Label(cadreBas,font = ('Arial', 25))
        self.temperature_lbl.pack(padx=50,pady=20,side="left")
        self.temperature_lbl.config(text = "Frame actuelle sur frame max")

        self.play_btn = tk.Button(cadreBas, text ='⏵',font = ('Arial', 25))
        self.play_btn.pack(side='left',padx=40, pady=20)

        self.skipBackward_btn = tk.Button(cadreBas, text ='⏮',font = ('Arial', 25))
        self.skipBackward_btn.pack(side='left',padx=5, pady=20)
        self.skipForward_btn = tk.Button(cadreBas, text ='⏭',font = ('Arial', 25))
        self.skipForward_btn.pack(side='left',padx=5, pady=20)

        self.espace = tk.Label(cadreBas,font = ('Arial', 25))
        self.espace.pack(padx=20,pady=5,side="left")

        self.back_btn = tk.Button(cadreBas, text ='⏪',font = ('Arial', 25))
        self.back_btn.pack(side='left',padx=5, pady=20)
        self.next_btn = tk.Button(cadreBas, text ='⏩',font = ('Arial', 25))
        self.next_btn.pack(side='left',padx=5, pady=20)       
        cadreBas.pack(side='bottom',fill="x")

    def setController(self, controller):
        self.controller = controller