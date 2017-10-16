    # coding=utf-8
# listy składana

liczby = range(0,20)

print liczby

kwadraty1 = [x*x for x in liczby]
kwadraty = [(x, x*x) for x in liczby]

print kwadraty


# funkcje wyższego rzędu
def f1(n):
    def f2(x):
        return n - x
    return f2


def f2(a,b):
        print a(b)


rec = f1(5)
f2(rec, 0)
print rec(10)


# wyrażenia lambda
kwadrat = lambda x: x*x
kwadrat2 = lambda x, y: x*y
print kwadrat(5)
print kwadrat2(2, 5)


# generatory
def generator(n):
        while n:
            print "Generator stop: %d" % n
            yield n
            print "Generator start: %d" % n
            n -= 1


# for x in generator(5):
#     print "Wywolanie %d" % x

x = generator(5)
print x.next()
print x.next()
