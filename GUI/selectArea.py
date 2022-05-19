from tkinter import messagebox
from tkinter import ttk
import tkinter as Tk
from draw import *
from utils.path_direct import *
COLOR_BACKGROUND    = '#d9f5ff'
COLOR_TEXT          = '#1e90ff'



class selectArea(Tk.Frame):
    def __init__(self, window,img, status):
        Tk.Frame.__init__(self, window)
        self.window = window
        self.status = status
        self.img = img
        self.status_draw = Tk.Label(self,width=0,height=0,text= 'OFF')
        self.status.config(text='ON')
        self.data = []
        Tk.Label(self.window, text='SELECT AREA', font='Helvetica 15 bold', fg=COLOR_TEXT,bg =COLOR_BACKGROUND ).grid(column=0,row=0,columnspan=2,padx=10,pady=5)
        self.area = {}

        with open(DATA_CAMERA, "r") as f :
            lines = f.readlines()
            for line in lines :
                check = line.replace("\n",'').split(',')
                self.area[check[1]] = check[2]

        print(self.area)


        Tk.Label(self.window,text='AREA :',font='Helvetica 10 bold',fg=COLOR_TEXT,bg=COLOR_BACKGROUND).grid(column=0,row=3,sticky='W',padx=10,pady=5)


        self.location = ttk.Combobox(self.window, width = 20,state="readonly")
        self.location['values'] = list(self.area.keys())
        # self.model.current(1)
        self.location.grid(column=1,row=3,padx=10,sticky='W')

        Tk.Button(self.window, text='Edit', font='Helvetica 15 bold', bg=COLOR_BACKGROUND, fg=COLOR_TEXT, height=1, width=8,
                  command=self.save).grid(column=0, row=8, columnspan=2, pady=10)
        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def save(self):
        if self.status_draw.cget('text') == "ON":
            messagebox.showwarning("Warning", "You need Close Edit Monitor")
        else:
            self.top = Tk.Toplevel()
            print(self.area[self.location.get()])
            # self._draw = Edit(self.top,self.area[self.location.get()],self.location.get(),self.status_draw)
            self._draw = Edit(self.top, self.img, self.location.get(), self.status_draw)

    def close(self):
        self.status.config(text="OFF")
        self.window.destroy()


if __name__ == '__main__':
    root = Tk.Tk()
    root.config(bg=_background)
    a = Tk.Label(root, text="User")
    b = Tk.Label(root, text="User")
    AddCamera(root, b, a)
    root.mainloop()