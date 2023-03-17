k = int(input())

distances = [int(x) for x in input().split(' ')]

possible_distances = set()

sum_of_elements = sum(distances)

for x in distances:
    possible_distances.add(sum_of_elements - x)

print(len(possible_distances))
possible_distances = sorted(possible_distances)
for x in possible_distances:
    print(x, end=' ')
