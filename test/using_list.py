#"Это мой списко покупок"

shoplist = ['яблоки','манго','морковь','бананы']

print('Я должен сделтаь', len(shoplist),'покупки.')

print('покупки: ', end = ' ') #печатать список покупок до конца "end = ' ' пока не будет пустоты"
for item in shoplist:
    print(item, end=' ')
    
print('Так же нужно купить риса.')
shoplist.append('рис')  # добавляет в конец списка рис
print('Теперь мой список покупок таков: ', shoplist ) 

print("Отсортирую я свой список")
shoplist.sort() #сортировка      
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это',shoplist[0]) # выбирает первый объект по модулю
olditem=shoplist[0]
del shoplist[0]
print('я купил', olditem)
print('Теперь мой список покупок:', shoplist)