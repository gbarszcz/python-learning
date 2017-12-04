# coding=utf-8
# tworzenie procesów

import subprocess
import os

out1 = subprocess.call(
    ["echo", "Hello world!"], shell=True)

print out1
#
# out1 = subprocess.check_output()
#        ("echo", "Hello world!"), shell=True])
try:
    out2 = subprocess.check_call(
       ("ech", "Hello world!"), shell=True)
except subprocess.CalledProcessError as ex:
    print ex
print out2

with open(os.devnullm, 'w') as devnull:
    out3 = subprocess.check_call(
       ("ech", "Hello world!"), stderr=devnull, shell=True)

