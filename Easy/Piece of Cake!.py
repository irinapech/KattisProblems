side_length, horizontal_cut, vertical_cut = [int(x) for x in input().split(' ')]
height = 4
print(max(side_length - horizontal_cut, horizontal_cut) * max(side_length - vertical_cut, vertical_cut) * height)