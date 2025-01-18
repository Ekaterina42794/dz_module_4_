'''
# Для исправления вашего кода, поменяйте местами цикл и условие.
# if 1 <= new_floor <= self.number_of_floors:
# for floor in range(1, new_floor + 1):
'''

print()
print('Задача "Developer - не только разработчик":')
print()


class House:
    def __init__(self, name, number_of_floors):  # имя и кол-во этажей всего
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):  # номер этажа(int), на который нужно приехать
        self.go_to = int(new_floor)
        if self.number_of_floors >= self.go_to>=0:
            for i in range(1, self.go_to + 1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h1.go_to(5)
print(h1.name,',',h1.go_to,'из', h1.number_of_floors)
print('___')

h2 = House('Домик в деревне', 2)
h2.go_to(5)
print(h2.name,',',h2.go_to,'из', h2.number_of_floors)
print('___')

h3=House('ЖК Эльбрус', 30)
h3.go_to(-5)
print(h3.name,',',h3.go_to,'из', h3.number_of_floors)