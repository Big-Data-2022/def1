# GITHUB
# ---------------------------------------------------------------------------------------------------------

# Если хотим запушить все на новую репозиторию 
# rm -rf                                    = Удаляем папку .git которая уже связано к старой репозитории
# git init                                  = инитцализирует и создает папку .git
# git remote add origin (shh репозитория)   = Копируем ssh нашего репозирия и вставляем
# git add .                                 = Выделяем все наши файлы
# git commit -m "all"                       = Коментим репозиторию
# git push -u origin master                 = Пушим все в ветку мастер

# ---------------------------------------------------------------------------------------------------------

# Если хотим отправить на тот же репозитории тогда не удаляем папку .git
# git add .                                 = Выделяем все наши файлы
# git commit -m "all"                       = Коментим репозиторию
# git push -u origin master                 = Пушим все в ветку мастер

# ---------------------------------------------------------------------------------------------------------
# OPEN and WITH

# f = open('marselle.py','r')
# a = f.readlines()
# f.close()
# print(a)

# with open('marselle.py','w') as f:
#     f.write('\nhello error')

# import marselle
# print(marselle.name)
# print(marselle.age)


# date = {

# }

# day = input("Укажите число: ")
# month = input("Укажите месяц: ")
# year = input("Укажите год: ")

# date.update( {
#             "year": year,
#             "month": month,
#              "day" : day
#             })
# print(date)


# while True:
#     if Salomon is not None:
#             print(f'     Здраствуйте уважаемый клиент{Salomon}\(>_<)/'  )
#     m = input("""
#     1 >>> Зарегистрироваться
#       2 >>> Авторизоваться
#       3 >>> Информация 
#       4 >>> Выйти
#      Выберите действие: """)
#     user1 = {

#     }

# if m == 1:
#         login = input("Введите логин: ")
#         if login not in user1.keys():
#             password =('Введите пароль:') 
#             password2 =('Введите пароль повторно: ')
#             if password == password2 and len(password2) >8:
#                 user1.update( {
#                             login :{
#                                 'login': login,
#                                 'password':password2
#                                    }
#                         } )


# final = {
#     'task': """
#      1. Добавить новый город
#             2. Отобразить список городов
#             3. Заменить город
#             4. Удалить город
#             5. Выход
#     """}


# def calculator(oper, x=1, y=1):
#     if oper == '+':
#         return x + y
#     elif oper == '-':
#         return x - y
#     elif oper == '*':
#         return x * y
#     elif oper == '/':
#         return x / y
#     # return 'выберите другую оператцию'
#     else:
#         return 'выберите другую оператцию'

# from test11 import calculator, len1 
# a = 2324576
# b = "hello world"
# print(len1(a))
# print(len(b))
# print(calculator('+',3,68))


def random_int(num_list,size_list,min_n,max_n):
    from random import randint
    for i in range(size_list):
        num_list.append(randint(min_n,max_n))


