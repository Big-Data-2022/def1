# git init


# def main(x, y):
#     return x+y
# print(main(5, 5))


# def len1(a):
#     n = 0
#     if a.isalpha():
#         for i in a:
#             n+=1
#     return n
# print(len1("qwerty"))        


# a = "qwerty"
# print(len(a))


# def adi(a, b=1):
#     return a + b
# print(adi(10))

#_________________________
# наш калькулятор принимает три пргумента (два аргумента по умолчанию =1)
# def calculator(oper, x=1, y=1):
#     if oper == "+":
#         return x + y
#     elif oper == "-":
#         return x - y  
#     elif oper == "*":
#         return x * y
#     elif oper == "/":
#         return oper == x / y
#     else:
#         return "выберете другую операцию"
# #___________________________

# def len1(a):
#     n = 0
#     try:
#         a = str(a)
#         for i in a:
#             n+=1
#         return n
#     except:
#         print("я принимаю только str snd int")

#____________________________#1
# from random import randint
# def random_int(num_list: list,size_list: int, min_n: int, max_n: int):
#     for i in range(size_list):
#         num_list.append(randint(min_n, max_n))
# n = []
# minint = int(input("minint: "))
# maxint = int(input("maxint: "))
# size_l = int(input("size_list: "))
# random_int(n, size_l, minint, maxint)
# print(n)
#_______________________________#

#____________________________#2___fibonachi
# start = int(input("starting: "))
# def chislo_fib(num):
#     start,b = 0, 1
#     for i in range(num):
#         yield start
#         start, b = b, start + b
# print(list(chislo_fib(start)))
#_____________________________

##2.2____________fibonachi
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
# fibonaci1()
# fibonaci2()
#____________________________________

#__3________________

# def reverse_text(text):
#     text = text.split()
#     text.reverse()
#     return ' '.join(text)
# print(reverse_text(input("Введите текст: ")))

#_________4___________

# from random import randint

# def random_num(l: list, s_l:int):
#     for i in range(s_l):
#         l.append(randint(1,100))
#     return l
# list_num = []
# size_list = int(input("size "))
# print(random_num(list_num, size_list))

#__________________________