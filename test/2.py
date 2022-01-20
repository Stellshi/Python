'''sp1 = ("Яблоки","Бананы","Капуста","Картошка","Грибы")
print(sp1)

print(sp1[2])
print(sp1[2:])
'''
#CЛОВАРИ

'''s1 = {"Ключ":"значение", "Яблоко":"Яблоня","Груша":"грушевое дерево","бананы": "Пальма"}

print (s1)
print(s1["Яблоко"])


s1["двигатель"] = "машина"

print(s1)

s1["Груша"] = "Высокое грушевое дерево"
print (s1)

del s1["Груша"]
print(s1)'''

#Massiv


arr_a = [23,32,54,5555,"hi","World"]
for i in range(len(arr_a)):
    print(arr_a[i])


print("Длинна массива: ",len(arr_a))


arr_b=[66,77,88]
arr_a.extend(arr_b)
arr_c = arr_a +arr_b
for i in range(len(arr_c)):
    print(arr_c[i])


print("Длинна массива: ",len(arr_c))

