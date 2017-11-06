# coding=utf-8
# Zaimplementuj klasę "liczbaZespolona". Klasa ma mieć możliwość
# dodawania, odejmowania, mnożenia, dzielenia oraz przypisywania z wykorzystaniem standardowych operatorów.
# Dodatkowo ma posiadać funcję "modul" obliczającą moduł liczby zespolonej oraz możliwość
# porównywania go również przy pomocy standardowych operatorów logicznych.
# Po przekazaniu obiektu do funkcji print ma ona zostać wyświetlona na ekranie.
from math import sqrt


class liczbaZespolona:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __str__(self):
        return "%f + %fi" % (self.x, self.y)

    def __add__(self, other):
        return liczbaZespolona(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return liczbaZespolona(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return liczbaZespolona(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return liczbaZespolona(self.x / other.x, self.y / other.y)

    def modul(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def porownajModul(self, other):
        return self.modul() > other.modul()


a = liczbaZespolona(2, 3)
b = liczbaZespolona(2, 3)

print a
print b
print a.modul()
print b.modul()
print a.porownajModul(b)
