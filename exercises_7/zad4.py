# coding=utf-8
# Napisz klasę implementację własnej obiektowej listy. Program powinien posiadać podstawowe operacje,
# takie jak dodawanie, usuwanie, sortowanie, posiadać przeciążone operatory i zgłaszać niezbędne wyjątki.


class Element:
    _name = None
    _id = None

    def __init__(self, _name, _id):
        self._name = _name
        self._id = _id

    def __repr__(self):
        return self._name + " " + str(self._id)


class Lista:
    lista = None

    def __init__(self):
        self.lista = []

    def __str__(self):
        return str(self.lista)

    def dodaj(self, obiekt):
        self.lista.append(obiekt)

    def znajdz(self, _id):
        for element in self.lista:
            try:
                if type(element._id) == type(_id) and element._id == _id:
                    return element
            except TypeError as ex:
                print ex

    def usun(self, _id):
        element = self.znajdz(_id)
        try:
            self.lista.remove(element)
        except ValueError as ex:
            print "Lista nie posiada takiego elementu. " + ex.message

    def sortuj(self):
        self.lista.sort(key=lambda x: x._id)


lista = Lista()
lista.usun(2)
lista.dodaj(Element("nazwa", 2))
lista.dodaj(Element("nazwa2", 134))
lista.dodaj(Element("nazwa3", -23))
print str(lista)
lista.sortuj()
print "---------------"
print str(lista)
