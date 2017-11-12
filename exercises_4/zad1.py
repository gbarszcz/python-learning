# napisz funkcje ktora przyjmuje napis w formacie:
# '''k1: w1
# k2: w2
# k3: w3'''
# i zwraca slownik w postaci: 'k1': 'w1', 'k2': 'w2', 'k3': 'w3'


def funkcja(string_input):
    slownik = {}
    string_input = string_input.split('\n')
    for i in range(0, len(string_input)):
        element = string_input[i].split(': ')
        slownik[element[0]] = element[1]
    return slownik


inp = '''k1: w1
k2: w2
k3: w3'''
print funkcja(inp)
