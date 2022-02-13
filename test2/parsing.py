from ast import walk
from importlib.metadata import files
import os
import time
from queue import Full

spisok = []

for adress, dirs, files  in os.walk('C:\Папка для примера'):
    # spisok.append(adress)
    for file in files:
        full= os.path.join (adress, file)
        # if '.txt' in full:
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full) 
    
print(spisok)