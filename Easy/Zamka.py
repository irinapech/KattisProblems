def sum_digits(number):
    sum = 0
    while number != 0:
        sum += number%10
        number = number//10
    return sum

l = int(input())
d = int(input())
x = int(input())

max = 0
min = 9999

for i in range(l, d + 1):
    if sum_digits(i) == x and i < min:
        min = i
        
    if sum_digits(i) == x and i > max:
        max = i

print(min, max)