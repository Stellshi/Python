from multiprocessing.sharedctypes import Value


price = {'meat':2, 'bread':1, 'potato':0.5, 'wather': 0.2}


# new_price ={}

# for i in price:
#     new_price[i] = round( price[i]  * 0.85, 2)
    
   
# new={}    

# for  key,value in price.items(): #ключ и значение
#     new[value] = key # значение стало ключем, а ключ значением
    
    
# print(new)
#     # print(key)
#     # print(value) 


for value in price.values(): # Значения словаря
    print(value)

    