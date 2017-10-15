from tkinter import *
from Carver import *
import win32api

class Application(Frame):
    def do_something(self):
        #print ("hi there, everyone!")
        choices =[]
        
        if self.jpgvar.get() == 1:
            choices.append("jpg")
        if self.pdfvar.get() == 1:
            choices.append("pdf")
        if self.docxvar.get() == 1:
            choices.append("docx")
        if self.xlsxvar.get() == 1:
            choices.append("xlsx")
        if self.docvar.get() == 1:
            choices.append("doc")
        if self.xlsvar.get() == 1:
            choices.append("xls")
        if self.pngvar.get() == 1:
            choices.append("png")
        
        print(choices)
        
        driveLetter = self.variable.get()[0]
        
        
        print(driveLetter)
<<<<<<< HEAD
        
        
        threadcount = int(self.threadEntry.get())
        print('threadcount: ', threadcount)
        carve(choices, driveLetter, threadcount)
        print("--- %s seconds ---" % (time.time() - start_time))
        
=======
        carve(choices, driveLetter)
>>>>>>> parent of b26dad5... recker

    def createWidgets(self):
        self.upperdiv = LabelFrame(self)
        self.upperdiv.pack()
        
        self.filetypes = LabelFrame(self, text="File Types" )
        self.filetypes.grid(in_=self.upperdiv,column=1, row=1,sticky=E+W, padx=15)
        
        self.jpgvar = IntVar(self)
        self.jpg  = Checkbutton(self, text="jpg",  variable=self.jpgvar)
        self.jpg.grid(in_=self.filetypes, sticky=W, column=1, row=1)
        
        self.pdfvar = IntVar(self)
        self.pdf  = Checkbutton(self, text="pdf",  variable=self.pdfvar)
        self.pdf.grid(in_=self.filetypes, sticky=W, column=1, row=2)
        
        self.docxvar = IntVar(self)
        self.docx = Checkbutton(self, text="docx", variable=self.docxvar)
        self.docx.grid(in_=self.filetypes, sticky=W, column=2, row=1)
        
        self.xlsxvar = IntVar(self)
        self.xlsx = Checkbutton(self, text="xlsx", variable=self.xlsxvar)
        self.xlsx.grid(in_=self.filetypes, sticky=W, column=2, row=2)
        
        self.docvar = IntVar(self)
        self.doc  = Checkbutton(self, text="doc",  variable=self.docvar)
        self.doc.grid(in_=self.filetypes, sticky=W, column=3, row=1)
        
        self.xlsvar = IntVar(self)
        self.xls  = Checkbutton(self, text="xls",  variable=self.xlsvar)
        self.xls.grid(in_=self.filetypes, sticky=W, column=3, row=2)
        
        self.pngvar = IntVar(self)
        self.png  = Checkbutton(self, text="png",  variable=self.pngvar)
        self.png.grid(in_=self.filetypes, sticky=W, column=4, row=1)
       
        
        
        self.drives = LabelFrame(self, text="Drive")
        self.drives.grid(in_=self.upperdiv,column=2, row=1,sticky=E+W, padx=15)
        
        #gets the current available drives
        drives = win32api.GetLogicalDriveStrings()
        the_drives = drives.split('\000')[:-1]
        print(the_drives)
        
        self.variable = StringVar(self)
        self.variable.set(the_drives[0])
        self.dropdown = OptionMenu(self, self.variable, *the_drives)
        self.dropdown.grid(in_=self.drives, column=1, row=1, sticky=E+W, padx=15)
        
        self.hi_there = Button(self)
        self.hi_there["text"] = "Start"
        self.hi_there["command"] = self.do_something
        self.hi_there.grid(in_=self.drives, column=1, row=2, sticky=E+W, padx=16, pady=5)
        
<<<<<<< HEAD
        self.threads = LabelFrame(self, text="Threads")
        self.threads.grid(in_=self.upperdiv,column=3, row=1,sticky=E+W, padx=15)
        #Label(self.master, text="Thread Count:").grid(in_=self.threads, column=1, row=1, sticky=E+W)
        self.threadEntry = Entry(self.master, bd=2, width=6)
        self.threadEntry.grid(in_=self.threads, column=2, row=1, sticky=E+W, pady=5, padx=5)
        self.threadEntry.insert(0, "100")
        
        
=======
>>>>>>> parent of b26dad5... recker
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