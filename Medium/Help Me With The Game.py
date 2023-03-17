number_of_lines = 17
column_offset = 2
cell_width = 4
row_width = 2
number_of_rows = 8

board = []

pieces = dict()
piece_ordering = ['K', 'Q', 'R', 'B', 'N', 'P']

for i in range(number_of_lines):
    line = input()
    board.append(line)

def add_figure(element, destination, column, row):
    element = element.upper()
    if element == 'P':
        destination.append(f"{column}{row}")
    else:
        destination.append(f"{element}{column}{row}")

def get_column_and_row(i, j):
    row = number_of_rows - i // row_width
    column = chr(ord('a') + (j - column_offset) // cell_width)
    return column, row

def set_pieces_dict(rows_range, color_condition):
    for piece in piece_ordering:
        pieces[piece] = []

    for i in rows_range:
        line = board[i]
        for j in range(len(line)):
            if line[j].isalpha() and color_condition(line[j]):
                column, row = get_column_and_row(i, j)
                add_figure(line[j], pieces[line[j].upper()], column, row)

#looking for white pieces
set_pieces_dict(range(number_of_lines - 1, -1, -1), lambda element: element.isupper())
white = []
for list in pieces.values():
    white.extend(list)
print('White: ' + ','.join(white))

#looking for black pieces
set_pieces_dict(range(number_of_lines), lambda element: element.islower())
black = []
for list in pieces.values():
    black.extend(list)
print('Black: ' + ','.join(black))