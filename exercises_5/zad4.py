# coding=utf-8
# Walidacja PESEL
import re


def dataurodzenia(pesel):
    miesiac = pesel[2]
    dzien = pesel[4] + pesel[5]
    if miesiac == "0" or miesiac == "1":
        rok = "19"
    elif miesiac == "2" or miesiac == "3":
        miesiac = str(int(miesiac) - 20)
        rok = "20"
    elif miesiac == "4" or miesiac == "5":
        miesiac = str(int(miesiac) - 40)
        rok = "21"
    elif miesiac == "6" or miesiac == "7":
        miesiac = str(int(miesiac) - 60)
        rok = "22"
    elif miesiac == "8" or miesiac == "9":
        miesiac = str(int(miesiac) - 80)
        rok = "18"
    else:
        raise Exception("Podano zły format daty")
    miesiac += pesel[3]
    rok += pesel[0] + pesel[1]
    return "%s-%s-%s" % (dzien, miesiac, rok)


pesel = raw_input("Podaj numer PESEL: ")
pattern = re.compile("[0-9]{2}"  # rok
                     "((0[1-9])|"  # miesiac
                     "(([13579])[0-2]|"  # miesiac part 2
                     "([02468])[1-9]))"  # miesiac part 3
                     "((0[1-9])|"
                     "([1-2][0-9])|"
                     "(3[0-1]))"
                     "[0-9]{5}")

result = re.match(pattern, pesel)

if result:
    sumakontrolna = (9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + int(pesel[3]) + 9 * int(pesel[4])
                     + 7 * int(pesel[5]) + 3 * int(pesel[6]) + int(pesel[7]) + 9 * int(pesel[8]) + 7 * int(
        pesel[9])) % 10
    if str(sumakontrolna) == pesel[10]:
        plec = None
        if int(pesel[9]) % 2 == 0:
            plec = "K"
        else:
            plec = "M"
        print "Data urodzenia: %s, płeć: %s" % (dataurodzenia(pesel), plec)
    else:
        print "Podano zły numer PESEL"
else:
    print "Podano zły numer PESEL"
