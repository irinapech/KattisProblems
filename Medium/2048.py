grid = []
for _ in range(4):
    grid.append([int(x) for x in input().split(' ')])

def move_numbers_right_or_left(input_list, direction):
    for i in range(4):
        while 0 in input_list[i]:
            input_list[i].remove(0)
        while len(input_list[i]) < 4:
            if direction in [0, 1]:
                input_list[i].append(0)
            else:
                input_list[i].insert(0, 0)

def print_new_grid(input_list, direction):
    for i in range(4):
        for j in range(4):
            if direction in [0, 2]:
                print(input_list[i][j], end='    ')
            else:
                print(input_list[j][i], end='     ')
        print()    

def merge_same_numbers(input_list, rows_range, offset):
    for i in range(4):
        for j in rows_range:
            if input_list[i][j] == input_list[i][j + offset]:
                input_list[i][j] *= 2 
                input_list[i][j + offset] = 0

def press_button(direction):
    if direction in [1, 3]:
        new_grid = []
        for i in range(4):
            new_grid.append([grid[j][i] for j in range(4)])
    else:
        new_grid = grid[:]

    move_numbers_right_or_left(new_grid, direction)

    if direction in [2, 3]:
        merge_same_numbers(new_grid, range(3, 0, -1), -1)
    else:
        merge_same_numbers(new_grid, range(3), 1)

    move_numbers_right_or_left(new_grid, direction)
    print_new_grid(new_grid, direction)

press_button(int(input()))