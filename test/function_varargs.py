
# Переменное число параметров

import numbers


def total(a=5, *numbers, **phonebook):
    print('a', a)
    
    #Проход по всем элементам кортежа
    for single_intem in numbers:
        print('single_item', single_intem)
        
    #Проход по всем элементам словоря
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
        
print (total(10,1,2,3,Jack=1123,John=2231,Inge=1560))