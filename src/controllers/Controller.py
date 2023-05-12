import tkinter as tk

class Controller:

    def __init__(self, video, view, FileRepo, PointHandler):
        
        self.video = video
        self.view = view
        self.FileRepo = FileRepo
        self.PointHandler = PointHandler
        self.editionMode = False # can the user add points by clicking the video ?
        self.scaleMode = False
        
        # Menu configuration
        self.view.fileMenu.entryconfig(0, command=self.loadVideo) 
        self.view.fileMenu.entryconfig(1, command=self.playAndLoadVideo) 
        self.view.fileMenu.entryconfig(3, command=self.saveData)     
        self.view.fileMenu.entryconfig(4, command=self.quit)

        self.view.viewMenu.entryconfig(0, command=self.printGraphe) 

        self.view.editMenu.entryconfig(0, command=self.switchMode)
        self.view.editMenu.entryconfig(1, command=self.showTable)
        self.view.editMenu.entryconfig(2, command=self.PointHandler.cleanTab)

        # Video action buttons
        self.view.play_btn.config(command=self.video.pause_video)
        self.view.skipBackward_btn.config(command=self.skip_to_first_frame)
        self.view.skipForward_btn.config(command=self.video.skip_to_last_frame)
        self.view.back_btn.config(command=self.video.backward_one_frame)
        self.view.next_btn.config(command=self.video.forward_one_frame)

        # set keyboard shortcuts
        self.view.parent.bind('<Control-o>',self.loadVideo)
        self.view.parent.bind('<Control-q>',self.playAndLoadVideo)

        # set keyboard events
        self.view.parent.bind('<Escape>', self.switchEditionOff)

        # set click event
        self.view.cadreMilieu.bind('<Button-1>',self.addPointInPointHandler)
        self.view.cadreMilieu.bind('<Button-3>',self.addScalePointInPointHandler)
        self.view.cadreMilieu.bind('<Button-2>',self.setOrthonormal)

    def switchMode(self, event=None) : # switch edition mode
        if self.editionMode == False:
            answer = self.view.DIALOG_EDITIONMODE()
            if answer == False:
                return
        else :
            self.view.DIALOG_HASQUITEDITION()
        self.editionMode = not self.editionMode

    def switchEditionOff(self, event=None) : # turn edition mode using escape key
        self.view.DIALOG_HASQUITEDITION()
        self.editionMode = False

    # fonction utilisé lors d'un click sur une frame de la vidéo => gére l'ajout des coordonnées du click et le numéro de la frame dans PointHandler
    def addPointInPointHandler(self,event):
        if self.editionMode and self.video.cap != None and self.video.frame_index != self.video.frames_max:
            frame_index=self.video.frame_index # récupère l'index de l'image dont les positions ont été récupérées
            tabOfEvent=[event.x,self.video.height - event.y, frame_index] # créer un tab de la forme [posX,posY, time] //  inverting y so (0,0) is in bottom left corner
            self.PointHandler.addPoint(tabOfEvent) # appel d'une méthode de self.PointHandler pour ajouter tabOfEvent dans son tab of coordonnées
            self.video.forward_one_frame() # avance d'une frame dans la vidéo

            if self.video.frame_index == self.video.frames_max : # Quitting edition mode when hitting last frame
                self.switchEditionOff()

    def addScalePointInPointHandler(self,event):
            if self.video.cap != None:
                tabOfEvent=[event.x,self.video.height - event.y] # créer un tab de la forme [posX,posY, time] //  inverting y so (0,0) is in bottom left corner
                self.PointHandler.addScalePoint(tabOfEvent) # appel d'une méthode de self.PointHandler pour ajouter tabOfEvent dans son tab of coordonnées

    def printGraphe(self, event=None) :
        self.PointHandler.printGraph(self.video.fps)

    def showTable(self) :
        self.PointHandler.showTable(self.video.fps)

    def saveData(self, event=None) :
        self.FileRepo.save_data(self.PointHandler.getTabFormattedPoint(self.video.fps)) 

    def skip_to_first_frame(self) : # handles keeping points or not
        if len(self.PointHandler.tabPoint) > 0 :
            answer = self.view.DIALOG_WANTPOINTSCLEARED()
            if answer == True :
                self.PointHandler.cleanTab()
            elif answer == None :
                return
        self.video.skip_to_first_frame()


    # function who get a path of a video in PATH, and then call the function load_video of self.video. Have an "event" argument for handling .bind
    def loadVideo(self,event=None):
        PATH=self.FileRepo.getFile() # get path with class FileRepo
        if PATH != None : # verify that PATH is valid
            self.video.load_video(PATH)
            self.PointHandler.tabPoint = [] # clean the tab in PointHandler

    # function who get a path of a video in PATH, and then call the function load_and_play_video of self.video. Have an "event" argument for handling .bind
    def playAndLoadVideo(self,event=None):
        PATH=self.FileRepo.getFile() # get path with class FileRepo
        if PATH != None : # verify that PATH is valid
            self.video.load_and_play_video(PATH)
            self.PointHandler.tabPoint = [] # clean the tab in PointHandler

    # update the orthonormal point with click coordonate
    def setOrthonormal(self,event):
        if self.video.cap != None:
            self.PointHandler.setOrthonormalPoint([event.x,self.video.height - event.y])
            self.view.DIALOG_OTHONORMALSET()

    # function who call function destroy of tkinter on self.view to stop app
    def quit(self):
        self.view.parent.destroy()


            

        
