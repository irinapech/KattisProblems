number = [int(digit) for digit in input()]
while len(number) > 1:
    product = 1
    for digit in number:
        if digit != 0:
            product *= digit
    number = [int(digit) for digit in str(product)]
print(number[0])