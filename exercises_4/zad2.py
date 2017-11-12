# -||- zad1.py, ale napis jest wczytywany z pliku. nazwa pliku jest podana jako parametr


def funkcja(filename):
    slownik = {}
    with file(filename) as f:
        inp = f.read().split('\n')
    for i in range(0, len(inp)):
        element = inp[i].split(': ')
        slownik[element[0]] = element[1]
    return slownik


print funkcja("test_2.txt")
