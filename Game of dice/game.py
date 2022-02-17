from cProfile import label
from msilib.schema import File
from tkinter import *
from tkinter import font
from tkinter.tix import IMAGE

import random,time

def bros(): 
    x = random.choice(['b.png','b2.png','b3.png','b4.png','b5.png','b6.png'])
    return x

def img():
    b1 = PhotoImage(file=(bros()))




root = Tk()
root.geometry('400x200')
root.title('Игра в кости.')
root.resizable(height=False, width=False)
root.iconphoto(True,PhotoImage(file=('C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\iconka.png')))
font = PhotoImage(file=('C:\\Users\Stellshi\Documents\GitHub\Python\Game of dice\holst.png'))
Label(root,image=font).pack()

lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER) #размещение метки по центру с координатами

lab1 = Label(root)
lab1.place(relx=0.7, rely=0.5, anchor=CENTER)



Button(root, text='Бросок', command=img).pack()

root.mainloop()