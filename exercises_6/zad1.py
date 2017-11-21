# coding=utf-8
# Napisz funkcję, która pobierze od użytkownika liczbę i wyświetli jej pierwiastek.
# Obsłuż wszystkie wyjątki, które mogą wystąpić w wyniku działania programu.
from math import sqrt

try:
    liczba = input("Podaj liczbę: ")
    pierwiastek = sqrt(liczba)
except (NameError, SyntaxError) as ex:
    print ex
    print 'Wartość powinna być liczbą.'
except ValueError as ex:
    print ex
    print 'Podano złą wartość. Liczba powinna być dodatnia.'
except ZeroDivisionError as ex:
    print ex
    print "Liczby nie powinno się dzielić przez 0"
else:
    print pierwiastek

