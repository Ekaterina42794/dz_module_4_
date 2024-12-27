#Цель: понять как работают базовые магические методы на практике.
# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче
# "Атрибуты и методы объекта".
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

class House:
    def __init__(self, name, number_of_floors):  # имя и кол-во этажей всего
        self.name = name
        self.number_of_floors = number_of_floors

    # def go_to(self, new_floor):  # номер этажа(int), на который нужно приехать
    #     self.go_to = int(new_floor)
    #     for i in range(1, self.go_to + 1):
    #         if self.number_of_floors >= self.go_to >= 0:
    #             print(i)
    #         else:
    #             print('Такого этажа не существует')
    #             break

    def __len__(self):  # - должен возвращать кол-во этажей здания self.number_of_floors.
       return self.number_of_floors

    def __str__(self):  # - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
        return f'"Название: {self.name}, кол-во этажей: {self.number_of_floors}"'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print()
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))






# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20
