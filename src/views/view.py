import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import ttk

class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Video Tracker")  
        parent.geometry("1100x500")
        parent['bg'] = 'gray'
        parent.minsize(1100,400)
        self.parent=parent

        leStyle = ttk.Style(parent)
        leStyle.theme_use("clam")
        leStyle.configure("TButton",font=('',12))
        leStyle.configure("TLabel",font=('Tekton Pro',12))

        """Définition des menus"""
        menuBarre = tk.Menu(self.parent)
        laFonte=("Tekton Pro",11)

        self.fileMenu=tk.Menu(menuBarre, tearoff=0) # labels are indexed in fileMenu (to be used with entry config in controller)
        self.fileMenu.add_command(label="Charger Vidéo",font=laFonte) #0
        self.fileMenu.add_command(label="Lire Vidéo",font=laFonte)#1
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exporter CSV",font=laFonte)#3
        self.fileMenu.add_command(label="Quitter",font=laFonte)#4
        menuBarre.add_cascade(label="File",menu=self.fileMenu,font=laFonte)
    
        self.viewMenu=tk.Menu(menuBarre, tearoff=0)
        self.viewMenu.add_command(label="Afficher Graphes",font=laFonte)
        menuBarre.add_cascade(label="View",menu=self.viewMenu,font=laFonte)

        self.editMenu=tk.Menu(menuBarre, tearoff=0)
        self.editMenu.add_command(label="Mode édition",font=laFonte)
        self.editMenu.add_command(label="Tableau Valeurs",font=laFonte)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Définir Echelle X",font=laFonte)
        self.editMenu.add_command(label="Définir Echelle Y",font=laFonte)
        menuBarre.add_cascade(label="Edit",menu=self.editMenu,font=laFonte)

        self.parent.config(menu=menuBarre)


        """Définition du widget qui contiendra les images"""
        self.cadreMilieu=tk.Canvas(self.parent)

        self.cadreMilieu.create_text((150,50),text="Chargez une vidéo pour commencer")
        self.cadreMilieu.pack()


        """Définition des widget boutons et label liés aux vidéos, contenu dans un widget frame"""
        cadreBas=ttk.Frame(self.parent,width=30)

        self.frameActuelle_lbl = ttk.Label(cadreBas,width=20)
        self.frameActuelle_lbl.pack(padx=15,pady=25,side="left")
        self.frameActuelle_lbl.config(text = "")

        self.next_btn = ttk.Button(cadreBas, text ='⏩')
        self.next_btn.pack(side='right',padx=5, pady=20)  
        self.back_btn = ttk.Button(cadreBas, text ='⏪')
        self.back_btn.pack(side='right',padx=5, pady=20)  

        self.espace = ttk.Label(cadreBas)
        self.espace.pack(padx=10,pady=5,side="right")

        self.skipForward_btn = ttk.Button(cadreBas, text ='⏭')
        self.skipForward_btn.pack(side='right',padx=5, pady=20)
        self.skipBackward_btn = ttk.Button(cadreBas, text ='⏮')
        self.skipBackward_btn.pack(side='right',padx=5, pady=20)

        self.play_btn = ttk.Button(cadreBas, text ='⏵')
        self.play_btn.pack(side='right',padx=40, pady=20)

           
        cadreBas.pack(side='bottom',fill="x")

    def setController(self, controller):
        self.controller = controller