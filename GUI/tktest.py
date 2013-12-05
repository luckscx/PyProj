# -*- coding: utf-8 -*-

import tkinter
from PIL import Image, ImageTk

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get() )

top=tkinter.Tk()


image1 = Image.open(r"pic\Counterspell.png")
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open(r"pic\Eaglehorn Bow.png")
photo2 = ImageTk.PhotoImage(image2)

w=photo1.width()
h=photo1.height()

canvas=tkinter.Canvas(top,width=w*2+10,height=h+5,bg="white" )

canvas.create_image(0,0,image=photo1,anchor = "nw" )
canvas.create_image(w+5,0,image=photo2,anchor = "nw" )


canvas.pack(fill=tkinter.X,expand=1)

quit = tkinter.Button(top,text="退出",command=top.quit,bg='red',fg='white')
quit.pack(fill=tkinter.X)

label = tkinter.Label(top,text="hello world!")
label.pack(fill=tkinter.Y,expand=1)

scale = tkinter.Scale(top,from_=10,to=40,orient=tkinter.HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=tkinter.X,expand=1)

tkinter.mainloop()