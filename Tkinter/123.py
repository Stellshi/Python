from tkinter import *  
from tkinter import messagebox  
  
  
def clicked():  
    messagebox.showinfo('Заголовок', 'Текст')  
  
from tkinter import messagebox


res = messagebox.askokcancel('123123', 'Тgfgfgfекст')

  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
btn = Button(window, text='Клик', command=clicked)  
btn.grid(column=0, row=0)  
window.mainloop()