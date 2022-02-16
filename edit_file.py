import os

list_paths =[]

for adress, papka, file in os.walk('C:\\'):
    for i in file:
        full_path = os.path.join(adress, i)
        list_paths.append(full_path)
        
        
# 'r' открыть для чтения (по умолчания)
# 't' открыть в текстовом режиме (по умолчанияю)
# 'w' открыть для записи, содержимое файла удаляется, если файла нет, создается новый
# 'a' открыть для дозаписи в конец файла, если файла нет, создается новый
# 'b' открыть в бинарном режиме
# '+' открыть для чтения и записи "r+", 'w+', 'a+'


r = open('text.txt','w')
for x in list_paths:
    r.write(x + '\n')
    
r.close

