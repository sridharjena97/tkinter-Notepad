from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("852x480")
    def statusbar(self):
        '''
        To show status at buttom of GUI
        '''
        self.status=StringVar()
        self.status.set("Ready")
        self.sbar=Label(self,textvariable=self.status,relief=SUNKEN,anchor="w")
        self.sbar.pack(side=BOTTOM,fill=X)
    def update_status(self,state="Ready"):
        '''
        To update status of GUI
        '''
        self.status.set(state)
        self.sbar.update()
    def create_button(self,master=None,btntxt="Button",bg="sky blue",relief=RAISED,bd=6,funcname=None,side=None,padx=3,pady=3,anchor=None,ipadx=10,ipady=None,**kwargs):
        '''
        To Create a button
        '''
        kargs={}
        for key,value in kwargs.items():
            kargs.__setitem__(key,value)
        btn=Button(master,text=btntxt,command=funcname,bg=bg,relief=relief,bd=bd,**kargs)
        btn.pack(side=side,padx=padx,pady=pady,anchor=anchor,ipadx=ipadx,ipady=ipady)
# Methods
def new():
    global file
    window.title("*Untitled - Notepad")
    file=None
    textarea.delete(1.0,END)

def openfile():
    global file
    file= askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file =="":
        file=None
    else:
        window.title(os.path.basename(file)+" - Notepad")
        textarea.delete(1.0,END)
        with open(file,"r") as f:
            textarea.insert(1.0, f.read())
        
def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            # save as new file
            with open(file,"w") as f:
                f.write(textarea.get(1.0,END))
                window.title(os.path.basename(file)+" - Notepad")
    else:
        # save the file
        with open(file,"w") as f:
                f.write(textarea.get(1.0,END))
                window.title(os.path.basename(file)+" - Notepad")

def saveas():
    file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    with open(file,"w") as f:
        f.write(textarea.get(1.0,END))
    window.title(os.path.basename(file)+" - Notepad") 
def exit():
    window.destroy()
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def cut():
    textarea.event_generate(("<<Cut>>"))
def about():
    showinfo("About","Notepad V-1.0 Developed by: Sridhar Jena ©SRIDHWORK-2020") 
    
# Fonts
dfont="Consolas 40 bold"
font1="Lucida 22 bold"
font2="Arial 12 normal"
if __name__ == "__main__":
    window=GUI()
    # window.statusbar()
    # window title
    window.title("*Untitled - Notepad")
    # Setting icon of the app
    window.wm_iconbitmap("notepad.ico")
    # Creating APP Menu
    mainmenu= Menu(window)
    # File Menu
    filemenu= Menu(mainmenu,tearoff=0)
    filemenu.add_command(label="New",command=new)
    filemenu.add_command(label="Open",command=openfile)
    filemenu.add_command(label="Save",command=save)
    filemenu.add_command(label="Save As",command=saveas)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=exit)
    mainmenu.add_cascade(label="File",menu=filemenu)
    # Edit Menu
    editmenu=Menu(window,tearoff=0)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    editmenu.add_command(label="Cut",command=cut)
    mainmenu.add_cascade(label="Edit",menu=editmenu)
    # Help Menu
    helpmenu=Menu(window,tearoff=0)
    helpmenu.add_command(label="About",command=about)
    mainmenu.add_cascade(label="Help",menu=helpmenu)
    # Configuring mainmenu
    window.config(menu=mainmenu)
    scroll= Scrollbar(window)
    scroll.pack(fill=Y,side=RIGHT,anchor="ne")
    textarea=Text(window,font=font2,yscrollcommand=scroll.set)
    file=None
    textarea.pack(fill=BOTH,expand=True,padx=3)
    scroll.config(command=textarea.yview)


    window.mainloop()