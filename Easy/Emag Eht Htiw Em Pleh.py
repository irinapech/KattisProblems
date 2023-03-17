#Emag Eht Htiw Em Pleh

board = [
    '+---+---+---+---+---+---+---+---+', 
    '|...|:::|...|:::|...|:::|...|:::|',
    '+---+---+---+---+---+---+---+---+',
    '|:::|...|:::|...|:::|...|:::|...|',
    '+---+---+---+---+---+---+---+---+',
    '|...|:::|...|:::|...|:::|...|:::|',
    '+---+---+---+---+---+---+---+---+',
    '|:::|...|:::|...|:::|...|:::|...|',
    '+---+---+---+---+---+---+---+---+',
    '|...|:::|...|:::|...|:::|...|:::|',
    '+---+---+---+---+---+---+---+---+',
    '|:::|...|:::|...|:::|...|:::|...|',
    '+---+---+---+---+---+---+---+---+',
    '|...|:::|...|:::|...|:::|...|:::|',
    '+---+---+---+---+---+---+---+---+',
    '|:::|...|:::|...|:::|...|:::|...|',
    '+---+---+---+---+---+---+---+---+'
]
board = [list(s) for s in board]

word_length = 7
letters_to_columns = 30
rows_to_indexes = 17
column_width = 4
row_height = 2

def scan_input_into_figures(input_list):
    input_list = input_list[word_length:]
    figures = input_list.split(',')
    return figures

white = input()
black = input()

white = scan_input_into_figures(white)
black = scan_input_into_figures(black)

def find_column(figures, i, index):
    column = letters_to_columns - column_width * (ord('h') - ord(figures[i][index]))
    return column

def find_row(figures, i, index):
    row = rows_to_indexes - row_height * ((ord(figures[i][index + 1])) - ord('0'))
    return row


def place_figures_on_board(figures, board, is_black):
    for i in range(len(figures)):
        if len(figures[i]) == 3:
            column = find_column(figures, i, 1)
            row = find_row(figures, i, 1)
            if is_black:
                board[row][column] = chr(ord(figures[i][0]) + ord(' '))
            else:
                board[row][column] = figures[i][0]

        elif len(figures[i]) == 2:
            column = find_column(figures, i, 0)
            row = find_row(figures, i, 0)
            if is_black:
                board[row][column] = 'p'
            else:
                board[row][column] = 'P'

place_figures_on_board(white, board, is_black = False)
place_figures_on_board(black, board, is_black = True)

for line in board:
    print(''.join(line))