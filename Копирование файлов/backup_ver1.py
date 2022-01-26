from distutils import command
from itertools import count
import os
import time

#1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source=['"C:\\Code"']

#2. Резернвые копии должны храниться в основном каталоге резерва.

target_dir = 'D:\\Copy' #Путь куда будет копироваться копия

#3.Файлы помещаются в zip-архив
#4.Именем для zip-архива служит текущая дата и время.

target=target_dir+os.sep+time.strftime("%Y%m%d%H%M%S") + '.zip'

#5.Используем команду zip  для помещения файлов в zip-архив
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# Запускаем резервное копирование
print('Zip command is:')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
    print("Резервная копия успешно создана в ", target)
else:
    print("Создание резервной копии НЕ УДАЛОСЬ")