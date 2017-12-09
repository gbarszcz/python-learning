# coding=utf-8
# Wyszukiwarka internetowa. Program wczytuje przygotowaną listę stron i wyszukuje 5 najczęściej
# pojawiających się na niej słów. Po wpisaniu hasła (jedno słowo) wyświetla link lub informację,
# że program nie znalazł żadnego wyniku.
import operator
import urllib2
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    page = None
    start = None
    d = {}

    def handle_starttag(self, tag, attrs):
        self.start = tag

    def handle_data(self, data):
        if self.start != 'script':
            for word in data.split(' '):
                word = word.strip()
                if word != '':
                    try:
                        value = self.d[word.lower()]
                        value += 1
                        self.d[word.lower()] = value
                    except KeyError as ex:
                        self.d[word.lower()] = 1

    def __repr__(self):
        print self.d


pages_list = {
    'http://python.org/',
    'http://moria.umcs.lublin.pl/link/',
    'http://square.github.io/retrofit/',
    'http://www.zdnet.com/',
    'http://www.openwall.com/john/doc/RULES.shtml'
}

dictionary = {}
parser = MyHTMLParser()

for page in pages_list:
    response = urllib2.urlopen(page)
    html = response.read()
    parser.d = {}
    parser.page = page
    parser.feed(html)
    new_dict = dict(sorted(parser.d.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    for key, value in new_dict.iteritems():
        dictionary[key] = page


data = raw_input("Podaj słowo: ")
address = dictionary.get(data.lower())
if address is None:
    print "Word was not found."
else:
    print address
