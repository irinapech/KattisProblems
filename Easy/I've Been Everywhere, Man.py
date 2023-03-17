number_of_cases = int(input())
for _ in range(number_of_cases):
    number_of_cities = int(input())
    cities = {input(): 1 for _ in range(number_of_cities)}
    print(len(cities))