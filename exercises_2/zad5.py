# coding=utf-8
# zaimplementu jfunkcję która przyjmuje listę punktów na płaszczyźnie w postaci krotek oraz punkt kontrolny.
# funkcja ma zwrócić listę krotek w postaci (odleglosc, punkt(x,y)) w kolejnosci od najblizszego do najdalszego
# pomiedzy elementami z listy a punktem kontrolnym
# wykorzystanie lambd

from math import sqrt

odleglosc = lambda a, b: sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def funkcja(krotki, punkt_kontrolny):
    lista = [(odleglosc(krotka, punkt_kontrolny), (krotka[0], krotka[1])) for krotka in krotki]
    return sorted(lista, reverse=False)


lista = [(0, 1), (5, 2), (0, 0), (3, 19)]
print funkcja(lista, (0, 0))
