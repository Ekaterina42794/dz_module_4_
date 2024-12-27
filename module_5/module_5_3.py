'''Перегрузка операторов"
Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.

Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
Необходимо дополнить класс House специальными методами:'''


class House:
    def __init__(self, name, number_of_floors):  # имя и кол-во этажей всего
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):  # - должен возвращать кол-во этажей здания self.number_of_floors.
        return self.number_of_floors

    def __str__(self):  # - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
        return f'"Название: {self.name}, кол-во этажей: {self.number_of_floors}"'
#   Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики
#  перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
#  isinstance(other, int):   - other указывает на объект типа int.
#  isinstance(other, House): - other указывает на объект типа House.
#  isinstance(obj, class_or_tuple, /)

    def __eq__(self, other):  # - должен возвращать True, если количество этажей одинаковое у self и у other
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self,
                value):  # (+) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    #  - работают так же как и __add__ (возвращают результат его вызова)
    #  Методы __iadd__ и __radd__ не обязательно описывать заново, достаточно вернуть значение вызова __add__
    def __iadd__(self, value):  # (+)
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):  # (+)
        return self.__add__(value)

    def __gt__(self, other):  # должны присутствовать в классе и возвращать результаты сравнения по (>)
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):  # должны присутствовать в классе и возвращать результаты сравнения по (>=)
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):  # должны присутствовать в классе и возвращать результаты сравнения по (<)
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other): #должны присутствовать в классе и возвращать результаты сравнения по (<=)
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other): #должны присутствовать в классе и возвращать результаты сравнения по (!=)
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print()

# __str__
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__