# napisz generator ktory bedzie zwracal nazwy kolejnych plikow z katalogu *os.listdir()) o podanym rozszerzeniu
# rozszerzenie oraz sciezke podaje uzytkownik w konsoli
import os

katalog = raw_input("Podaj katalog: ")
rozszerzenie = raw_input("Podaj rozszerzenie: ")
pliki_i_katalogi = os.listdir(katalog)


def generator(lista):
    length = len(lista)
    for i in range(0, length):
        if lista[i].endswith(rozszerzenie):
            yield lista[i]


for x in generator(pliki_i_katalogi):
    print x