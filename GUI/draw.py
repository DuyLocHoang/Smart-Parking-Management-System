
from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import cv2
import tkinter as Tk
import os
import mysql.connector
import requests
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
class Edit(Tk.Frame):
    def __init__(self,window,video_dir,data_dir,status,location):
        self.window = window
        self.status = status
        self.location = location
        self.status.configure(text='ON')
        self.ids = 0
        self.counts = 0
        self.click_counts = 0
        self.coors = []
        self.send_cors = []
        self.data_dir = data_dir

        # Get frame from video to draw parking lots
        self.video_dir = video_dir
        # cap = cv2.VideoCapture(self.video_dir)
        # cap.set(cv2.CAP_PROP_POS_MSEC, 20000)
        #
        # success, img_cv2 = cap.read()

        img_cv2 = cv2.cvtColor(self.video_dir, cv2.COLOR_BGR2RGB)
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

        # self.window.protocol("WM_DELETE_WINDOW", self.close)

    # def insert_cordb(self, cor1, cor2, cor3, cor4, slotID):
    #     mydb = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="duyloc",
    #         database="parking"
    #
    #     )
    #     mycursor = mydb.cursor()
    #
    #     Q1 = "INSERT INTO coordinates (cor1, cor2, cor3, cor4, slotID) VALUES (%s,%s,%s,%s,%s)"
    #     val = (cor1, cor2, cor3, cor4, slotID)
    #
    #     mycursor.execute(Q1, val)
    #     mydb.commit()
    #     print(mycursor.rowcount, "slot data inserted.")

    def printcoords(self,event):
        self.coors.append((event.x, event.y))
        self.click_counts += 1
        # print(self.coors)
        self.canvas.create_polygon(self.coors, outline='#f11', fill='', width=1)
        if self.click_counts >=4 :
            self.click_counts = 0
            coords = np.array(self.coors)
            # print(self.coors)
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
            self.send_cors.append({'x_coordinate1': str(coords[0][0]),
                        'y_coordinate1': str(coords[0][1]),
                        'x_coordinate2': str(coords[1][0]),
                        'y_coordinate2': str(coords[1][1]),
                        'x_coordinate3': str(coords[2][0]),
                        'y_coordinate3': str(coords[2][1]),
                        'x_coordinate4': str(coords[3][0]),
                        'y_coordinate4': str(coords[3][1]),
                        'id': str(self.location[0] + str(self.ids +1))
                        })
            # try :
            #     r = requests.post("http://localhost:8080/coordinates", json=self.send_cors)
            #     print(self.send_cors)
            # except (requests.ConnectionError) as exception :
            #     print("No internet connection.")

            self.ids += 1
            self.counts +=1

    def close(self):
        self.status.config(text = "OFF")
        self.window.destroy()

if __name__ == "__main__":
    Edit(Tk(), "/videos/video_2.mp4")
