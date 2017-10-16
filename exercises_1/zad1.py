# coding=utf-8
name = raw_input("Podaj imię: ")
surname = raw_input("Podaj nazwisko: ")
age = input("Podaj swój wiek: ")
output = "Cześć " + name + " " + surname + ", jesteś "
if age >= 18:
    print output + "pełnoletni"
else:
    print output + "niepełnoletni"
