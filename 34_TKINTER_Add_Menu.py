from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog as tkFileDialog

message = 'Hey you are looking good!'
root = Tk()
root.title('TKinter Menu demo form')
root.geometry("500x600")

def showimage():
    load = Image.open(".\samplefiles\picture.jpg")
    render = ImageTk.PhotoImage(load)
    img  = Label(root, image=render)
    img.image = render
    img.pack()

def showtext():
    text = Label(root, text=message)
    text.pack()

def filesave():
    targetfile = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
    if targetfile is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    #text2save = str(text.get(1.0, END))  # starts from `1.0`, not `0.0`
    targetfile.write(message)
    targetfile.close()  # `()` was missing.

menu = Menu(root)
root.config(menu=menu) # adding menu widget to the root form

filemenu = Menu(menu) # dropdown menu widget
filemenu.add_command(label='Save',command=filesave) # Dropdown menu command
filemenu.add_separator() # adds a separator between menu items
filemenu.add_command(label='Exit', command=exit) # Dropdown menu command

editmenu = Menu(menu) # dropdown menu widget
editmenu.add_command(label='Show Image', command=showimage) # Dropdown menu command
editmenu.add_separator()  # adds a separator between menu items
editmenu.add_command(label='Show Text', command=showtext) # Dropdown menu command

# adding the dropdown menu to the Main menu
menu.add_cascade(label='File', menu=filemenu) # adding dropdown menu to the menu bar under 'File' button
menu.add_cascade(label='Tools', menu=editmenu) # adding dropdown menu to the menu bar under 'Edit' button

root.mainloop() # Show form
