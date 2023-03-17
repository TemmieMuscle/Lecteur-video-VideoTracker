from models.Video import Video
from views.view import View
from controllers.Controller import Controller
from models.FileRepo import FileRepo

import tkinter as tk

class Application(tk.Tk):

    def __init__(self):
        
        super().__init__()
        self.title('Video Tracker')

        # create a view and place it on the root window
        view = View(self)

        # create a video model
        video = Video(view)
        #video.play_video()

        # create a FileRepo model
        fileRepo=FileRepo()

        # create a controller
        controller = Controller(video, view,fileRepo)

        # set the controller to view
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()

    # end of the main loop
    app.mainloop()

    