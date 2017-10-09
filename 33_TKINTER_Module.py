'''
Tkinter provides classes which allow the display, positioning and
control of widgets. Toplevel widgets are Tk and Toplevel. Other
widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
LabelFrame and PanedWindow.
'''

from tkinter import *

root = Tk()
root.geometry("200x80")
root.title("GUI") # title of the frame

def onclickA():
    label.configure(foreground = 'red');label.configure(text = 'Button A Clicked')
def onclickB():
    label.configure(foreground = 'green');label.configure(text = 'Button B Clicked')
def onclickC():
    label.configure(foreground = 'blue');label.configure(text = 'Button C Clicked')
def onclickD():
    label.configure(foreground = 'brown');label.configure(text = 'Button D Clicked')

label = Label(root, text='Press a button')  # label widget
label.place(x=10,y=40) # position the label

Abutton = Button(root,text="A",command=onclickA)# button widget
Abutton.place(x=10, y=10) # position the button

Bbutton = Button(root,text="B",command=onclickB)# button widget
Bbutton.place(x=30, y=10) # position the button

Cbutton = Button(root,text="C",command=onclickC)# button widget
Cbutton.place(x=50, y=10) # position the button

Dbutton = Button(root,text="D",command=onclickD)# button widget
Dbutton.place(x=70, y=10) # position the button

Exitbutton = Button(root,text="Exit",command=exit)# button widget
Exitbutton.place(x=110, y=10) # position the button

root.mainloop() # shows the window
