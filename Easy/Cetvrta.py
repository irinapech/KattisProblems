cost_per_square = float(input())
number_of_lawns = int(input())
sum_of_squares = 0
for _ in range(number_of_lawns):
    w, l = [float(x) for x in input().split(' ')]
    sum_of_squares += w * l
print(f"{cost_per_square * sum_of_squares:6f}")