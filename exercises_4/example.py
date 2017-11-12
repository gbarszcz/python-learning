# skrypt jezyka python nalezy zapisac z rozszerzeniem *.py
import sys

print sys.argv

#slowniki // mapy
slownik = {
    'ki' : 'gi',
    2 : [1,2,3],
    (4,3,2) : 4
}

slownik['slownik'] = slownik
print slownik['brak'] # rzuca wyjatkiem, wiec bezpieczniej uzywac te ponizej :
print slownik.get('brak')
print slownik.get('brak', 'wartosc')

for z in slownik.items():
    print z

# napisy
napis1 = "abc"
napis2 = 'abc'
napis3 = """a
b"""
napis4 = '''a
b'''

# napisy sa niemodyfikowalne; nastepujacy kod jest nieoptymalny
# ...

# join pozwala na laczenie napisow z wykorzystaniem separatora
# split dzieli napisy

# pliki

