from cProfile import label
from msilib.schema import File
from tkinter import *
from tkinter import font
from tkinter.tix import IMAGE

import random,time

def bros(): 
    x = random.choice(['C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\\b.png','C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\\b2.png','C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\\b3.png','C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\\b4.png','C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\\b5.png','C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\\b6.png'])
    return x

def img(event):
    global b1, b2 
    for i in range(10):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image']=b1
        lab2['image']=b2
        root.update()
        time.sleep(0.12)


root = Tk()
root.geometry('400x200')
root.title('Игра в кости.')
root.resizable(height=False, width=False)
root.iconphoto(True,PhotoImage(file=('C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\iconka.png')))
font = PhotoImage(file=('C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\holst.png'))
Label(root,image=font).pack()

lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER) #размещение метки по центру с координатами

lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)  #anchor=CENTER центр метки



root.bind('<1>',img)

img('event')

root.mainloop()