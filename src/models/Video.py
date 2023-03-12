import cv2
import PIL.Image, PIL.ImageTk
from tkinter import *

class Video:

    def __init__(self, window, window_title):

        self.window = window
        self.window.title(window_title)

        self.canvas = Canvas(window)
        self.canvas.pack()
        self.delay = 15   # ms
        self.open_file('test.mp4')
        self.play_video()
        self.window.mainloop()

    # Open video file
    def open_file(self, path): 
        self.pause = False
        self.cap = cv2.VideoCapture(path)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)
        print(f"{self.width} : {self.height}")


   # get only one frame    
    def get_frame(self):   
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except:
            #print("end of the video !") # eventually make an error pop up ?
            pass

    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        try :
            ret, frame = self.get_frame()
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame)) ## got to view
                self.canvas.create_image(0, 0, image = self.photo, anchor = NW) ## go to view
            if not self.pause:
                self.window.after(self.delay, self.play_video)   
        except :
            print(" End of the video")
        

        # Release the video source when the object is destroyed
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

if __name__ == "__main__" :
    Video(Tk(), "Video Tracker")