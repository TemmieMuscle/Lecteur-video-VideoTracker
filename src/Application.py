from models.Video import Video
from views.view import View
from controllers.Controller import Controller

import tkinter as tk

class Application(tk.Tk):

    def __init__(self):
        
        super().__init__()
        self.title('Video Tracker')

        # create a view and place it on the root window
        view = View(self)

        # create a video model
        video = Video(view)
        # test commands : change path of video for it to work
        video.load_video(r"C:\Users\leo\Documents\videotracker_b1\src\models\test.mp4") ### ne support qu'un path absolu pour une raison obscure
        video.play_video()

        # create a controller
        controller = Controller(video, view)

        # set the controller to view
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()

    # end of the main loop
    app.mainloop()

    