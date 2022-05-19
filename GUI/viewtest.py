import tkinter as Tk
import PIL.Image

from PIL import ImageTk, Image
from widget.tesst import *

from utils.path_direct import *

from selectArea import *
from draw import *
class tkCamera(Tk.Frame):
    def __init__(self, window, model, column, row, location="", video_source=0, width=None, height=None,data_file = None):
        super().__init__(window)
        self.column = column
        self.row = row
        # Variable basic
        self.name = location
        self.data_file = data_file
        self.window = window
        self.video_source = video_source
        self.camera = Camera(model, self.video_source,data_file=self.data_file,location = self.name)
        self.status_total = Tk.StringVar(window)
        self.status_free = Tk.StringVar(window)
        self.status_update = Tk.Label(self.window, width=0, height=0, text='OFF')
        self.label = Tk.Label(self.window, text = self.name, font='Helvetica 20 bold', bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
        self.label.grid(column=self.column + 0, row=self.row + 0, columnspan=5, sticky='')

        self.total_text = Tk.Label(self.window, text="Total: ", font='Helvetica 15 bold', bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
        self.total_text.grid(column=self.column + 0, row=self.row + 1, columnspan=5, sticky='')
        self.total = Tk.Label(self.window, textvariable=self.status_total, font='Helvetica 15 bold', bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
        self.total.grid(column=self.column + 1, row=self.row + 1, columnspan=5, sticky='')


        self.free_text = Tk.Label(self.window, text="Free: ", font='Helvetica 15 bold', bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
        self.free_text.grid(column=self.column + 0, row=self.row + 2, columnspan=5, sticky='')
        self.free = Tk.Label(self.window, textvariable=self.status_free, font='Helvetica 15 bold', bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
        self.free.grid(column=self.column + 1, row=self.row + 2, columnspan=5, sticky='')

        self.status_parkingslots = Tk.Label(self,width=0,height=0,text= 'OFF')
        self.btn_parkingslots = Tk.Button(self.window, text="PARKING SLOTS", command=self.parkingslots,
                                          font='Helvetica 12 bold',
                                          bg='#ffe973', fg='#b22222', height=2, width=18)
        self.btn_parkingslots.grid(column=self.column +0, row=self.row +3, pady=10, padx=10, sticky="W")

        self._setting = Tk.Label(self.window, width=0, height=0, text='NULL')
        self._update = Tk.Label(self.window, width=0, height=0, text='NULL')

        self.main = Tk.Label(self.window)
        self.main.grid(column=self.column + 0, row=self.row + 4, columnspan=5, rowspan=3)

        self.flagDelete = False

        # After it is called once, the update method will be automatically called every delay milliseconds
        # calculate delay using `FPS`
        if self.camera.flagErr != True:
            self.delay = int(1000 / 33)
        else:
            self.delay = 33
        self.delay = 1
        print('[tkCamera] source:', self.video_source)
        print('[tkCamera] fps:', self.camera.fps, 'delay:', self.delay)
        self.image = None
        self.running = True
        self.running_status = True

        self.update_frame()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)


    def update_frame(self):
        if self.flagDelete != True:
            ret, frame = self.camera.get_frame()

            if ret and not self.camera.flagErr:
                try:
                    frame = self.camera.img_show
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                    self.image = PIL.Image.fromarray(frame).resize((750, 500))
                    self.photo = PIL.ImageTk.PhotoImage(image=self.image)
                    self.main.imgtk = self.photo
                    self.main.configure(image=self.photo)
                    self.status_total.set(self.camera.total)
                    self.status_free.set(self.camera.free)
                except:
                    # print("ERR PIL.ImageTk.PhotoImage")
                    pass
            if self.running:
                self.window.after(self.delay, self.update_frame)

    def parkingslots(self):
        if self.status_parkingslots.cget('text') == "ON":
            messagebox.showwarning("Warning", "You need Close Edit Monitor")
        else:
            self.top5 = Tk.Toplevel()

            # self._parkingslots = Edit(self.top5,"D:\\LVTN\\combine\\videos\\video_2.mp4",self.status_parkingslots)

            # self._parkingslots = selectArea(window = self.top5,img = self.camera.img_show ,status = self.status_parkingslots)
            self._parkingslots = Edit(window=self.top5, video_dir=self.camera.img_show,data_dir=self.name, status=self.status_parkingslots,location = self.name)


    def on_closing(self, event=None):
        self.camera.running_thread = False
        self.camera.thread.join(0.1)
        print('[Camera] is closed', self.camera.thread.getName)
        print('[Camera] is closed', self.camera.thread2.getName)
        if self.camera.vid.isOpened():
            self.camera.vid.release()
        self.window.destroy()

    def update_grid(self):

        self.main.grid(column=self.column + 0, row=self.row + 4, columnspan=5, rowspan=3)
        self.label.grid(column=self.column + 0, row=self.row + 0, columnspan=5, sticky='')
        self.total_text.grid(column=self.column + 0, row=self.row + 1, columnspan=5, sticky='')
        self.total.grid(column=self.column + 1, row=self.row + 1, columnspan=5, sticky='')
        self.free_text.grid(column=self.column + 0, row=self.row + 2, columnspan=5, sticky='')
        self.free.grid(column=self.column + 1, row=self.row + 2, columnspan=5, sticky='')
        self.btn_parkingslots.grid(column=self.column + 0, row=self.row + 3, pady=10, padx=10, sticky="W")



if __name__ == '__main__':
    # Create a window and pass it to the Application object
    root = Tk.Tk()
    root.resizable(False, False)
    root.config(bg=COLOR_BACKGROUND)
    a = Tk.Label(root, location="User")
    tkCamera(root, 'yolov3', 0, 0, "Home", 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov', 500, 250,"D:\LVTN\combine\data\duyloc1.yml")
    # tkCamera(root,'yolov3-tiny',5,5, "Home",'video','video/video1.mp4',625,313)
    root.mainloop()