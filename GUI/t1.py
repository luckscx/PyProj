import tkinter
from tkinter import *

root = Tk()

widget = Label(root)
widget.config(text='this is my first GUI!!')

widget.pack(side=TOP,expand=YES,fill=BOTH)
widget.mainloop()