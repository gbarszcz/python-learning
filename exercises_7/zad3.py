# coding=utf-8
# Napisz program posiadający funkcję która oblicza rozkład liczby podanej w argumencie na czynniki pierwsze i zwraca
# wynik w postaci par krotek [(p1,w1), (p2,w2)] takich, że n = p1^(w1) * p2^(w2)...
# Przykład:
# rozklad(756)
# [(2,2), (3,3}, (7,1)]


def rozklad(liczba):
    lista = []
    dzielnik = 2
    l = liczba
    ilosc = 0
    while l > 1:
        while l%dzielnik == 0:
            ilosc = ilosc + 1
            krotka = (dzielnik, ilosc)
            if ilosc > 1:
                lista.pop()
            lista.append(krotka)
            l = l/dzielnik
        ilosc = 0
        dzielnik = dzielnik + 1
    return lista


print rozklad(756)
