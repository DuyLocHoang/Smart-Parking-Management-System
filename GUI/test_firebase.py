from utils.util import remove_tempdata
from monitortest import *
from viewtest_sensor import *
from widget.addCamera import *
from utils.path_direct import *
from selectArea import *
from draw import *
import cv2
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
class App(Tk.Frame):
    def __init__(self,window,):
            Tk.Frame.__init__(self,window)
            self.window = window
            self.window.title("Smart Parking Management System")
            self.window.resizable(0,0)
            self.status_monitor = Tk.Label(self,width=0,height=0,text= 'OFF')
            self.status_edit = Tk.Label(self,width=0,height=0,text= 'OFF')
            self.status_addCamera = Tk.Label(self,width=0,height=0,text= 'OFF')
            # self.status_parkingslots = Tk.Label(self,width=0,height=0,text= 'OFF')
         #LOGO
            Tk.Label(window ,text = "Smart Parking Management System",font='Helvetica 20 bold',fg=COLOR_TEXT,bg=COLOR_BACKGROUND).grid(column = 1,row = 0, columnspan=5,pady=50,padx=10,sticky='E')
            i=Image.open(LOGO)
            i =i.resize((100, 100), Image. ANTIALIAS)
            img = ImageTk.PhotoImage(i)
            image = Tk.Label(window, image=img,bg=COLOR_BACKGROUND)
            image.image = img
            image.grid(column = 0,row = 0,sticky='nw',padx=20,pady=10)

         #SETTING EMAIL
            self.var= Tk.IntVar()
            Tk.Checkbutton(window, command = self.toggle_pass, offvalue = 0, onvalue = 1, variable = self.var,text='Show Password',bg=COLOR_BACKGROUND).grid(row=4,column=3)
            Tk.Label(window ,text = "USERNAME: ",bg=COLOR_BACKGROUND).grid(row = 2,column = 2, pady = 10,sticky="W")
            Tk.Label(window ,text = "PASSWORD: ",bg=COLOR_BACKGROUND).grid(row = 3,column = 2, pady = 10,sticky="W")
            self.str_name=Tk.StringVar(window)
            self.str_password=Tk.StringVar(window)
            self.name_Entry=Tk.Entry(window,textvariable=self.str_name)
            self.name_Entry.grid(row = 2,column = 3, pady = 2,padx=12)
            self.password_Entry = Tk.Entry(window,textvariable=self.str_password,show="*")
            self.password_Entry.grid(row = 3,column = 3, pady = 2,padx=10)
            self.btn_email = Tk.Button(window, text="Login",command=self.login,font='Helvetica 12 bold',bg='#00cc00',fg='#b22222',height=1,width=8)
            self.btn_email.grid(column=3,row=5,pady = 5,padx = 10,sticky="W")

        #SET UP
            self.flag = True
            self.count =0
            self.flagSettingEmail=False
            self.msg = None

            self.password= None

            self.running=True
            self._monitor= None
            self._monitorsensor = None
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    # Check
    def check(self):
        if self.str_name.get() == "duyloc" and self.str_password.get() == "duyloc":
            self.validateLogin(self.str_name,self.str_password)
            self.flagSettingEmail = True
        else:
            self.flagSettingEmail = False

    def validateLogin(self,username,password):
        print("username entered :", username.get())
        print("password entered :", password.get())

    def toggle_pass(self):
        if self.var.get() == 1 :
            self.password_Entry.config(show = "")
        elif self.var.get() == 0 :
            self.password_Entry.config(show = "*")
#Open Monitor camera
    def login(self):
        if self.str_name.get() == "duyloc" and self.str_password.get() == "duyloc":
            self.validateLogin(self.str_name,self.str_password)
            self.flagSettingEmail = True
        else:
            self.flagSettingEmail = False

        if  self.flagSettingEmail :
            self.top = Tk.Toplevel()
            self.top.title("Smart Parking Management System")
            self.top.resizable(0,0)

            self.btn_monitor = Tk.Button(self.top, text="MONITOR", command=self.monitor, font='Helvetica 12 bold',
                                         bg='#ffe973', fg='#b22222', height=2, width=18)
            self.btn_monitor.grid(column=2, row=20, pady=10, padx=10, sticky="W")

            self.btn_edit = Tk.Button(self.top, text="EDIT", command=self.edit, font='Helvetica 12 bold',
                                         bg='#ffe973', fg='#b22222', height=2, width=18)
            self.btn_edit.grid(column=7, row=20, pady=10, padx=10, sticky="W")
            self.top.config(bg = COLOR_BACKGROUND)

    def edit(self):
        if self.status_edit.cget('text') == "ON":
            messagebox.showwarning("Warning", "You need Close Edit Monitor")
        else:
            self.top3 = Tk.Toplevel()
            self.btn_monitor = Tk.Button(self.top3, text="ADD CAMERA",command =self.addCamera, font='Helvetica 12 bold',
                                         bg='#ffe973', fg='#b22222', height=2, width=18)
            self.btn_monitor.grid(column=2, row=20, pady=10, padx=10, sticky="W")
            # -----------------------------------------------
            self.top4 = Tk.Toplevel()
            self.top4.config(bg=COLOR_BACKGROUND)
            # -----------------------------------------------



            # self.btn_parkingslots = Tk.Button(self.top3, text="PARKING SLOTS",command =self.parkingslots, font='Helvetica 12 bold',
            #                              bg='#ffe973', fg='#b22222', height=2, width=18)
            # self.btn_parkingslots.grid(column=7, row=20, pady=10, padx=10, sticky="W")
            self.top3.config(bg = COLOR_BACKGROUND)

    # def parkingslots(self):
    #     if self.status_parkingslots.cget('text') == "ON":
    #         messagebox.showwarning("Warning", "You need Close Edit Monitor")
    #     else:
    #         self.top5 = Tk.Toplevel()
    #
    #         # self._parkingslots = Edit(self.top5,"D:\\LVTN\\combine\\videos\\video_2.mp4",self.status_parkingslots)
    #
    #         self._parkingslots = selectArea(window = self.top5,img = None,status = self.status_parkingslots,)
    #         self.top5.config(bg = COLOR_BACKGROUND)



    def addCamera(self):
        if self.status_addCamera.cget('text') == "ON":
            messagebox.showwarning("Warning", "You need Close Edit Monitor")
        else:
            self.top4 = Tk.Toplevel()
            self._addCamera = AddCamera(self.top4,self.status_addCamera)
            self.top4.config(bg = COLOR_BACKGROUND)
    def monitor(self):
        if self.status_monitor.cget('text') == 'ON':
            messagebox.showwarning("Warning", "You need Close monitor Camera")
        else:
            self.top2 = Tk.Toplevel()

            self._monitor= Monitor(self.top2,'Camera monitor',self.status_monitor)
            self.top2.config(bg=COLOR_BACKGROUND)
            # ------------------------------
            self.top5 = Tk.Toplevel()
            self._monitorsensor = MonitorSensor(self.top5,'Sensor monitor',self.status_monitor)
            self.top5.config(bg=COLOR_BACKGROUND)
            # ------------------------------


        self.top.config(bg=COLOR_BACKGROUND)


    def on_closing(self):
        if self.running == True:
            self.running= False
            # self.thread_email.join(0.05)
        if self._monitor is not None:
            self._monitor.on_closing()
        remove_tempdata()
        print("[App] Exit")
        self.window.destroy()

if __name__ == '__main__':
    # Create a window and pass it to the Application object
    root = Tk.Tk()
    root.config(bg=COLOR_BACKGROUND)
    App(root)
    root.mainloop()