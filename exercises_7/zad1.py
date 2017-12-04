# coding=utf-8
# Napisz program, który kompiluje kod C++, a następnie uruchamia go i sprawdza czy jego działanie nie kończy się błędem.

import subprocess
import sys

proces = subprocess.call(
    ["g++", sys.argv[1]], shell=True)
if str(proces).endswith('0'):
    print "program zakonczyl sie bledem"
else:
    print "program nie zakonczyl sie bledem"