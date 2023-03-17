number_of_matches, side1, side2 = [int(x) for x in input().split(' ')]
import math
diagonal = math.sqrt(side1**2 + side2**2)
for _ in range(number_of_matches):
    length = int(input())
    if length <= side1 or length <= side2 or length <= diagonal:
        print('DA')
    else:
        print('NE')
