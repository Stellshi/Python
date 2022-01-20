#привередливая считалка
#Демонстриурует работу команд break and couninue

count = 0
while True:
    count += 1
    # Завершить цикл если count принимает значение больше 10
    if count >10:
        break
    # пропустить 5
    if count == 5:
        continue
    print(count)
input("\n\n Нажмите Энтер чтобы выйти")