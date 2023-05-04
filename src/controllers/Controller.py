import tkinter as tk

class Controller:

    def __init__(self, video, view, FileRepo, PointHandler):
        
        self.video = video
        self.view = view
        self.FileRepo = FileRepo
        self.PointHandler = PointHandler
        
        # Menu configuration
        self.view.fileMenu.entryconfig(0, command=self.loadVideo) 
        self.view.fileMenu.entryconfig(1, command=self.playAndLoadVideo) 
        self.view.fileMenu.entryconfig(3, command=self.FileRepo.save_data) ######## TO BE DISCONTINUED mais on verra quand on fera les points        
        self.view.fileMenu.entryconfig(4, command=self.quit)

        self.view.viewMenu.entryconfig(0, command=self.PointHandler.printGraphe) 

        # Video action buttons
        self.view.play_btn.config(command=self.video.pause_video)
        self.view.skipBackward_btn.config(command=self.video.skip_to_first_frame)
        self.view.skipForward_btn.config(command=self.video.skip_to_last_frame)
        self.view.back_btn.config(command=self.video.backward_one_frame)
        self.view.next_btn.config(command=self.video.forward_one_frame)

        # set keyboard shortcuts
        self.view.parent.bind('<Control-o>',self.loadVideo)
        self.view.parent.bind('<Control-q>',self.playAndLoadVideo)

    # function who get a path of a video in PATH, and then call the function load_video of self.video. Have an "event" argument for handling .bind
    def loadVideo(self,event=None):
        PATH=self.FileRepo.getFile() # get path with class FileRepo
        if isinstance(PATH,str)==True: # verify that PATH is STR
            self.video.load_video(PATH)

    # function who get a path of a video in PATH, and then call the function load_and_play_video of self.video. Have an "event" argument for handling .bind
    def playAndLoadVideo(self,event=None):
        PATH=self.FileRepo.getFile() # get path with class FileRepo
        if isinstance(PATH,str)==True: # verify that PATH is STR
            self.video.load_and_play_video(PATH)

    # function who call function destroy of tkinter on self.view to stop app
    def quit(self):
        self.view.parent.destroy()


            

        
