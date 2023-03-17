number_of_sets = int(input())

for set_number in range(number_of_sets):
    set_number, number_of_days = [int(x) for x in input().split(' ')]
    number_of_candles = sum([i + 1 for i in range(number_of_days)]) + number_of_days
    print(set_number, number_of_candles)