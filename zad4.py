# coding=utf-8
# ciąg Fibonacciego

user_input = input("Podaj ilość liczb: ")

x = 0
y = 1
print x
print y
for i in range(0, user_input):
    z = x + y
    print z
    x = y
    y = z