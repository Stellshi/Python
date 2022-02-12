from itertools import count


m = 'stroka text'
count = 0

for i in m:
    if i =='t':
        continue
        print("В строке буква Т")  #пропуск итерации
        count += 1
    print(i)  #выводить значение i
    
else:
    print("Цикл завершен, букв т", count)
        
print ('Программма работает дальше')
        