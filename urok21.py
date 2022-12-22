# def main(x,y):
#     return x+y

# print(main(5,5))



# def len1(a):
#     n =0
#     try:
#         a=str(a)
#         for i in a:
#             n+=1
#         return n
#     except:
#         print('я принимаю только str и int')



# def adi(a,b=10):
#     return a+b
# print(adi(10))





# def calculator(oper,x,y):
#     if oper =='+':
#         return x + y
#     elif oper =='-':
#         return x - y
#     elif oper =='*':
#         return x * y
#     elif oper =='/':
#         return x / y
#     return"error"



#1
# from random import randint
# def random_int(num_list ,size_list,min_n,max_n):
#     for i in range(size_list):
#         num_list.append(randint(min_n,max_n))

# n =[]
# minint =int(input())
# maxint = int(input())
# size_l = int(input())
# random_int(n,size_l,minint,minint)
# print(n)





#2

# start =int(input('starting '))
# def chislo_fib(num):
#     start,b=0,1
#     for i in range(num):
#         yield start
#         start, b=b, start + b
# print(list(chislo_fib(start)))



# 3 В строке изменить последовательность слов на обратную
#   Напишите функцию, которая принимает строку слов и возвращает строку с теми же словами,
#   но идущими в обратном порядке.




# def reverse_text(text):
#     text=text.split()
#     text.reverse()
#     return ' '.join(text)

# print(reverse_text(input('Введите тест: ')))



from random import randint
start = int(input('starting: ')) # 10
def chislo_fib(num): # 10
    start, b = 1, 1
    for i in range(num): # 10
        yield start
        start, b =b, start + b
        
 
print(list(chislo_fib(start))) # 10
def fibonaci2():
    fib1 = fib2 = 1
    n = int(input('Введите номер элемента последовательности: '))
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
        
fibonaci2()