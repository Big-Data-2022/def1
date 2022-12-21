# from def1 import calculator, len1
from os import system
system('clear')

# # a = input('''
# # +
# # *
# # -
# # /
# # > ''')
# # n1 = int(input('n1: '))
# # n2 = int(input('n2: '))

# # print(calculator(a, n1, n2))

# a = 'hello world'
# b = 232345678
# print(len1(a))
# print(len1(b))

#  № 1



# def random_int(num_list: list, size_list: int, min_n: int, max_n: int):
#     from random import randint
#     for i in range(size_list):
#         num_list.append(randint(min_n, max_n))


#  № 2




# start = int(input('starting: ')) # 10
# def chislo_fib(num): # 10
#     start, b = 1, 1
#     for i in range(num): # 10
#         yield start
#         start, b =b, start + b
        
 
# print(list(chislo_fib(start))) # 10
# def fibonaci2():
#     fib1 = fib2 = 1
#     n = int(input('Введите номер элемента последовательности: '))
#     print(fib1, fib2, end=' ')
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=' ')
        
# fibonaci2()

# 3 В строке изменить последовательность слов на обратную
#   Напишите функцию, которая принимает строку слов и возвращает строку с теми же словами,
#   но идущими в обратном порядке.


# def reverse_text(text):
#     text = text.split()
#     text.reverse()
#     return ' '.join(text)

# print(reverse_text(input('Введите текст: ')))
# -----------------------------------------------------------
# # 4 Заполнение массива случайными числами
# #   Заполнить список случайными целыми числами и вывести на экран. 
# (С помощью функции) 2 аргумента

from random import randint

def random_num(max_num = 100):
    l = []
    for i in range(max_num):
        l.append(randint(1,max_num))
    return l

max_num = int(input("size "))
print(random_num(max_num))