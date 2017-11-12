# coding=utf-8
# Napisz program który w parametzre otrzymuje dwie nazwy plików. Program ma wcztać jeden plik,
# zaszyfrować go szyfrem cezara i zapisać pod inną nazwą z parametru.

import sys


def newSymbol(symbol, shift, firstLetter):
    position = (ord(symbol) + shift - firstLetter) % 26 + firstLetter + 1
    chrct = chr(position)
    return chrct


with file(sys.argv[1]) as f, open(sys.argv[2], "r+") as f2:
    shifting = 3
    for line in f:
        for character in line:
            if 97 <= ord(character) <= 122:
                f2.write(newSymbol(character, shifting, 96))
            elif 65 <= ord(character) <= 90:
                f2.write(newSymbol(character, shifting, 64))
            else:
                f2.write(character)
