# coding=utf-8
# Napisz prostą bazę danych kolekcji domowych (książki, płyty itd.).
# Program ma mieć możliwość dodania nowego obiektu do bazy, wyszukiwania po dowolnym filtrze,
# w tym wyświetlania całej kolekcji, kolekcji danego typu itp.,
# usuwania elementów z bazy i modyfikowania już istniejących.


class Kolekcja:
    elementy = []

    def __init__(self):
        self.elementy = []

    def dodaj(self, other):
        self.elementy.append(other)

    def dodajKolekcje(self, other):
        self.elementy.extend(other.elementy)

    def usun(self, other):
        self.elementy.remove(other)

    def znajdz(self, other):
        for i in range(0, len(self.elementy)):
            if self.elementy[i] == other:
                return other
        return None

    def wyswietl(self):
        for i in range(0, len(self.elementy)):
            print self.elementy[i]


class Film:
    tytul = None
    rok = None
    rezyser = None

    def __init__(self, tytul, rok, rezyser):
        self.tytul = tytul
        self.rok = rok
        self.rezyser = rezyser

    def __str__(self):
        return "Tytul %s\nRok %d\nRezyser %s\n" % (self.tytul, self.rok, self.rezyser)


class Ksiazka:
    tytul = None
    rok = None
    autor = None

    def __init__(self, tytul, rok, autor):
        self.tytul = tytul
        self.rok = rok
        self.autor = autor

    def __str__(self):
        return "Tytul %s\nRok %d\nAutor %s\n" % (self.tytul, self.rok, self.autor)


kolekcjaGlowna = Kolekcja()
kolekcjaFilmow = Kolekcja()
kolekcjaKsiazek = Kolekcja()

film1 = Film("Pulp Fiction", 1994, "Quentin Tarantino")
film2 = Film("The Avengers", 2012, "Joss Whedon")
film3 = Film("Citizen Kane", 1941, "Orson Welles")

ksiazka1 = Ksiazka("Harry Potter (kolekcja)", 1997, "J. K. Rowling")
ksiazka2 = Ksiazka("Władca Pierścieni (kolekcja)", 1954, "J. R. R. Tolkien")
ksiazka3 = Ksiazka("Idiota", 1869, "Fiodor Dostojewski")

kolekcjaFilmow.dodaj(film1)
kolekcjaFilmow.dodaj(film2)
kolekcjaFilmow.dodaj(film3)
kolekcjaFilmow.wyswietl()
print("\n")

kolekcjaKsiazek.dodaj(ksiazka1)
kolekcjaKsiazek.dodaj(ksiazka2)
kolekcjaKsiazek.dodaj(ksiazka3)
kolekcjaKsiazek.wyswietl()
print("\n")

kolekcjaGlowna.dodajKolekcje(kolekcjaFilmow)
kolekcjaGlowna.dodajKolekcje(kolekcjaKsiazek)
kolekcjaGlowna.wyswietl()