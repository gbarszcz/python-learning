# coding=utf-8
# Napisz program który pobiera plik html i zapisuje go na dysku.

import urllib2

response = urllib2.urlopen('http://python.org/')
html = response.read()
with open("test_4.txt", 'wb') as f:
    f.write(html)

