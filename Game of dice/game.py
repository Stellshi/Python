from cProfile import label
from msilib.schema import File
from tkinter import *
from tkinter import font


root = Tk()
root.geometry('400x200')
root.title('Игра в кости.')
root.resizable(height=False, width=False)
root.iconphoto(True,PhotoImage(file=('iconka.png')))


font = PhotoImage(file=('holst.png'))


# Label(root,image=font).pack()


root.mainloop()