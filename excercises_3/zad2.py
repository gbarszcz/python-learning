# coding=utf-8
# Zaimplementuj dwie klasy, Punkt2D i rozszerzającą ją Punkt3D.
# Każda z klas ma mieć możliwość obliczania odległości między dwoma punktami.
from math import sqrt


class Punkt2D:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc(self, other):
        return sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2)


class Punkt3D(Punkt2D):
    y = None

    def __init__(self, x, y, z):
        Punkt2D.__init__(self, x, y)
        self.z = z

    def odleglosc(self, other):
        return sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2)


punkt1 = Punkt2D(0, 0)
punkt2 = Punkt2D(1, 1)
print punkt1.odleglosc(punkt2)

punkt3d1 = Punkt3D(0, 0, 0)
punkt3d2 = Punkt3D(1, 1, 1)
print punkt3d1.odleglosc(punkt3d2)
