multiply_by = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
number = [int(x) for x in input() if x != '-']
sum_of_changed_digits = sum([multiply_by[i] * number[i] for i in range(10)])
print(1 if sum_of_changed_digits % 11 == 0 else 0)