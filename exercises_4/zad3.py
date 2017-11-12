# coding=utf-8
# napisz program, ktory w parametrze przyjmuje nazwe pliku.
# Program ma stworzyć słownik w którym zostanie zliczona ilść wystąpień danego słowa we wczytanym tekście


def funkcja(filename):
    slownik = {}
    with file(filename) as f:
        for line in f:
            for word in line.split():
                if word in slownik:
                    val = slownik.get(word)
                    val += 1
                    slownik[word] = val
                else:
                    slownik[word] = 1
    return slownik


print funkcja("test_3.txt")
