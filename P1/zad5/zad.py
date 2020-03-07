from random import randint
#□ ■ 
#picture - ((columns), (rows))

def bad_columns(picture, board):
    bad_col = []
    for i in range(len(picture[0])):
        counter = 0
        for j in range(len(picture[1])):
            if board[j][i] == 1:
                counter += 1
        if counter != picture[0][i]:
            bad_col.append(i)
    return bad_col



def bad_rows(picture, board):
    bad_ro = []
    for i in range(len(picture[1])):
        if sum(board[i]) != picture[1][i]:
            bad_ro.append(i)
    return bad_ro


def one_step(picture, board):
    if len(bad_rows(picture, board)) == 0 and len(bad_columns(picture, board)) == 0:
        return 1
    row = True
    if len(bad_rows(picture, board)) != 0:
        random_row = bad_rows(picture, board)[randint(0, len(bad_rows(picture, board)) - 1)]
    else:
        random_column = bad_columns(picture, board)[randint(0, len(bad_columns(picture, board)) - 1)]
        row = False
    list_of_pixels = []
    if row:
        for i in range(len(picture[1])):
            list_of_pixels.append((random_row, i))
    else:
        for i in range(len(picture[1])):
            list_of_pixels.append((i, random_column))
    if row:
        last_board = board
        for i in range(len(picture[1])):
            try_board = board
            try_board[random_row][i] = (try_board[random_row][i] + 1)%2
            if (len(bad_columns(picture, try_board)) + len(bad_rows(picture, try_board))) <= (len(bad_columns(picture, last_board)) + len(bad_rows(picture, last_board))):
                last_board = try_board
                return last_board
            
        return last_board
    
    else:
        for i in range(len(picture[1])):
            try_board = board
            try_board[i][random_column] = (try_board[i][random_column] + 1)%2
            if (len(bad_columns(picture, try_board)) + len(bad_rows(picture, try_board))) <= (len(bad_columns(picture, board)) + len(bad_rows(picture, board))):
                last_board = try_board
                return last_board
        return last_board
    
          


def solve(picture):
    board = [[0 for i in range(len(picture[0]))] for i in range(len(picture[0]))]
    while True:
        if one_step(picture,board) == 1:
            return board
        board = one_step(picture, board)

print(solve(([7,7,7,7,7,7,7], [7,7,7,7,7,7,7])))