number_of_cases = int(input())

for k in range(number_of_cases):
    rows, columns = [int(x) for x in input().split(' ')]
    picture = [input() for _ in range(rows)]
    print("Test ", k + 1)
    for i in range(rows - 1, -1, -1):
        print(picture[i][::-1])