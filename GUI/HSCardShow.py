# -*- coding: utf-8 -*-

import tkinter
import os
from PIL import Image, ImageTk




def pic_list(dirname):
    pic_list=[]
    fullpath=os.curdir+dirname
    for pic in os.listdir(path=dirname):
        path=os.path.join(dirname,pic)
        if os.path.isfile(path):
            pic_list.append(path)
            print(path)
    return pic_list
    
def show_pic(role):
    if role == None :
        return
    
    photo_list=[]
    image_list=[]
    
    image_list=pic_list("pic\\"+role)  
    for f in image_list:
        image=Image.open(f)
        photo=ImageTk.PhotoImage(image)
        photo_list.append(photo)
        w=photo.width()
        h=photo.height()
        
    canvas=tkinter.Canvas(top,width=w*len(image_list)+10,height=h+5,bg="white" )
    
    for index,photo in enumerate(photo_list): 
        canvas.create_image(index*w+5,0,image=photo,anchor = "nw" )
        
    canvas.pack(fill=tkinter.X,expand=1)

top=tkinter.Tk()

role_s = None

def check_role(role):
    role_s=role
    show_pic(role)


mage_b = tkinter.Button(top,text="法师",command=check_role("Mage"),bg='blue',fg='black')
mage_b.grid(row = 0, column = 0)
mage_b.pack(fill=tkinter.X)

Hunter_b = tkinter.Button(top,text="猎人",command=check_role("Hunter"),bg='Green',fg='black')
Hunter_b.grid(row = 0, column = 1)
Hunter_b.pack(fill=tkinter.X)


label = tkinter.Label(top,text="hello world!")
label.grid(row = 1, column = 1)
label.pack(fill=tkinter.Y)



quit = tkinter.Button(top,text="退出",command=top.quit,bg='red',fg='white')
quit.pack(fill=tkinter.X)


tkinter.mainloop()

