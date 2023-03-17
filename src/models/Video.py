import cv2
import PIL.Image, PIL.ImageTk
import tkinter as tk
class Video():

    def __init__(self, view):

        self.canvas = view.cadreMilieu
        self.pause = True
        self.delay = 15 # delay between frames

    # Load video with a file given
    def load_video(self,PATH) :
        self.cap = cv2.VideoCapture(PATH)
        self.pause = True
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT) ############ afficher la première frame de manière automatique apres avoir load la vidéo je te laisse faire
        self.canvas.config(width = self.width, height = self.height)
        #print(f"{self.width} : {self.height}") # DEBUG

        print("Successfully loaded video !")
    
    def play_and_load_video(self,PATH) :
        self.load_video(PATH)
        self.pause = False
        self.play_video()

   # get only one frame    
    def get_frame(self):   
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except:
            #print("end of the video !") # eventually make an error pop up ?
            return (ret, None)

    def play_video(self): 
        # Get a frame from the video source, and go to the next frame automatically by recursion
            ret, frame = self.get_frame()
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame)) ## go to view
                self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW) ## go to view
            if not self.pause:
                self.canvas.after(self.delay, self.play_video)   
        
    def pause_video(self): # set video in pause if it was playing, or play it if it was pause
        if self.pause==False:
            self.pause=True
        else:
            self.pause=False
            self.play_video()

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
    