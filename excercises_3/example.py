class klasa:
    def funkcja(self, zmienna):
        print "uruchomienie metody " + zmienna
        self.funkcja2()
    def funkcja2(self):
        print "funkcja 2"


obiekt = klasa()
obiekt.funkcja("1")


class Klasa2:
    zm1 = None
    __zm2 = None

    def ustaw1(self, zmienna):
        zm1 = zmienna

    def ustaw2(self, zmienna):
        __zm2 = zmienna


class Samochod:
    Kolor = None

    def setKolor(self, kolor):
        self.Kolor = kolor


class Osobowy(Samochod):
    Marka = "Mercedes"


ob = Osobowy()
ob.setKolor("czerwony")
print("Kolor %s marka %s" % (ob.Kolor, ob.Marka))


class A:

    def __init__(self, zmienna):
        self.zmienna = zmienna

    def __add__(self, other):
        return self.zmienna + other.zmienna


a = A(3)
b = A(2)

print a+b
