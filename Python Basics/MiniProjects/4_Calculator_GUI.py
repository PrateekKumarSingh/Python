from tkinter import *

root = Tk()
root.geometry("250x100")
root.title("Calculator")

def add():
    result.configure( text='Result = {0}'.format( str(int(num1.get(1.0, END))+int(num2.get(1.0, END))) ) )
def sub():
    result.configure( text='Result = {0}'.format( str(int(num1.get(1.0, END))-int(num2.get(1.0, END))) ) )
def mul():
    result.configure( text='Result = {0}'.format( str(int(num1.get(1.0, END))*int(num2.get(1.0, END))) ) )
def div():
    result.configure( text='Result = {0}'.format( str(int(num1.get(1.0, END))/int(num2.get(1.0, END))) ) )
def modulus():
    result.configure(text='Result = {0}'.format(
        str(int(num1.get(1.0, END)) % int(num2.get(1.0, END)))))

shift = 90
num1Label = Label(root, text='Number1')
num1Label.place(x=5,y=0)
num2Label = Label(root, text='Number1')
num2Label.place(x=5, y=20)

num1 = Text(root, height=1, width=17)
num1.place(x=0+shift, y=0)
num2 = Text(root, height=1, width=17)
num2.place(x=0+shift, y=20)

opLabel = Label(root, text='Operators')
opLabel.place(x=5 , y=45)

addButton = Button(root, text='+', command=add)
addButton.place(x=5+shift, y =45)
SubButton = Button(root, text='-', command=sub)
SubButton.place(x=25+shift, y=45)
MulButton = Button(root, text='X', command=mul)
MulButton.place(x=45+shift, y =45)
DivButton = Button(root, text='/', command=div)
DivButton.place(x=65+shift, y =45)
ModulusButton = Button(root, text='%', command=div)
ModulusButton.place(x=85+shift, y=45)


result = Label(root, text='Result')
result.place(x=5,y=70)
exitButton = Button(root, text='exit', command=exit)
exitButton.place(x=110+shift,y=45)
root.mainloop()
