import tkinter as tk

class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view
        
        self.view.play_btn.config(command=self.play_pause)

    def play_pause(self):
        self.video.pause_video()
        print("ff")

            

        

        