dice1, dice2 = [int(x) for x in input().split(' ')]

sums = dict()
for i in range(1, dice1 + 1):
    for j in range(1, dice2 + 1):
        if i + j in sums:
            sums[i + j] += 1
        else:
            sums[i + j] = 1

max_sum = max(sums.values())
for a_sum in sums:
    if max_sum == sums[a_sum]:
        print(a_sum)