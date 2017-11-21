# coding=utf-8
# Napisz klasę, która będzie przechowywać adresy e-mail. Konstruktor ma przyjmować napis będący adresem.
# Jeżeli zostanie podany niewłaściwy adres, konstruktor ma zgłaszać wyjątek odpowiedniej klasy.
# Walidacja adresu ma być realizowana przy pomocy wyrażeń regularnych.
import re


class Email:
    adres = None

    def __init__(self, adr):
        # http://www.ex-parrot.com/~pdw/Mail-RFC822-Address.html
        pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        result = pattern.match(adr)
        try:
            if result:
                self.adres = adr
            else:
                raise ValueError('Podano niewlasciwy adres ' + adr)
        except ValueError as ex:
            print ex


email = Email("email")
email2 = Email("email@")
email3 = Email("email@sadsad")
email4 = Email("email@sadsad.sad")