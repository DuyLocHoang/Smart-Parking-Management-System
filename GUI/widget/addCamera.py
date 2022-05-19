import tkinter as Tk
from tkinter import messagebox
from tkinter import ttk
from utils.path_direct import *

_background='#d9f5ff'
_colortext='#1e90ff'
class AddCamera(Tk.Frame):
    def __init__(self,window,status):
        Tk.Frame.__init__(self,window)
        self.window = window
        self.status=status
        self.status.config(text = 'ON')
        self.data = []
        Tk.Label(self.window,text='ADD CAMERA',font='Helvetica 20 bold',fg=_colortext,bg=_background).grid(column=0,row=0,columnspan=2,padx=10,pady=5)
        Tk.Label(self.window,text='NAME CAMERA :',font='Helvetica 10 bold',fg=_colortext,bg=_background).grid(column=0,row=1,sticky='W',padx=10,pady=5)
        Tk.Label(self.window,text='IP CAMERA :',font='Helvetica 10 bold',fg=_colortext,bg=_background).grid(column=0,row=2,sticky='W',padx=10,pady=5)
        # Tk.Label(self.window,text='MODEL :',font='Helvetica 10 bold',fg=_colortext,bg=_background).grid(column=0,row=3,sticky='W',padx=10,pady=5)
        self.name_input = Tk.StringVar(self)
        self.name = Tk.Entry(self.window,textvariable=self.name_input,width=30).grid(column=1,row=1,padx=10,sticky='W')

        self.ip_input = Tk.StringVar(self.window)
        self.ip = Tk.Entry(self.window,textvariable=self.ip_input,width=30).grid(column=1,row=2,padx=10,sticky='W')


        # self.model = ttk.Combobox(self.window, width = 10,state="readonly")
        # self.model['values'] = ('yolov3','yolov3-tiny')
        # self.model.current(1)
        # self.model.grid(column=1,row=3,padx=10,sticky='W')

        Tk.Button(self.window,text='Save',font='Helvetica 15 bold',bg=_background,fg=_colortext,height=1,width=8,command=self.save).grid(column=0,row=7,columnspan=2,pady=10)
        self.window.protocol("WM_DELETE_WINDOW", self.close)
    def save(self):
        self.status.config(text="OFF")
        if len(self.name_input.get())!=0 and len(self.ip_input.get())!=0:
            self.data.append(["yolov3",self.name_input.get(),self.ip_input.get()])
            with open("D:\LVTN\combine\data\datacamera.txt","a") as f :
                for i in self.data:
                    f.write(",".join(i)+'\n')


        else:
            messagebox.showwarning("Warning", "You need fill out Update")
        
    def close(self):
        self.status.config(text="OFF")
        self.window.destroy()

if __name__ == '__main__':     
    root = Tk.Tk()
    root.config(bg=_background)
    a=Tk.Label(root ,text = "User")
    b=Tk.Label(root ,text = "User")
    AddCamera(root, b,a)
    root.mainloop()