from tkinter import N


n = input("Введите целоче число: ")

while type(n) !=int:
    try:
        n=int(n)
    except ValueError:
        print("Неправильно ввели")
        n=input("Введите целое число")
        
if n % 2 == 0:
    print("Четное")
else:
    print("Нечетное")