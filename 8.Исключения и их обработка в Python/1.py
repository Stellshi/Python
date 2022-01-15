'''n = input("Введи целое число: ")
try:
    n = int(n)
    print("Удачно")
except:
    print ("Что-то пошло не так")'''
    
  #error  
'''try:
    n=input('Введите целое число: ')
    n=int(n)
    print('Все нормально. Вы ввели число', n)
except ValueError:
    print("Вы ввели не целое число")'''
   #3 errors 
'''try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    c= a/b
    print("Частное: %.2f" % c)
except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    print("Нельзя делить на ноль")
    '''
    #Группировка ошибок
'''try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    c= a/b
    print("Частное: %.2f" % c)
except(ValueError, ZeroDivisionError):
    print("Нельзя вводить строки или делить на ноль")'''
    #Ошибки finally
    
'''try:
    n= input('Vvedite 4islo: ')
    n= int(n)
except ValueError:
    print("Neverno")
else: 
    print ('Vse OK, vashe shislo', n)
finally:
    print("end programs") '''
    
a_str = input("Введите первое значние: ")
b_str = input("Введите второе значние: ")


try:
    a_num = float(a_str)
    b_num = float(b_str)
    print("Результат: " , a_num + b_num)
except ValueError:
    print("Результат: " , a_str + b_str)
