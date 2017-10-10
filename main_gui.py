from tkinter import *
import win32api

class Application(Frame):
    def do_something(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.upperdiv = LabelFrame(self)
        self.upperdiv.pack()
        
        self.filetypes = LabelFrame(self, text="File Types" )
        self.filetypes.grid(in_=self.upperdiv,column=1, row=1,sticky=E+W, padx=15)
        
        self.jpg  = Checkbutton(self, text="jpg",  variable=1).grid(in_=self.filetypes, sticky=W, column=1, row=1)
        
        self.pdf  = Checkbutton(self, text="pdf",  variable=2).grid(in_=self.filetypes, sticky=W, column=1, row=2)
        
        self.docx = Checkbutton(self, text="docx", variable=3).grid(in_=self.filetypes, sticky=W, column=2, row=1)
        #self.docx.grid(column=3, row=1, sticky=W)
        self.xlsx = Checkbutton(self, text="xlsx", variable=4).grid(in_=self.filetypes, sticky=W, column=2, row=2)
        #self.xlsx.grid(column=4, row=1, sticky=W)
        self.doc  = Checkbutton(self, text="doc",  variable=5).grid(in_=self.filetypes, sticky=W, column=3, row=1)
        #self.doc.grid(column=5, row=1, sticky=W)
        self.xls  = Checkbutton(self, text="xls",  variable=6).grid(in_=self.filetypes, sticky=W, column=3, row=2)
        #self.xls.grid(column=6, row=1, sticky=W)
        
        
        self.drives = LabelFrame(self, text="Drive")
        self.drives.grid(in_=self.upperdiv,column=2, row=1,sticky=E+W, padx=15)
        
        #gets the current available drives
        drives = win32api.GetLogicalDriveStrings()
        the_drives = drives.split('\000')[:-1]
        print(the_drives)
        
        variable = StringVar(self)
        variable.set(the_drives[0])
        self.dropdown = OptionMenu(self, variable, *the_drives)
        self.dropdown.grid(in_=self.drives, column=1, row=1, sticky=E+W, padx=15)
        
        self.hi_there = Button(self)
        self.hi_there["text"] = "Start"
        self.hi_there["command"] = self.do_something
        self.hi_there.grid(in_=self.drives, column=1, row=2, sticky=E+W, padx=16, pady=5)
        
        self.filesdiv = LabelFrame(self, text="Scanned Files" )
        self.filesdiv.pack(fill=BOTH, expand="yes")
        
        Label(self, text="FILES").grid(in_=self.filesdiv, column=1,row=1, padx=220, pady=150)
        
        self.progressbar = LabelFrame(self, text="Progress")
        self.progressbar.pack(fill=X)
        
        self.loading = Label(self, text="100%")
        self.loading.grid(in_=self.progressbar, column=1,row=1)
    
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
        self.pack() 
        self.createWidgets() #Creates widgets for the Frame
        master.minsize(width=500, height=500) #sets the minimum frame size
        self.center(master) #sets the position of the frame to the center of the screen
        master.wm_title("File Recovery Software")
        

root = Tk()
app = Application(master=root)
app.mainloop()