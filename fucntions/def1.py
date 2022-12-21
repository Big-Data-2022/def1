# FUNCTIONS - функции

# a = 5
# b = 10
# print(a + b)

# def - объявить функцию 
# def function( arguments):
    #return 

# def main(x, y):
#     return x + y
    
# print(main(99, 90))

def len1(a):
    n = 0
    try:
        a = str(a)
        for i in a:
            n += 1
        return n
    except:
        print('ONLY STR AND INT ARGUMENTS!!!!')


# b = 'qwerzsfdfsfdasdas'
# print(len1(b))


# def adi(a, b = 45):  # a - обязательный аргумент  b - необязательный аргумент
#                     # если мы ничего не передаем в b то он будет равен 1 по умолчанию
#     return b - a
# print(adi(14))

# калькулятор принмает 3 аргумента
def calculator(oper, x = 1, y = 1):  # по умолчанию х и у равны 1
    if oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    elif oper == '*':
        return x * y
    elif oper == '/':
        return x / y
    return 'choose another option - "+", "-", "*", "/"'
    
