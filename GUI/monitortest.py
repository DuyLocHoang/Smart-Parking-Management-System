# Import library

from viewtest import *
from widget.addCamera import *
from utils.path_direct import *
from utils.util import check_ip


class Monitor:
    def __init__(self, window, window_title, status):
        self.status = status
        self.status.configure(text='ON')
        self.window = window
        # self.window2 =
        self.window.title(window_title)
        self.window.resizable(0, 0)
        self.vids = []
        self.add_camera = Tk.Label(self.window, width=0, height=0, text='NULL')
        self.status_Add = Tk.Label(self.window, width=0, height=0, text='OFF')
        self.Load()
        self.running = True
        self.Update()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    def Load(self):
        temp = []
        try:
            f = open(DATA_CAMERA, 'r')
            for line in f:
                temp.append([i.strip() for i in line.split(',')])
            f.close()
        except FileNotFoundError:
            print("[Monitor] Not found File Dataset")
        if len(temp) == 2 :
            if temp[1] == [''] :
                temp.remove(temp[1])
        columns = 2
        out = []

        for i in temp:
            # print(i)
            if check_ip(i[2]):
                out.append(i)
        # print("out",out)
        for p, i in enumerate(out):
            # print("p,i",p,i)
            x = p % columns
            y = p // columns
            datafile = "D:\\LVTN\\combine\\data\\{c}.yml".format(c = i[1])

            vid = tkCamera(self.window, i[0], 5 * x, 5 * y, i[1], i[2], 500, 250,data_file=datafile)

            self.vids.append(vid)

    def Update(self):
        if self.running:
            columns = 2
            for number, vid in enumerate(self.vids):
                x = number % columns
                y = number // columns
                vid.column = x * 5
                vid.row = y * 5
                vid.update_grid()
                vid.grid(row=y * 5, column=x * 5, padx=10, pady=10)
            return self.window.after(1, self.Update)

    def on_closing(self, event=None):
        self.status.configure(text='OFF')
        print('[Monitor] stoping threads of camera')

        for source in self.vids:
            # source.delete()
            print(source)
            source.camera.running_thread = False
            source.camera.thread.join(0.1)
            print('[Camera] is closed', source.camera.thread.getName)
            if source.camera.vid.isOpened():
                source.camera.vid.release()
        print('[Monitor] stoping threads of camera Done !!!')
        self.vids = []
        if self.running:
            self.running = False
            print('[Monitor] exit')
        self.window.destroy()


if __name__ == '__main__':
    root = Tk.Tk()
    root.config(bg=COLOR_BACKGROUND)
    a = Tk.Label(root, text="User")
    Monitor(root, "Monitor camera App", a)
    print(os.getcwd())
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print(files)
    root.mainloop()