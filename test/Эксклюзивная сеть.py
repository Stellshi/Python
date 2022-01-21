#Эксклюзивная компьютерная сеть
#Демонстрирует составные условия и логические операторы

print("Эксклюзивная компьютерная сеть")
print("Только для зарегестрированных пользователей")

security = 0
username=""

while not username:
    username = input("Логин: ")
password =""
while not password:
    password = input("Пароль: ")
if username == "Dawson" and password=="secret":
    print("Привет Давсон")
    security = 5
elif username =="Miler" and password =="civilization":
    print("Привет Милер")
    security=3
elif username=="Neo" and password=="123":
    print("Привет Neo")
    security=3
elif username=="guest" and password=="guest":
    print("Добро пожаловать к нам в гости.")
    security=1
else:
    print("Войти в систему не удалось. Должно быть. Вы не очень эксклюзивный гражданин")
input("Нажмите Энтер чтобы выйти из программы.")