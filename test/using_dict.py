# 'ab' -  сокращение от адрес бук

ab = {'Swaroop' : 'swaroop@swaroopch.com',
      'Larry'   : 'larry@wall.org',
      'Matsumoto' : 'matz@ruby-lang.com',
      'Spammer': 'spammer@gotmail.com'
    
}

print("Адрес Swaroop`a", ab['Swaroop'])

# удаление пары клю-значение

del ab['Spammer']

print('\nВ адресной книге {0} контакта'.format(len(ab)))

for name, adress in ab.items():
    print('Контакт {0} c адресом {1}'.format(name,adress))

# добавление пары ключ-значение

ab['Guido']= 'guido@python.org'

if 'Guido' in ab:
    print('Адрес Guido: ', ab['Guido'])