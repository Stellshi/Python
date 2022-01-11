'''n = input("Введи целое число: ")
try:
    n = int(n)
    print("Удачно")
except:
    print ("Что-то пошло не так")'''
    
try:
    n=input('Введите целое число: ')
    n=int(n)
    print('Все нормально. Вы ввели число', n)
except ValueError:
    print("Вы ввели не целое число")