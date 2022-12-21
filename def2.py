# from def1 import calculator, len1


# a = input('''
# +
# *
# -
# /
# >''')
# n1 = int(input('n1: '))
# n2 = int(input('n2: '))

# print(calculator(a, n1, n2))

# a = 'hello world'
# b = 12345678
# print(len1(a))
# print(len1(b))
# print(len(d))



# 1 Функция, заполняющая список числами
#   Напишите функцию, которая заполняет список случайными числами 
#   в указанном количестве и в пределах заданных границ значений. 
#   Реализуйте код вызова этой функции.


# from random import randint

# def random_int(num_list, size_list, min_n, max_n):
#     for i in range(size_list):
#         num_list.append(randint(min_n, max_n))

# n = []
# minint = int(input('minint: '))
# maxint = int(input('maxint: '))
# size_l = int(input('size_list: '))
# random_int(n, size_l, minint, maxint)
# print(n)
# -------------------------------------------------------------------------------------------------------------------------


# 2 Функции Фибоначчи
#   Примеры двух функция для ряда Фибоначчи. 
#   Первая функция принимает номер элемента ряда и возвращает его значение. 
#   Вторая функция принимает номер элемента и выводит на экран весь ряд Фибоначчи до элемента с заданным номером включительно.

# start = int(input('starting: '))
# def chislo_fib(num):
#     start, b = 0, 1
#     for i in range(num):
#         yield start
#         start, b =b, start + b


# print(list(chislo_fib(start)))



# def fibonaci2():
#     fib1 = fib2 = 1
#     n = int(input("Введите номер элемента последовательности: "))
#     print(fib1, fib2, end=' ')
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2,end ='')

# fibonaci2()




# -------------------------------------------------------------------------------------------------------------------------
# 3 В строке изменить последовательность слов на обратную
#   Напишите функцию, которая принимает строку слов и возвращает строку с теми же словами,
#   но идущими в обратном порядке.

# def reverse_text(text):
#     text = text.split()
#     text.reverse()
#     return ' '.join(text)

# print(reverse_text(input('Введите текст: ')))


# -------------------------------------------------------------------------------------------------------------------------

# 4 Заполнение массива случайными числами
#   Заполнить список случайными целыми числами и вывести на экран. (С помощью функции)
# from random import randint
# def random_num(l: list, s_l: int):
#     for i in range(s_l):
#         l.append(randint(1,100))
#     return l
# list_num = []
# size_list = int(input("size "))
# print(random_num(list_num, size_list))

