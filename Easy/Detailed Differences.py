n = int(input())

for i in range(n):
    line1 = str(input())
    line2 = str(input())
    print(line1)
    print(line2)
    for j in range(len(line1)):
        print('.' if line1[j] == line2[j] else '*', end="")
    print('\n')