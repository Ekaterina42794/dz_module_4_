#Создайте модули fake_math и true_math в которых создайте функции отвечающие за деление, но разными способами.
# В fake_math создайте функцию divide, которая принимает два параметра first и second.

# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать строку 'Ошибка'.

def divide(first,second):
    if second != 0:
        a = first / second
        print(a)
    else:
        print('Ошибка')





divide(69,3)
divide(3,0)

