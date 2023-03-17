n = int(input())
cities = []
count = 0
for i in range(n):
    cities.append([int(x) for x in input().split(' ')])
    for j in range(n):
        if cities[i][j] != -1:
            count += 1
print(count)
for i in range(n):
    for j in range(n):
        if cities[i][j] != -1:            
            print(f"{i + 1} {j + 1} {cities[i][j]}")