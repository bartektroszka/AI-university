from random import randint
from copy import deepcopy
#picture = [[columns], [rows]]
#board = [[col1, col2 ...][row1, row2 ...]]
def bad_columns(picture, columns):
    bad = []
    for i in range(len(columns)):
        counter = 0
        for j in range(len(columns)):
            if counter != 0 and columns[i][j] == 1:
                bad.append(i)
            if columns[i][j] == 1:
                counter +=1
        if counter != picture[0][i] and i not in bad:
            bad.append(i)
    return bad

def bad_rows(picture, rows):
    bad = []
    for i in range(len(rows)):
        counter = 0
        for j in range(len(rows)):
            if counter != 0 and rows[i][j] == 1:
                bad.append(i)
            if rows[i][j] == 1:
                counter +=1
        if counter != picture[1][i] and i not in bad:
            bad.append(i)
    return bad

def missing(picture, columns, rows):
    missing_sum = 0
    for i in range(len(columns)):
        missing_sum += picture[0][i] - sum(columns[i])
        missing_sum += picture[1][i] - sum(rows[i])
    return missing_sum

def one_step(picture, board):
    if len(bad_rows(picture, board[1])) == 0:
        random_column = bad_columns(picture, board[0])[randint(0, len(bad_columns(picture, board[0]))-1)]
        last_board = board
        for i in range(len(board[0])):
            try_board = deepcopy(last_board)
            try_board[0][random_column][i] = (try_board[0][random_column][i] + 1) %2
            try_board[1][i][random_column] = (try_board[0][random_column][i] + 1) %2
            if missing(picture, try_board[0], try_board[1]) < missing(picture, last_board[0], last_board[1]):
                last_board = try_board
        board = last_board


    else:
        random_row = bad_rows(picture, board[1])[randint(0, len(bad_rows(picture, board[1]))-1)]
        last_board = board
        for i in range(len(board[0])):
            try_board = deepcopy(last_board)
            try_board[1][random_row][i] = (try_board[1][random_row][i] + 1) %2
            try_board[0][i][random_row] = try_board[1][random_row][i]
            if missing(picture, try_board[0], try_board[1]) < missing(picture, last_board[0], last_board[1]):
                last_board = try_board
        board = last_board

def solve(picture):
    board = [[], []]
    board[0] = [[0 for i in range(len(picture[0]))] for j in range(len(picture[0]))]
    board[1] = [[0 for i in range(len(picture[0]))] for j in range(len(picture[0]))]
    for i in range(1000):
        one_step(picture, board)
    print(board)

solve([[7,7,7,7,7,7,7], [7,7,7,7,7,7,7]])