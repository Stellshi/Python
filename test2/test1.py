from itertools import count


m = 'stroka text'
count = 0

for i in m:
    if i =='t':
        print("В строке буква Т")
        count += 1
        
    if i == 'a': #прирывание программы когда находит букву а
        break    
else:
    print("Цикл завершен, букв т", count)
        
print ('Программма работает дальше')
        