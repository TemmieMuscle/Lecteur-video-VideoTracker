import tkinter as tk

class Controller:

    def __init__(self, video, view, fileRepo):
        
        self.video = video
        self.view = view
        self.FileRepo=fileRepo
        
        # Menu configuration
        self.view.fileMenu.entryconfig(0, command=self.loadVideo) 
        self.view.fileMenu.entryconfig(1, command=self.playAndLoadVideo) 
        self.view.fileMenu.entryconfig(3, command=self.FileRepo.save_data) ######## TO BE DISCONTINUED mais on verra quand on fera les points
        # Video action buttons
        self.view.play_btn.config(command=self.video.pause_video)
        self.view.skipBackward_btn.config(command=self.video.skipBackward)
        self.view.skipForward_btn.config(command=self.video.skipForward)
        self.view.back_btn.config(command=self.video.back)
        self.view.next_btn.config(command=self.video.next)

    def loadVideo(self):
        PATH=self.FileRepo.getFile() # get path with class FileRepo
        if isinstance(PATH,str)==True: # verify that PATH is STR
            self.video.load_video(PATH)

    def playAndLoadVideo(self):
        PATH=self.FileRepo.getFile() # get path with class FileRepo
        if isinstance(PATH,str)==True: # verify that PATH is STR
            self.video.play_and_load_video(PATH)


            

        
