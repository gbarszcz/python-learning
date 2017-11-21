# coding=utf-8
# Sprawdź poprawność adresów IPv4 wczytywanych z pliku
import sys
import re


pattern = re.compile("(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])")
with file(sys.argv[1]) as f, open(sys.argv[2], "r+") as f2:
    for line in f:
        result = pattern.match(line)
        if result:
            f2.write(line + "\t: poprawny" + "\n")
        else:
            f2.write(line + "\t: błędny" + "\n")