import PIL.Image, PIL.ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import matplotlib.pyplot as plt

class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Video Tracker")  
        parent.geometry("1100x500")
        parent['bg'] = 'gray'
        parent.minsize(1100,400)
        self.parent=parent

        # Style options
        leStyle = ttk.Style(parent)
        leStyle.theme_use("clam")
        leStyle.configure("TButton",font=('',12))
        leStyle.configure("TLabel",font=('Tekton Pro',12))

        """Définition des menus"""
        menuBarre = tk.Menu(self.parent)
        laFonte=("Tekton Pro",11)

        self.fileMenu=tk.Menu(menuBarre, tearoff=0) # labels are indexed in fileMenu (to be used with entry config in controller)
        self.fileMenu.add_command(label="Charger une vidéo",font=laFonte) #0
        self.fileMenu.add_command(label="Lire une vidéo",font=laFonte)#1
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exporter en CSV",font=laFonte)#3
        self.fileMenu.add_command(label="Quitter",font=laFonte)#4
        menuBarre.add_cascade(label="File",menu=self.fileMenu,font=laFonte)
    
        self.viewMenu=tk.Menu(menuBarre, tearoff=0)
        self.viewMenu.add_command(label="Afficher les graphes",font=laFonte)
        menuBarre.add_cascade(label="View",menu=self.viewMenu,font=laFonte)

        self.editMenu=tk.Menu(menuBarre, tearoff=0)
        self.editMenu.add_command(label="Mode édition",font=laFonte)
        self.editMenu.add_command(label="Tableau de points",font=laFonte)
        self.editMenu.add_command(label="Effacer les points",font=laFonte)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Aide",font=laFonte)
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
        self.next_btn.pack(side='right',padx=10, pady=20)  
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


    ### ALL DIALOGS WINDOWS FOR MODELS AND CONTROLLER
    # FILEREPO
    def DIALOG_NODATA(self) :
        mb.showerror("Erreur", "Aucune donnée disponible. Avez vous au moins crée un point ?")

    # POINTHANDLER
    def DIALOG_SETSCALE(self) :
        return sd.askfloat("Définition de l'échelle", "Quelle est la distance séparant les 2 points ? (en mètres)")
    
    def DIALOG_NOTENOUGHPOINTS(self) :
        mb.showerror("Erreur", "Aucune donnée disponible. Avez vous au moins crée deux points ?")

    def DIALOG_SEPARATEDWINDOWS(self) :
        return mb.askyesnocancel("Choix décisif", "Voulez-vous les graphiques dans des fenêtres séparées ?")
    
    def DIALOG_TABPOINTCLEARED(self) :
        mb.showinfo("Information","Les points ont été éffacés")
    
    # CONTROLLER
    def DIALOG_EDITIONMODE(self) :
        return mb.askokcancel("Mode édition", "Vous pouvez maintenant ajouter des points sur la vidéo en cliquant dessus.\nAppuyez sur échap pour quitter ce mode.")

    def DIALOG_HASQUITEDITION(self) :
        mb.showinfo("Information","Vous avez quitté le mode édition.")
 
    def DIALOG_WANTPOINTSCLEARED(self) :
        return mb.askyesnocancel("Choix décisif", "Voulez vous effacer les points crées ?")
    
    def DIALOG_OTHONORMALSET(self) :
        mb.showinfo("Information","Un nouvel origine du repère à été crée.")

    def DIALOG_HELP(self) :
        mb.showinfo("Aide","""Commandes spéciales :
- Effectuer un clic gauche pour ajouter des points (uniquement en mode édition)
- Effectuer deux clics droit pour pouvoir définir une échelle
- Effectuer un clic molette pour définir l'origine de l'axe
- Ctrl+O pour charger une vidéo
- Ctrl+Q pour lire une vidéo
        """)
    ### POINT HANDLER RELATED
    def showSeparatedGraphs(self, xValues, yValues, timeValues) :
        fig, ax1 = plt.subplots()
        ax1.plot(timeValues, xValues)
        ax1.set(xlabel='Temps (en s)', ylabel='Position horizontale (en m)',title='Position horizontale en fonction du temps')
        ax1.grid()

        fig, ax2 = plt.subplots()
        ax2.plot(timeValues, yValues)
        ax2.set(xlabel='Temps (en s)', ylabel='Position verticale (en m)',title='Position verticale en fonction du temps')
        ax2.grid()

        fig, ax3 = plt.subplots()
        ax3.plot(xValues, yValues)
        ax3.set(xlabel='Position horizontale (en m)', ylabel='Position verticale (en m)',title='Position verticale en fonction de la position horizontale')
        ax3.grid()

        plt.show()

    def showGraphs(self, xValues, yValues, timeValues) :
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

        ax1.plot(timeValues, xValues)
        ax1.set(xlabel='Temps (en s)', ylabel='Position horizontale (en m)',title='Position horizontale en fonction du temps')
        ax1.grid()

        ax2.plot(timeValues, yValues)
        ax2.set(xlabel='Temps (en s)', ylabel='Position verticale (en m)',title='Position verticale en fonction du temps')
        ax2.grid()

        ax3.plot(xValues, yValues)
        ax3.set(xlabel='Position horizontale (en m)', ylabel='Position verticale (en m)',title='Position verticale en fonction de la position horizontale')
        ax3.grid()

        ax4.axis('off')

        plt.tight_layout()
        plt.show()

    def showTable(self, xValues, yValues, timeValues) :
 
        class Table:
            def __init__(self,root):
                # setup table
                for i in range(len(xValues)): 
                    for j in range(3):
                        self.e = tk.Entry(root, width=30,font=('Arial',16))
                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, lst[i][j])
        
        # input data into table
        lst = [(xValues[i], yValues[i], timeValues[i]) for i in range(len(xValues))]
        
        # create root window
        root = tk.Toplevel(self.parent)
        t = Table(root)
        root.mainloop()


    def setController(self, controller):
        self.controller = controller