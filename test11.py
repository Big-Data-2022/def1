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


# def len1(a):
#     n = 0
#     try:
#         a = str(a)
#         for i in a:
#             n+=1
#         return int(n)

#     except:
#         print("я могу пройтись только по  str and int")


# from test10 import random_int

# n = []
# minint = int(input("minint: "))
# maxint = int(input("maxint: "))
# size_l = int(input("size_list: "))
# random_int(n,size_l,minint,maxint)
# print(n)


# start = int(input("Starting: "))# 10

# def chislo_fib(num):
#     start, b = 0, 1
#     for i in range(num):
#         yield start
#         start, b = b, start + b

# print(list(chislo_fib(start)))


# def fibonaci1():
#     fib1 = fib2 = 1
#     n = input("Номер элемента ряда Фибоначчи: ")
#     n = int(n) - 2
#     while n > 0:
#         fib1, fib2 = fib2, fib1 + fib2
#         n -= 1
#     print("Значение этого элемента:", fib2)

# def fibonaci2():
#     fib1 = fib2 = 1
#     n = int(input('Введите номер элемента последовательности: '))
#     print(fib1, fib2, end=' ')
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=' ')

# fibonaci2()


# def reverse_text(text):
#     text = text.split()
#     text.reverse()
#     return ' '.join(text)


# print(reverse_text(input("Введите текст: ")))


# from random import randint

# def random_num(l: list, s_l: int, max_num = 100):
#     for i in range(s_l):
#         l.append(randint(1,max_num))
#     return l
# list_num = []
# size_list = int(input("size: "))
# print(random_num(list_num, size_list))
