from typing import NamedTuple
point = (3, 5)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Person(NamedTuple):
    name: str
    surname: str
    date: str
    country: str


Megan = Person('Megan', 'Jones', '1998-07-16', 'Bolivia')

# print(Megan.surname)

points = [...]


keywords_for_client = ['Банк', 'Номер телефона:', 'банк', 'номер телефона', 'ФИО:']
for i in keywords_for_client:
    if i in 'Банк получателя и Номер телефона:':
        print(i)
