from widget.sensor import *
from selectArea import *
from draw import *
class MonitorSensor:
    def __init__(self, window, window_title, status):
        # super().__init__(window)
        self.status = status
        self.status.configure(text='ON')

        self.window = window
        self.window.title(window_title)
        self.window.resizable(0, 0)

        self.sensor = Sensor()
        self.status_sensor = Tk.StringVar(window)

        self.status_update = Tk.Label(self.window, width=0, height=0, text='OFF')

        self.total_text = Tk.Label(self.window, text="Slot-1: ", font='Helvetica 15 bold', bg=COLOR_BACKGROUND, fg=COLOR_TEXT,width = 10, height = 3)
        self.total_text.grid(column= 1, row=5, columnspan=5, sticky='')
        self.total = Tk.Label(self.window, textvariable=self.status_sensor, font='Helvetica 15 bold', bg=COLOR_BACKGROUND, fg=COLOR_TEXT,width = 10, height = 3)
        self.total.grid(column=10, row=5, columnspan=5, sticky='')


        self.flagDelete = False

        self.delay = 1

        self.running = True
        self.running_status = True

        self.update_frame()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)


    def update_frame(self):
        if self.flagDelete != True:
            self.status_sensor.set(self.sensor.parkingStatus)
            if self.running:
                self.window.after(self.delay, self.update_frame)


    def on_closing(self, event=None):
        self.sensor.running_thread = False
        self.sensor.thread.join(0.1)
        print('[Camera] is closed', self.sensor.thread.getName)
        if self.running:
            self.running = False
            print('[Monitor] exit')
        self.window.destroy()

    def update_grid(self):
        self.total_text.grid(column=1, row=5, columnspan=5, sticky='')
        self.total.grid(column=10, row=5, columnspan=5, sticky='')

if __name__ == '__main__':
    # Create a window and pass it to the Application object
    root = Tk.Tk()
    root.resizable(False, False)
    root.config(bg=COLOR_BACKGROUND)
    a = Tk.Label(root, location="User")
    # tkCamera(root, 'yolov3', 0, 0, "Home", 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov', 500, 250,"D:\LVTN\combine\data\duyloc1.yml")
    # tkCamera(root,'yolov3-tiny',5,5, "Home",'video','video/video1.mp4',625,313)
    root.mainloop()