#board = [size, whitekingpos, blackkingpos, rookpos, lastmove]

def check_for_white(white_king_pos, black_king_pos, rook_pos):
    if ((black_king_pos[0] == rook_pos[0]) or (black_king_pos[1] == rook_pos[1])) and (black_king_pos != rook_pos):
        if not ((((rook_pos[0] <= white_king_pos[0] < black_king_pos[0]) or
        (rook_pos[0] >= white_king_pos[0] > black_king_pos[0])) and (white_king_pos[1] == black_king_pos[1])) or
        (((rook_pos[1] <= white_king_pos[1] < black_king_pos[1]) or
        (rook_pos[1] >= white_king_pos[1] > black_king_pos[1])) and (white_king_pos[0] == black_king_pos[0]))):
            return True
    if ((abs(black_king_pos[0] - white_king_pos[0]) <= 1) and
        (abs(black_king_pos[1] - white_king_pos[1]) <= 1)):
        return True
    return False

def check_for_black(white_king_pos, black_king_pos, rook_pos):
    if ((abs(black_king_pos[0] - white_king_pos[0]) <= 1) and
        (abs(black_king_pos[1] - white_king_pos[1]) <= 1)):
        return True
    return False


def check_m_for_white(size, white_king_pos, black_king_pos, rook_pos):
    for i in range(3):
        for j in range(3):
            if (0<=black_king_pos[0] + 1 - i<size and 0<=black_king_pos[1] + 1 - j<size):
                if check_for_white(white_king_pos, (black_king_pos[0] + 1 - i, black_king_pos[1] + 1 - j), rook_pos) == False:
                    return False
    return True

#if last_move 1 now white
def all_pos_moves(size, white_king_pos, black_king_pos, rook_pos, last_move):
    def white_king_pos_moves():
        possibilities = set()
        for i in range(3):
            for j in range(3):
                new_pos_x = white_king_pos[0] + 1 - i
                new_pos_y = white_king_pos[1] + 1 - j
                new_pos = (new_pos_x, new_pos_y)
                if ((0 <= new_pos_x < size) and
                (0 <= new_pos_y < size) and
                (new_pos != white_king_pos) and
                (new_pos != rook_pos) and
                (not check_for_black(new_pos, black_king_pos, rook_pos))):
                    possibilities.add((size, new_pos, black_king_pos, rook_pos, 0))
        return possibilities

    def black_king_pos_moves():
        possibilities = set()
        for i in range(3):
            for j in range(3):
                new_pos_x = black_king_pos[0] + 1 - i
                new_pos_y = black_king_pos[1] + 1 - j
                new_pos = (new_pos_x, new_pos_y)
                if ((0 <= new_pos_x < size) and
                (0 <= new_pos_y < size) and
                (new_pos != black_king_pos) and
                (new_pos != rook_pos) and
                (not check_for_white(white_king_pos, new_pos, rook_pos))):
                    possibilities.add((size, white_king_pos, new_pos, rook_pos, 1))
        return possibilities

    def rook_pos_moves():  
        possibilities = set()
        for i in range(size):
            if not ((rook_pos[0] <= white_king_pos[0] <= i) and (rook_pos[1] == white_king_pos[1])):
                if i != rook_pos[0]:
                    possibilities.add((size, white_king_pos, black_king_pos, (i, rook_pos[1]), 0))
            if not ((rook_pos[1] <= white_king_pos[1] <= i) and (rook_pos[0] == white_king_pos[0])):
                if i != rook_pos[1]:
                    possibilities.add((size, white_king_pos, black_king_pos, (rook_pos[0], i), 0))
        return possibilities
    
    if last_move == 1:
        return white_king_pos_moves().union(rook_pos_moves())
    else:
        return black_king_pos_moves()
          
def BFS(board):
    queue = []
    i = -2
    queue.append(board)
    queue.append(board)
    checked = {board}
    while True:
        i +=2
        if check_m_for_white(queue[i][0], queue[i][1], queue[i][2], queue[i][3]):
            return queue[i+1]
        else:
            for next_board in all_pos_moves(queue[i][0], queue[i][1], queue[i][2], queue[i][3], queue[i][4]):
                if next_board not in checked:
                    queue.append(next_board)
                    queue.append(queue[i+1]+next_board)
                    checked.add(next_board)
