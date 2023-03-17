points = []
for _ in range(5):
    points.append(sum([int(x) for x in input().split(' ')]))
print(points.index(max(points)) + 1, max(points), end=' ')