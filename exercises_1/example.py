print('Hello world!')
# data = raw_input('Wprowadz dane')  # wczytuje zawsze jako string
# data2 = input('Wprowadz')
# print(data)
# print(data2)
#
# data3 = int(data) + data2
# print(data3)


def suma(a, b):
    return a + b


print(suma(2, 4))
print(suma('a', 'b'))

a = 4
b = 2

if a > b:
    print("wieksze")
elif a == b:
    print("rowne")
else:
    print("mniejsze")


li = ['a', 'v', 'c', 'd']
for i in range(len(li)):
    print li[i]

i = 0
while i < 5:
    print i
    i = i + 1

lista = [1, 2.32, "str", 4]
print lista[1]

krotka = {1, 4, "erew"}
print krotka

lista[1] = "ree"
# krotka[0] = 0 # nie mozna edytowac krotki