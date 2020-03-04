import numpy as np

rook = 4
wk = 2
bk = 1

def check_for_white(white_king_pos, black_king_pos, rook_pos):
    if (black_king_pos[0] == rook_pos[0]) or (black_king_pos[1] == rook_pos[1]):
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
                if not check_for_white(white_king_pos, [black_king_pos[0] + 1 - i, black_king_pos[1] + 1 - j], rook_pos):
                    return False
    return True

class Board:
    def __init__(self, size, white_king_pos, black_king_pos, rook_pos, last_move):
        self.size = size
        self.white_king_pos = white_king_pos
        self.black_king_pos = black_king_pos
        self.rook_pos = rook_pos
        self.last_move = last_move

    def all_pos_moves(self):
        def white_king_pos_moves():
            possibilities = []
            for i in range(3):
                for j in range(3):
                    new_pos_x = self.white_king_pos[0] + 1 - i
                    new_pos_y = self.white_king_pos[1] + 1 - j
                    new_pos = [new_pos_x, new_pos_y]
                    if ((0 <= new_pos_x < self.size) and
                    (0 <= new_pos_y < self.size) and
                    (new_pos != self.white_king_pos) and
                    (new_pos != self.rook_pos) and
                    (not check_for_black(new_pos, self.black_king_pos, self.rook_pos))):
                        possibilities.append(Board(self.size, new_pos, self.black_king_pos, self.rook_pos, "w"))
            return possibilities

        def black_king_pos_moves():
            possibilities = []
            for i in range(3):
                for j in range(3):
                    new_pos_x = self.black_king_pos[0] + 1 - i
                    new_pos_y = self.black_king_pos[1] + 1 - j
                    new_pos = [new_pos_x, new_pos_y]
                    if ((0 <= new_pos_x < self.size) and
                    (0 <= new_pos_y < self.size) and
                    (new_pos != self.black_king_pos) and
                    (new_pos != self.rook_pos) and
                    (not check_for_white(self.white_king_pos, new_pos, self.rook_pos))):
                        possibilities.append(Board(self.size, self.white_king_pos, new_pos, self.rook_pos, "b"))
            return possibilities

        def rook_pos_moves():  
            possibilities = []
            for i in range(self.size):
                if not ((self.rook_pos[0] <= self.white_king_pos[0] <= i) and (self.rook_pos[1] == self.white_king_pos[1])):
                    if i != self.rook_pos[0]:
                        possibilities.append(Board(self.size, self.white_king_pos, self.black_king_pos, [i, self.rook_pos[1]], "w"))
                if not ((self.rook_pos[1] <= self.white_king_pos[1] <= i) and (self.rook_pos[0] == self.white_king_pos[0])):
                    if i != self.rook_pos[1]:
                        possibilities.append(Board(self.size, self.white_king_pos, self.black_king_pos, [self.rook_pos[0], i], "w"))
            return possibilities
        
        if self.last_move == "b":
            return white_king_pos_moves() + rook_pos_moves()
        else:
            return black_king_pos_moves()
                
            
def BFS(board, last_level, counter, checked):
    counter += 1
    size = board.size
    board = board
    # [wk pos, bk pos, rook pos]
    if check_m_for_white(size, board.white_king_pos, board.black_king_pos, board.rook_pos):
        print(counter, board.white_king_pos, board.black_king_pos, board.rook_pos)
        return 0
    for next_board in last_level.all_pos_moves():
        if next_board



board = Board(8, [0,0], [7,7], [6,1], "b")
print(board.all_pos_moves())