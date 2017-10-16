# coding=utf-8
# for i in range(97, 123):
#     print chr(i)
# for i in range(65, 91):
#     print chr(i)

# for i in range(97, 123):
#     ch = i - 32
#     print chr(i)
#     print chr(ch)

# user_input = input("Podaj co ile liter ma się wyświetlać alfabet: ")
# for i in range(97,123,user_input):
#     print chr(i)

# sortowanie
user_numbers_count = input("Podaj ilość liczb: ")
user_sort = raw_input("Podaj kierunek sortowania (R - rosnąco/M - malejąco): ")
user_range_start = input("Podaj początek zakresu liczb: ")
user_range_end = input("Podaj koniec zakresu liczb: ")
user_numbers = [0] * user_numbers_count
for i in range(0, user_numbers_count):
    user_numbers[i] = input("Podaj liczbę: ")

if user_sort == "R":
    user_numbers = sorted(user_numbers, reverse=False)
elif user_sort == "M":
    user_numbers = sorted(user_numbers, reverse=True)

for i in range(0, user_numbers_count):
    if (user_numbers[i] >= user_range_start) and (user_numbers[i] <= user_range_end):
        print user_numbers[i]
