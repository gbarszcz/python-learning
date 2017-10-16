# coding=utf-8
# zaimplementuj funkcję, która w argumencie otrzymuje funkcję logiczną oraz listę
# i zwraca listę elementów spełniających warunek podany w przekazywanej funkcji


def logiczna(lista):
    lista_ret = []
    for i in range(0, len(lista)):
        if lista[i] > 0:
            lista_ret.append(lista[i])
    return lista_ret


def funkcja(funkcja_arg, lista_arg):
    return funkcja_arg(lista_arg)


lista = [4, 5, 2, 421, -43, 324, -353.32, 23.432]
print funkcja(logiczna, lista)