import random, math
import copy
#0 -free, 1 - black, 2 - white
size = 8
board = [[0 for i in range(size)] for j in range(size)]
free = 0
turn = 0

    


def find_neighbours(move, board):
    x = move[0]
    y = move[1]
    neighbours = []
    for i in range(3):
        for j in range(3):
            a = i - 1
            b = j - 1 
            if (x + a) < size and (x + a >= 0) and (y + b < size) and (y + b >= 0) and (a != 0 or b != 0):
                if board[x+a][y+b] == 0:
                    neighbours.append((x+a, y+b))
    return neighbours

free = 60



def make_move(move, end_points, board):
    x, y = move
    player_color = board[end_points[0][0]][end_points[0][1]]
    current_field = move
    for end_point in end_points:
        if x < end_point[0]:
            if y > end_point[1]:
                vector = (1,-1)
            elif y == end_point[1]:
                vector = (1, 0)
            else:
                vector = (1,1)
        elif x == end_point[0]:
            if y > end_point[1]:
                vector = (0,-1)
            elif y == end_point[1]:
                vector = (0, 0)
            else:
                vector = (0,1)
        else:
            if y > end_point[1]:
                vector = (-1,-1)
            elif y == end_point[1]:
                vector = (-1, 0)
            else:
                vector = (-1,1)

        while current_field != end_point:
            board[current_field[0]][current_field[1]] = player_color
            current_field = (current_field[0] + vector[0], current_field[1] + vector[1])
        current_field = move
    
    return board
        


    

def legal_moves(board, turn):
    pos_moves = {}
    for i in range(size):
        for j in range(size):
            if board[i][j] == turn%2 + 1:
                neighbours = find_neighbours([i,j], board)
                for neighbour in neighbours:
                    nx = neighbour[0]
                    ny = neighbour[1]
                    v_x = i - nx
                    v_y = j - ny
                    new_x = i
                    new_y = j
                    while new_x < size and new_x>= 0 and new_y < size and new_y >= 0:
                        if board[new_x][new_y] == 0:
                            break
                        if board[new_x][new_y] == turn:
                            if neighbour in pos_moves.keys():
                                pos_moves[neighbour].append((new_x, new_y))
                            else:
                                pos_moves[neighbour] = [(new_x, new_y)]
                            break
                        new_x += v_x
                        new_y += v_y
    return pos_moves


def random_bot(board, turn):
    pos_moves = legal_moves(board, turn)
    if not pos_moves:
        return 0
    random_move = random.choice(list(pos_moves.keys()))
    return (random_move, pos_moves[random_move])


def heur(board, free):
    WEIGHTS = [[4, -3, 2, 2, 2, 2, -3, 4],
                [-3, -4, -1, -1, -1, -1, -4, -3],
                [2, -1, 1, 0, 0, 1, -1, 2],
                [2, -1, 0, 1, 1, 0, -1, 2],
                [2, -1, 0, 1, 1, 0, -1, 2],
                [2, -1, 1, 0, 0, 1, -1, 2],
                [-3, -4, -1, -1, -1, -1, -4, -3],
                [4, -3, 2, 2, 2, 2, -3, 4]]
    if free >40:
        sum_points = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    sum_points += WEIGHTS[i][j] 
                elif board[i][i] == 2:
                    sum_points -= WEIGHTS[i][j]
        return sum_points
    else:
        sum_points = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    sum_points += 1 #WEIGHTS[i][j] /free 
                elif board[i][i] == 2:
                    sum_points -= 1 #WEIGHTS[i][j] /free
        return sum_points
def is_terminal(free, passes):
    if free <= 0 or passes >= 2:
        return True
    return False

def alphabeta(board, depth, a, b, maximizingPlayer, turn, passes, free):
    if depth == 0 or is_terminal(free, passes):
        return heur(board, free)
    if maximizingPlayer:
        value = float("-inf")
        pos_moves = legal_moves(board, turn)
        if not pos_moves:
            value = max(value, alphabeta(board, depth -1, a, b, False, turn%2 + 1, passes+1, free))
        else:
            for move, endpoints in pos_moves.items():
                child = make_move(move, endpoints, copy.deepcopy(board))
                value = max(value, alphabeta(child, depth -1, a, b, False, turn%2 + 1, 0, free - 1))
                a = max(a, value)
                if a >= b:
                    break
        return value
    else:
        value = float("inf")
        pos_moves = legal_moves(board, turn)
        if not pos_moves:
            value = min(value, alphabeta(board, depth -1, a, b, True, turn%2 + 1, passes+1, free))
        else:
            for move, endpoints in pos_moves.items():
                child = make_move(move, endpoints, copy.deepcopy(board))
                value = min(value, alphabeta(child, depth -1, a, b, True, turn%2 + 1, 0, free - 1))
                b = min(b, value)
                if a >= b:
                    break
        return value
    

def smart_agent(board, passes, free, turn):
    pos_moves = legal_moves(board, turn)
    current_max = float("-inf")
    best_move = 0
    if not pos_moves:
        return 0
    else:
        for move, endpoints in  pos_moves.items():
            child = make_move(move, endpoints, copy.deepcopy(board))
            value =  alphabeta(child, 2, float("-inf"), float("inf"), True, turn, passes, free)
            if value > current_max:
                current_max = value
                best_move = (move, endpoints)
    return best_move





def print_board():
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                print(". ")
            elif board[i][j] == 1:
                print("○ ")
            else:
                print("● ")
            
        print(" ")

#print(find_neighbours([3,3], board))
#print_board()
def result():
    white_counter = 0
    black_counter = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                black_counter += 1
            elif board[i][j] == 2:
                white_counter += 1
    if black_counter > white_counter:
        return 0
    elif black_counter < white_counter:
        return 1
    else:
        return 0


counter = 0
for i in range(100):
    board = [[0 for i in range(size)] for j in range(size)]
    board[size//2 - 1][size//2 - 1] = 2
    board[size//2][size//2] = 2
    board[size//2 - 1][size//2] = 1
    board[size//2][size//2 - 1] = 1
    free = size**2 - 4
    turn = 1
    passes = 0
    while free:
        if passes == 2:
            break
        move = 0
        if turn == 1:
            move = smart_agent(board, passes, free, turn)

        else:
            move = random_bot(board, turn)
            
        if move == 0:
            passes += 1
        else:
            board = make_move(move[0], move[1], board)
            free -= 1
            
        turn = 2 - (turn + 1)%2

    counter += result()
print(counter)
    

