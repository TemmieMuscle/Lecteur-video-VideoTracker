import tkinter as tk

class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view
        
        # Menu configuration
        self.view.fileMenu.entryconfig(0, command=video.load_video) 
        self.view.fileMenu.entryconfig(1, command=video.play_and_load_video) 

        # Video action buttons
        self.view.play_btn.config(command=self.play_pause)


    def play_pause(self):
        self.video.pause_video()

            

        

        