# coding=utf-8
# Napisz program który w parametrze otrzymuje nazwę pliku lub znak '-' oraz ciąg znaków. Program ma
# wczytać plik i wyświelić te linie, w których znajduje się podany ciąg znaków. Jeżeli zamiast nazwy pliku jest znak
#  '-', to linie są wczytywane ze standardowego wejścia. Pusta linia kończy wczytywanie.

import sys

if sys.argv[1] == '-':
    line = raw_input()
    while line != "":
        if sys.argv[2] in line:
            print line
        line = raw_input()

else:
    with file(sys.argv[1]) as f:
        for line in f:
            if sys.argv[2] in line:
                print line
