# coding=utf-8
# korzystając z list składanych napisz funkcję która stworzy n elementów ciągu Fibonacciego,
# liczba n jest podawana z konsoli


def fib_ls(n):
    lista = []
    x = 0
    y = 1
    lista.append((0, x))
    lista.append((1, y))
    for i in range(0, n):
        z = x + y
        lista.append((i+2, z))
        x = y
        y = z
    return lista


ilosc = input("Podaj liczbę elementów ciągu: ")
print fib_ls(ilosc)
