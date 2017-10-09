# coding=utf-8
int_1 = input("Podaj pierwszą liczbę: ")
int_2 = input("Podaj drugą liczbę: ")
int_3 = input("Podaj trzecią liczbę: ")
output = "Największa liczba to: "
if int_1 > int_2:
    if int_1 > int_3:
        print output + int_1
    else:
        print output + int_3
elif int_2 > int_3:
        print output + int_2
else:
    print output + int_3
