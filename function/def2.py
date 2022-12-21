from functions import calculator, len2

# a = input('''
# +
# -
# *
# /
# ''')
# n1 = int(input(('n1: ')))
# n2 = int(input(('n2: ')))
# print(calculator(a, n1, n2))
# d = 2345
# b = 'hello world'
# a = int(input('a: '))
# q = len2(d)
# print(len2(a))
#-----------------------------------------

def randoom_nums(num_list : list, x:int, y:int, size_list:int):
    from random import randint
    for i in range(size_list):
        num_list.append(randint(x,y))

