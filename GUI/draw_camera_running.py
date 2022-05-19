
from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import cv2
import tkinter as Tk
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
class Edit(Tk.Frame):
    def __init__(self,window,video_dir,data_dir,status):
        self.window = window
        self.status = status
        self.status.configure(text='ON')
        self.ids = 0
        self.counts = 0
        self.click_counts = 0
        self.coors = []
        self.data_dir = data_dir

        # Get frame from video to draw parking lots
        self.video_dir = video_dir
        cap = cv2.VideoCapture(self.video_dir)
        cap.set(cv2.CAP_PROP_POS_MSEC, 20000)

        success, img_cv2 = cap.read()

        img_cv2 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
        img_1 = Image.fromarray(img_cv2)
        img = ImageTk.PhotoImage(img_1)
        width, height = img_1.size

# -----------------------------------
        self.frame = Frame(window, bd=2, relief=SUNKEN)
        self.canvas = Canvas(self.frame, bd=0, width=width, height=height)
        self.canvas.grid(row=0, column=0)
        self.frame.pack(fill=BOTH, expand=1)
        self.canvas.create_image(0, 0, image=img, anchor="nw")
        self.canvas.bind("<Button 1>",self.printcoords)
        self.window.mainloop()

    def printcoords(self,event):
        self.coors.append((event.x, event.y))
        self.click_counts += 1
        print(self.coors)
        self.canvas.create_polygon(self.coors, outline='#f11', fill='', width=1)
        if self.click_counts >=4 :
            self.click_counts = 0
            coords = np.array(self.coors)
            if self.counts == 0 :
                mode = "w+"
            else:
                mode = "a"
            datadir = "D:\\LVTN\\combine\\data\\{c}.yml".format(c = self.data_dir)
            with open(datadir, mode) as points:
                points.write("-\n          id: " + str(self.ids) + "\n          coordinates: [" +
                                  "[" + str(coords[0][0]) + "," + str(coords[0][1]) + "]," +
                                  "[" + str(coords[1][0]) + "," + str(coords[1][1]) + "]," +
                                  "[" + str(coords[2][0]) + "," + str(coords[2][1]) + "]," +
                                  "[" + str(coords[3][0]) + "," + str(coords[3][1]) + "]]\n")
                for i in range(0, 4):
                    self.coors.pop()
            self.ids += 1
            self.counts +=1

    def close(self):
        self.status.config(text = "OFF")
        self.window.destroy()

if __name__ == "__main__":
    Edit(Tk(), "/videos/video_2.mp4")
