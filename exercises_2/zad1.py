# coding=utf-8
# napis i jego długość jako krotka w liście składanej


def lista_skladana(lista):
    krotka = [(slowo, len(slowo)) for slowo in lista.split()]
    return krotka


print lista_skladana('ala ma kota')
