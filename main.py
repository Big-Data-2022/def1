# 1 Функция, заполняющая список числами
#   Напишите функцию, которая заполняет список случайными числами 
#   в указанном количестве и в пределах заданных границ значений. 
#   Реализуйте код вызова этой функции.

# from random import randint

# def random_number_list(number_list, size_list, min_number, max_number):
#     for i in range(size_list):
#         number_list.append(randint(min_number, max_number))

# number = []
# minimum = int(input("Min: "))
# maximum = int(input("Max: "))
# size = int(input("Quantity: "))

# random_number_list(number, size, minimum, maximum)
# print(number)
# -------------
# from random import randint
# minimum = int(input("Min: "))
# maximum = int(input("Max: "))
# size = int(input("Quantity: "))
# a = [randint(minimum, maximum) for i in range(size)]
# print(a)

# -------------------------------------------------------------------------------------------------------------------------

# 2 Функции Фибоначчи
#   Примеры двух функция для ряда Фибоначчи. 
#   Первая функция принимает номер элемента ряда и возвращает его значение. 
#   Вторая функция принимает номер элемента и выводит на экран весь ряд Фибоначчи до элемента с заданным номером включительно.

# a = int(input('Количества чисел: '))
# def chislo_fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
# print(list(chislo_fib(a)))

# -------------------------------------------------------------------------------------------------------------------------

# 3 В строке изменить последовательность слов на обратную
#   Напишите функцию, которая принимает строку слов и возвращает строку с теми же словами,
#   но идущими в обратном порядке.

# def reverse_text(text):
#     text = text.split()
#     text.reverse()
#     return ' '.join(text)

# print(reverse_text(input('Введите какой-то текст: ')))

# -------------------------------------------------------------------------------------------------------------------------

# 4 Заполнение массива случайными числами
#   Заполнить список случайными целыми числами и вывести на экран. (С помощью функции)

# from random import randint

# def random_number(list_num: list, size_list):
#     for i in range(size_list):
#         list_num.append(randint(1, 99))
#     return list_num

# list_number = []
# number = int(input('Количество чисел: '))
# print(random_number(list_number, number))

# -------------------------------------------------------------------------------------------------------------------------
