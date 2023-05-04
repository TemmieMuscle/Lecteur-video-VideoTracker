from models.Video import Video
from views.view import View
from controllers.Controller import Controller
from models.FileRepo import FileRepo
from models.PointHandler import PointHandler

import tkinter as tk

class Application(tk.Tk):

    def __init__(self):
        
        super().__init__()
        self.title('Video Tracker')

        # create a view and place it on the root window
        view = View(self)

        # Create all models
        pointHandler=PointHandler()
        video = Video(view)
        fileRepo=FileRepo()

        # create a controller
        controller = Controller(video, view, fileRepo, pointHandler)

        # set the controller to view
        view.setController(controller)
  

if __name__ == '__main__':
    app = Application()
    app.mainloop()

    