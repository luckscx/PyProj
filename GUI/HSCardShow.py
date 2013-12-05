# -*- coding: utf-8 -*-

import tkinter
import os
from PIL import Image, ImageTk




def pic_list(dirname):
    pic_list=[]
    for pic in os.listdir(path=os.curdir()+dirname):
        path=os.path.join(dirname,pic)
        if os.path.isfile(path):
            pic_list.append(path)
            print(path)
    return pic_list
    
def show_pic():
    pass
    

top=tkinter.Tk()

mage_b = tkinter.Button(top,text="法师",command=show_pic(),bg='blue',fg='black')
mage_b.grid(row = 0, column = 0)
mage_b.pack(fill=tkinter.X)

Hunter_b = tkinter.Button(top,text="猎人",command=show_pic(),bg='Green',fg='black')
Hunter_b.grid(row = 0, column = 1)
Hunter_b.pack(fill=tkinter.X)


label = tkinter.Label(top,text="hello world!")
label.grid(row = 1, column = 1)
label.pack(fill=tkinter.Y)

image1 = Image.open(r"pic\Mage\Counterspell.png")
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open(r"pic\Hunter\Snipe.png")
photo2 = ImageTk.PhotoImage(image2)

w=photo1.width()
h=photo1.height()

canvas=tkinter.Canvas(top,width=w*2+10,height=h+5,bg="white" )

canvas.create_image(0,0,image=photo1,anchor = "nw" )
canvas.create_image(w+5,0,image=photo2,anchor = "nw" )


canvas.pack(fill=tkinter.X,expand=1)

quit = tkinter.Button(top,text="退出",command=top.quit,bg='red',fg='white')
quit.pack(fill=tkinter.X)


tkinter.mainloop()