# # wyjatki
# slownik = {}
# print slownik['test'] #KeyError
#
# print 1/0
#
# lista = []
# print lista[2]


# obsluga wyjatkow
def divide(x, y):
    try:
        result = x/y
    except (ZeroDivisionError, TypeError) as ex:
        print ex
    else:
        print 'Brak wyjatku'
        return result
    finally:
        print 'Koniec funkcji'


print divide(2.0, 4.0)
print divide(1, 0)
print divide(1, 'string')


class Wyjatek(Exception):
    pass


try:
    raise Wyjatek('Wystapil wyjatak')
except Wyjatek as w:
    print w


# virtualenv

# http
import urllib2

response = urllib2.urlopen('http://python.org/')
html = response.read()
print html

# parsowanie xml
from xml.dom import minidom

doc = minidom.parse("test.xml")
elements = doc.getElementsByTagName("element")
for el in elements:
    elementId = el.getAttribute("id")
    par = el.getElementsByTagName("par")[0]
    print "id %s, par %s" % (elementId, par.firstChild.data)

