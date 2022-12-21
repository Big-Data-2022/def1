# import os
# os.system('clear')

# # def main(x,y):
# #     return x+y
# def len2(a):
#     n = 0
#     try :
#         a = str(a)
#         for i in a :
#                 n +=1
#         return int(n)
#     except :
#         print('принимаю тольо стр и инт ')
    
# # print(len2('qwertyuiop'))

# # def adi (a,b = 1):
# #     return a+b
# # print(adi(10))
# #--------------------------------
# def calculator(oper, x,y):
#     if oper == '+':
#         return x+y
#     elif oper == '-':
#         return x-y
#     elif oper == '*':
#         return x*y
#     elif oper == '/':
#         return x/y
#     return  'выберите другую операцию '
#     # else:
#     #     return 'выберите другую операцию '

# from def2 import randoom_nums

# # n = []
# x = int(input('min num: '))
# y = int(input('max num :'))
# size_l = int(input('size list :'))
# randoom_nums(n, x,y,size_l)
# print(n)

# start = int (input('starting : '))
# def fib_ch (num):
#     start,b = 0,1
#     for i in range (num):
#         yield start
#         start,b = b,start+b 

# print(list(fib_ch(start)))

# 3 В строке изменить последовательность слов на обратную
#   Напишите функцию, которая принимает строку слов и возвращает строку с теми же словами,
#   но идущими в обратном порядке.

# def reversed_text(text):
#    text = text.split()
#    text.reverse()
#    return " ".join(text)
#     #return text[::-1]
# print(reversed_text(input('vvedite text ')))

from random import *

def rand_num (y_razmer = 100):
    x = []
    for i in range(y_razmer):
        x.append(randint(1, y_razmer))
    return x 
list_num = []
y_razmer = int(input('vvedite razmer'))
print( rand_num(y_razmer))


