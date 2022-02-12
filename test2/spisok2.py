n = list(range(1,21))
#b= n.copy()
#b= n[1::2] # срез [старт:стоп:шаг] от 1 до конца 
b= n[5:] # срез [старт:стоп:шаг] 
m = []

for i in n:
    if i%2 ==0:
        m.append(i)
        n.remove(i)
        
else:
    print(m)
    print(n)

print(b)