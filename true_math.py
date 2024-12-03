#Создайте модули fake_math и true_math в которых создайте функции отвечающие за деление, но разными способами.
#В true_math создайте функцию divide, которая принимает два параметра first и second.
''' Функция должна возвращать результат деления first на second,
но когда в second записан 0 - возвращать бесконечность.
'''
#Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)

from math import inf

def divide(first, second):
    if second != 0:
        a = first / second
    else:
        a = inf
    print(a)

divide(49, 7)
divide(15, 0)
