'''def func(a, b=5, c=10):
    print('a равно ', a, ', b равно ',b,', a c равно', c)
    
func(3,7)
func(25,c=24)
func(c=50,a=100)'''


from math import *
import pstats
n= int(input("ВВедите диапазон: "))
p=[2,3]
count = 2
a=5
while (count<5):
    b=0
    for i in range (2,a):
        if(i<= sqrt(2)):
            if(a % i ==0):
                print(a,"непростое")
                b=1
            else:
                pass
            
        if(b!=1):
            print(a,"простое")
            p=p+[a]
        count = count + 1
        a = a + 2
print(p)
    
