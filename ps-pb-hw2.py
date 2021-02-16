import time
import os

os.system('cls') # Очищаем консоль

i = 0 # Здесь и далее i - переменная для цикла

# Создаём словари с паролями для юзеров
account1 = {'login': 'ivan','password':'q1'}
account2 = {'login': 'petr','password':'q2'}
account3 = {'login': 'olga','password':'q3'}
account4 = {'login': 'anna','password':'q4'}

# Создаём бд с данными юзеров
user1 = {'name':'Иван','age':20,'account':account1}
user2 = {'name':'Пётр','age':25,'account':account2}
user3 = {'name':'Ольга','age':18,'account':account3}
user4 = {'name':'Анна','age':27,'account':account4}

user_list = [user1,user2,user3,user4] # Список всех юзеров
key = input('Введите ключ (name или account): ') # Запрашиваем ключ
key = key.lower() # Переводим ключ в нижний регистр

# Проверка на существование ключа 
try:
    # Вывод информации по ключу обо всех пользователях
    while i < 4:
        user_list0 = user_list[i]
        key_print = user_list0[f'{str(key)}']
        print (f'значение ключа {key} для юзера {i+1} = ' + str(key_print))
        i = i + 1
# Вывод ошибки и выход из программы
except KeyError:
    print("Введенный ключ не найден")
    exit()

print(' ') # Разделение блоков программы

# Запрашиваем порядковый номер юзера с проверкой
try:
    listnumb = input('Введите порядковый номер: ') 
    # Номера юзеров 1-4, для работы со списком вычитаем 1
    user_listx = user_list[int(listnumb) - 1] 
    # Вывод ошибки и выход из программы
except:
    print('Пользователь с указанным номером не найден')
    exit()

# Вывод данных по выбранному юзеру
print('Данные по юзеру №' + listnumb + ':')
print('имя: ' + user_listx['name'])
print('возраст: ' + str(user_listx['age']))
print('логин: ' + user_listx['account']['login'])
print('пароль: ' + user_listx['account']['password'])

# Переменные для работы цикла и расчета среднего возраста
a = 0
average_age = 0

while a < 4: # Цикл для расчета среднего возраста юзеров
    user_list1 = user_list[a]
    average_age = average_age + user_list1['age']
    a = a + 1

# Вывод среднего возраста юзеров из БД
print('Средний возраст пользователей:' + str(average_age/4))

print(' ') # Разделение блоков программы

# Запрашиваем порядковый номер юзера для переноса в конец списка
move_user = input ('Введите номер пользователя, которого нужно переместить в конец: ')

# Вывод юзера для переноса в конец списка
# Номера юзеров 1-4, для работы со списком вычитаем 1
print(user_list[int(move_user)-1]) 
print(' ')

# Вывод списка юзеров до изменения
i = 0
while i < 4:
    user_list_mu = user_list[i]
    print (user_list_mu)
    i = i + 1

# Перенос юзера в конец списка
print(' ')
user_list_mu = user_list.pop(int(move_user)-1)
user_list.append(user_list_mu)

# Вывод списка юзеров после изменения
i = 0
while i < 4:
    user_list_mu = user_list[i]
    print (user_list_mu)
    i = i + 1