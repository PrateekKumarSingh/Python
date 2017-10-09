'''
Tkinter provides classes which allow the display, positioning and
control of widgets. Toplevel widgets are Tk and Toplevel. Other
widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
LabelFrame and PanedWindow.
'''

from tkinter import *

message = 'Press a button'
class Window(Frame):


    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master # to make this frame the root frame
        self.init_window() # custom function

    def init_window(self):
        self.master.title("GUI") # title of the frame
        self.pack(fill=BOTH,expand=1) 
        Abutton = Button(self,text="A",command=label.config(text = 'Button pressed')) # button widget
        Abutton.place(x=10, y=10) # position the button

        Bbutton = Button(self,text="B",command=self.action) # button widget
        Bbutton.place(x=30, y=10) # position the button
        
        Cbutton = Button(self,text="C",command=self.action) # button widget
        Cbutton.place(x=50, y=10) # position the button

        Dbutton = Button(self,text="D",command=self.action) # button widget
        Dbutton.place(x=70, y=10) # position the button
        
        label = Label(self, text=message)  # label widget
        label.place(x=10,y=40) # position the label

    def action():
        label.config(text = 'Button pressed')


#label.pack(fill=X, expand=1)
#
#button.pack(side=BOTTOM) # 



root = Tk()
root.geometry("200x80")
app = Window(root)
root.mainloop() # shows the window
