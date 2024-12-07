#Создайте модули fake_math и true_math в которых создайте функции отвечающие за деление, но разными способами.
#В true_math создайте функцию divide, которая принимает два параметра first и second.
''' Функция должна возвращать результат деления first на second,
но когда в second записан 0 - возвращать бесконечность.
'''
#Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)

from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second


if __name__ == "__main__":
# Чтобы ф-ции не вызывались при импорте, в родных модулях их нужно оборачивать в if __name__ == "__main__":
    print(divide(69, 3))
    print(divide(3, 0))
