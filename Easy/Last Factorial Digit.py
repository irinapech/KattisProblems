def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

number_of_cases = int(input())
for _ in range(number_of_cases):
    print(factorial(int(input())) % 10)