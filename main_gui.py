from tkinter import *
import win32api

class Application(Frame):
    def do_something(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.jpg = Checkbutton(self, text="jpg", variable=1)
        self.jpg.grid(column=1, row=1, sticky=W)
        
        self.pdf = Checkbutton(self, text="pdf", variable=2)
        self.pdf.grid(column=2, row=1, sticky=W)
        
        self.docx = Checkbutton(self, text="docx", variable=3)
        self.docx.grid(column=3, row=1, sticky=W)
        
        self.xlsx = Checkbutton(self, text="xlsx", variable=4)
        self.xlsx.grid(column=4, row=1, sticky=W)
        
        self.doc = Checkbutton(self, text="doc", variable=5)
        self.doc.grid(column=5, row=1, sticky=W)
        
        self.xls = Checkbutton(self, text="xls", variable=6)
        self.xls.grid(column=6, row=1, sticky=W)
        
        #gets the current available drives
        drives = win32api.GetLogicalDriveStrings()
        the_drives = drives.split('\000')[:-1]
        print(the_drives)
        
        variable = StringVar(self)
        variable.set(the_drives[0])
        
        self.dropdown = OptionMenu(self, variable, *the_drives)
        self.dropdown.grid(column=7, row=1, sticky=W)
        
        self.hi_there = Button(self)
        self.hi_there["text"] = "ok",
        self.hi_there["command"] = self.do_something

        self.hi_there.grid(column=2, row=4, sticky=W)
    
    def center(self,toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    
    #master is tk
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid() 
        self.createWidgets() #Creates widgets for the Frame
        master.minsize(width=500, height=500) #sets the minimum frame size
        self.center(master) #sets the position of the frame to the center of the screen
        master.wm_title("File Recovery Software")
        

root = Tk()
app = Application(master=root)
app.mainloop()