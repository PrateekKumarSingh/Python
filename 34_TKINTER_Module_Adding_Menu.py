from tkinter import *

root = Tk()
root.geometry("300x100")

menu = Menu(root)
root.config(menu=menu) # adding menu widget to the root form

file =  Menu(menu) # dropdown menu widget
file.add_command(label='Open',) # Dropdown menu command
file.add_command(label='Save',) # Dropdown menu command
file.add_command(label='Exit', command=exit) # Dropdown menu command

menu.add_cascade(label='File', menu=file) # adding dropdown menu to the menu bar under 'File' button

edit = Menu(menu) # dropdown menu widget
edit.add_command(label='Undo') # Dropdown menu command
edit.add_command(label='Replace') # Dropdown menu command
edit.add_command(label='Find') # Dropdown menu command

menu.add_cascade(label='Edit', menu=edit) # adding dropdown menu to the menu bar under 'Edit' button

root.mainloop() # Show form

