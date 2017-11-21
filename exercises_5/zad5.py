# coding=utf-8
# Napisz program, który magazynuje informacje oposiadanych książkach (tytuł, numer ISBN, autor).
# Program ma mieć możliwość dodawania, usuwania, wyświetlania pozycji oraz zapisu stanu programu
# do pliku jak i możliwość jego wczytania. Ścieżkę do pliku podajmy w parametrze uruchieniowym skryptu.

import sys
import pickle


class Ksiazka:
    def __init__(self, t, a, i):
        self.tytul = t
        self.autor = a
        self.isbn = i

    tytul = None
    autor = None
    isbn = None

    def __repr__(self):
        return "Tytul: %s\nAutor: %s\nISBN: %d\n" % (self.tytul, self.autor, self.isbn)


class Katalog:
    def __init__(self):
        self.ksiazki = {}

    ksiazki = {}

    def wczytaj(self):
        with file(sys.argv[1]) as f:
            self.ksiazki = pickle.load(f)
        print "Wczytano plik " + sys.argv[1] + "."
        print self.ksiazki

    def dodaj(self, ksiazka):
        self.ksiazki[ksiazka.isbn] = ksiazka

    def zapisz(self):
        with open(sys.argv[1], 'wb') as f:
            pickle.dump(self.ksiazki, f)

    def usun(self, isbn):
        self.ksiazki.pop(isbn, None)

    def wyswietl(self):
        print self.ksiazki.items()


katalog = Katalog()
ksiazka1 = Ksiazka("Tytul 1", "Autor 1", 123)
katalog.dodaj(ksiazka1)
print "Katalog: "
katalog.wyswietl()
katalog.zapisz()
katalog1 = Katalog()
katalog1.wczytaj()
print "Katalog1 po wczytaniu z pliku: "
katalog1.wyswietl()
katalog1.ksiazki[123].autor = "Autor 2"
print "Katalog1 po zmianie: "
katalog1.wyswietl()
print "Katalog: "
katalog.wyswietl()

ksiazka2 = Ksiazka("Tytul 2", "Autor 2", 456)
katalog.usun(123)
print "Katalog po usunieciu 123"
katalog.wyswietl()
katalog.dodaj(ksiazka2)
print "Katalog po dodaniu 456: "
katalog.wyswietl()
katalog.zapisz()
