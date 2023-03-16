import tkinter as tk

class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view
        
        # Menu configuration
        self.view.fileMenu.entryconfig(0, command=video.load_video) 
        self.view.fileMenu.entryconfig(1, command=video.play_and_load_video) 
        self.view.fileMenu.entryconfig(3, command=video.save_data) ######## TO BE DISCONTINUED mais on verra quand on fera les points
        # Video action buttons
        self.view.play_btn.config(command=self.play_pause)


    def play_pause(self):
            self.video.pause_video() # if video is not loaded

            

        

        