import cv2
import PIL.Image, PIL.ImageTk
import tkinter as tk

class Video():

    def __init__(self, view):
        self.canvas = view.cadreMilieu
        self.compteurFrame = view.frameActuelle_lbl

        self.pause = True
        self.delay = 15 # delay between frames
        self.frame_index = 0
        self.frames_max = -1 # is -1 when nothing is loaded
        self.idImage = -1

    # Load video with a file given
    def load_video(self,PATH) :
        # get all data needed about the video
        self.cap = cv2.VideoCapture(PATH)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)
        self.frames_max = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1

        self.update_indexAndIndexMax() # setup indexation
        self.skip_to_first_frame() # go back to frame 1

        #print(f"{self.width} : {self.height}") # DEBUG
        #print("Successfully loaded video !")
    
    def load_and_play_video(self,PATH) :
        self.load_video(PATH)
        self.pause = False
        self.play_video()


    """The way cv2.read() works is by getting the n-th frame and moving forward to the n+1th frame 
    We used this fact as a basis to create all the needed fuctions and an index system"""

    def read(self) : # get frame and increments frame_index
        if self.cap.isOpened() :
            ret, frame = self.cap.read() # frame in cv2 format
            self.image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame)) # frame in tkinter format
            self.frame_index += 1

    def update_view(self) : # transform frame to tkinter image and sends it to the view / updates counter
        self.canvas.delete(self.idImage)
        self.idImage=self.canvas.create_image(0, 0, image = self.image, anchor = tk.NW)
        self.update_indexAndIndexMax()


    def play_video(self) : # forwards one frame until index is invalid and user did not pause
        if self.frame_index > 0 and self.frame_index < self.frames_max :
            self.forward_one_frame()
            if not self.pause :
                self.canvas.after(self.delay, self.play_video) 

    def forward_one_frame(self) : # reads() and updates() once
        if self.frame_index < self.frames_max :
            self.read()
            self.update_view()

    def backward_one_frame(self) : # goes back one frame
        if self.frame_index > 1 :
            self.frame_index -= 2
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_index)
            self.forward_one_frame()

    def skip_to_first_frame(self) : # goes back to the first frame
        self.frame_index = 0
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_index)
        self.forward_one_frame()

    def skip_to_last_frame(self) : # goes to the last frame
        self.frame_index = self.frames_max - 1
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_index)
        self.forward_one_frame()

    
    def pause_video(self): # set video in pause if it was playing, or play it if it was pause
        if self.pause==False:
            self.pause=True
        else:
            self.pause=False
            self.play_video()

    def update_indexAndIndexMax(self): # updates view for frames / frames_max
        frameActualOnFrameMax=str(self.frame_index)+"/"+str(self.frames_max)
        self.compteurFrame.config(text=frameActualOnFrameMax)


    # Release the video source when the object is destroyed
    def __del__(self):
        try : 
            if self.cap.isOpened():
                self.cap.release()
        except : # if no video is loaded
            pass


if __name__ == "__main__" :

    window = tk.Tk()
    window.title("Video Tracker [VIDEO MODEL]")

    vid = Video(window, 'test.mp4')
    vid.play_video()

    window.mainloop()
    