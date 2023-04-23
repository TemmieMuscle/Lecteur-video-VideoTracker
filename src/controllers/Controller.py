import tkinter as tk

class Controller:

    def __init__(self, video, view, FileRepo):
        
        self.video = video
        self.view = view
        self.FileRepo = FileRepo
        
        # Menu configuration
        self.view.fileMenu.entryconfig(0, command=self.loadVideo) 
        self.view.fileMenu.entryconfig(1, command=self.playAndLoadVideo) 
<<<<<<< HEAD
        self.view.fileMenu.entryconfig(3, command=self.FileRepo.save) ######## TO BE DISCONTINUED mais on verra quand on fera les points
=======
        self.view.fileMenu.entryconfig(3, command=self.FileRepo.save_data)
        
>>>>>>> 86dc013c2fd1c03ce760923fa9f6fc9cc2c023db
        # Video action buttons
        self.view.play_btn.config(command=self.video.pause_video)
        self.view.skipBackward_btn.config(command=self.video.skip_to_first_frame)
        self.view.skipForward_btn.config(command=self.video.skip_to_last_frame)
        self.view.back_btn.config(command=self.video.backward_one_frame)
        self.view.next_btn.config(command=self.video.forward_one_frame)

    def loadVideo(self):
        PATH=self.FileRepo.getFile() # get path with class FileRepo
        if isinstance(PATH,str)==True: # verify that PATH is STR
            self.video.load_video(PATH)

    def playAndLoadVideo(self):
        PATH=self.FileRepo.getFile() # get path with class FileRepo
        if isinstance(PATH,str)==True: # verify that PATH is STR
            self.video.load_and_play_video(PATH)


            

        
