import random, math
import copy
from heapq import heappush, heappop
import time
from os import system

#0 -free, 1 - black, 2 - white
size = 8
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 1, 0, 0, 0],
         [0, 0, 0, 1, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
free = 60
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
    return make_move(random_move, pos_moves[random_move], board)

def heuristic(board, player, free, passes):
    enemy = player%2+1
    WEIGHTS = [[20, -3, 11, 8, 8, 11, -3, 20],
                [-3, -7, -4, 1, 1, -4, -7, -3],
                [11, -4, 2, 2, 2, 2, -4, 11],
                [8, 1, 2, -3, -3, 2, 1, 8],
                [8, 1, 2, -3, -3, 2, 1, 8],
                [11, -4, 2, 2, 2, 2, -4, 11],
                [-3, -7, -4, 1, 1, -4, -7, -3],
                [20, -3, 11, 8, 8, 11, -3, 20]]

    player_blocks = 0
    enemy_blocks = 0
    sum_weights = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == player:
                sum_weights += WEIGHTS[i][j]
                player_blocks += 1
            elif board[i][i] == enemy:
                sum_weights -= WEIGHTS[i][j]
                enemy_blocks += 1

    coin_value = 100 * (player_blocks - enemy_blocks) / (player_blocks + enemy_blocks)

    player_corners = 0
    enemy_corners = 0
    corners_value = 0
    for cords in [(0, 0), (0, 7), (7, 0), (7, 7)]:
        if board[cords[0]][cords[1]] == player:
            player_corners += 1
        elif board[cords[0]][cords[1]] == enemy:
            enemy_corners += 1

    if player_corners + enemy_corners != 0:
        corners_value = 100 * (player_corners - enemy_corners) / (player_corners + enemy_corners)

    player_blocks = enemy_blocks = 0
    if board[0][0] == 0:
        if board[0][1] == player: player_blocks += 1
        elif board[0][1] == enemy: enemy_blocks += 1
        if board[1][1] == player: player_blocks += 1
        elif board[1][1] == enemy: enemy_blocks += 1
        if board[1][0] == player: player_blocks += 1
        elif board[1][0] == enemy: enemy_blocks += 1
    if board[0][7] == 0:
        if board[0][6] == player: player_blocks += 1
        elif board[0][6] == enemy: enemy_blocks += 1
        if board[1][6] == player: player_blocks += 1
        elif board[1][6] == enemy: enemy_blocks += 1
        if board[1][7] == player: player_blocks += 1
        elif board[1][7] == enemy: enemy_blocks += 1
    if board[7][0] == 0:
        if board[7][1] == player: player_blocks += 1
        elif board[7][1] == enemy: enemy_blocks += 1
        if board[6][1] == player: player_blocks += 1
        elif board[6][1] == enemy: enemy_blocks += 1
        if board[6][0] == player: player_blocks += 1
        elif board[6][0] == enemy: enemy_blocks += 1
    if board[7][7] == 0:
        if board[6][7] == player: player_blocks += 1
        elif board[6][7] == enemy: enemy_blocks += 1
        if board[6][6] == player: player_blocks += 1
        elif board[6][6] == enemy: enemy_blocks += 1
        if board[7][6] == player: player_blocks += 1
        elif board[7][6] == enemy: enemy_blocks += 1

    close_to_corner_value = -12.5 * (player_blocks - enemy_blocks)
    x = sum_weights if free == 0 else sum_weights*(1/free)

    return (10*coin_value) + (805.724*corners_value) + (382.026*close_to_corner_value) + (10*x) + (60*passes[1]) - (40*passes[0])

def is_terminal(free, passes):
    if free <= 0 or passes == (1, 1) or passes[0] > 1 or passes[1] > 1:
        return True
    return False

def alphabeta_heuristic_queue(board, heur, depth, a, b, maximizingPlayer, turn, passes, free):
    if depth == 0 or is_terminal(free, passes):
        if heur is None:
            return heuristic(board, turn, free, passes)
        else:
            return heur
    if maximizingPlayer:
        value = float("-inf")
        pos_moves = legal_moves(board, turn)
        if not pos_moves:
            passes_new = list(passes)
            passes_new[turn-1] += 1
            value = max(value, alphabeta_heuristic_queue(board, None, depth -1, a, b, False, turn%2 + 1, tuple(passes_new), free))
        else:
            heap = []
            for move, endpoints in pos_moves.items():
                child = make_move(move, endpoints, copy.deepcopy(board))
                heappush(heap, (-heuristic(child, turn, free-1, passes), child))
            while heap:
                child = heappop(heap)
                value = max(value, alphabeta_heuristic_queue(child[1], -child[0], depth -1, a, b, False, turn%2 + 1, (0, 0), free - 1))
                a = max(a, value)
                if a >= b:
                    break
        return value
    else:
        value = float("inf")
        pos_moves = legal_moves(board, turn)
        if not pos_moves:
            passes_new = list(passes)
            passes_new[turn-1] += 1
            value = min(value, alphabeta_heuristic_queue(board, None, depth -1, a, b, True, turn%2 + 1, tuple(passes_new), free))
        else:
            heap = []
            for move, endpoints in pos_moves.items():
                child = make_move(move, endpoints, copy.deepcopy(board))
                heappush(heap, (-heuristic(child, turn, free-1, passes), child))
            while heap:
                child = heappop(heap)
                value = min(value, alphabeta_heuristic_queue(child[1], -child[0], depth -1, a, b, True, turn%2 + 1, (0, 0), free - 1))
                b = min(b, value)
                if a >= b:
                    break
        return value

def alphabeta(board, depth, a, b, maximizingPlayer, turn, passes, free):
    if depth == 0 or is_terminal(free, passes):
        return heuristic(board, turn%2+1, free, passes)
    if maximizingPlayer:
        value = float("-inf")
        pos_moves = legal_moves(board, turn)
        if not pos_moves:
            passes_new = list(passes)
            passes_new[turn-1] += 1
            value = max(value, alphabeta(board, depth -1, a, b, False, turn%2 + 1, tuple(passes_new), free))
        else:
            for move, endpoints in pos_moves.items():
                child = make_move(move, endpoints, copy.deepcopy(board))
                value = max(value, alphabeta(child, depth -1, a, b, False, turn%2 + 1, (0, 0), free - 1))
                a = max(a, value)
                if a >= b:
                    break
        return value
    else:
        value = float("inf")
        pos_moves = legal_moves(board, turn)
        if not pos_moves:
            passes_new = list(passes)
            passes_new[turn-1] += 1
            value = min(value, alphabeta(board, depth -1, a, b, True, turn%2 + 1, tuple(passes_new), free))
        else:
            for move, endpoints in pos_moves.items():
                child = make_move(move, endpoints, copy.deepcopy(board))
                value = min(value, alphabeta(child, depth -1, a, b, True, turn%2 + 1, (0, 0), free - 1))
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
            value =  alphabeta(child, 2, float("-inf"), float("inf"), False, turn%2+1, passes, free-1)
            if value > current_max:
                current_max = value
                best_move = child
    return best_move

def smart_agent_heuristic_queue(board, passes, free, turn):
    pos_moves = legal_moves(board, turn)
    current_max = float("-inf")
    best_move = 0
    if not pos_moves:
        return 0
    else:
        heap = []
        for move, endpoints in pos_moves.items():
            child = make_move(move, endpoints, copy.deepcopy(board))
            heappush(heap, (-heuristic(child, turn, free-1, passes), child))
        while heap:
            child = heappop(heap)
            value =  alphabeta_heuristic_queue(child[1], -child[0], 2, float("-inf"), float("inf"), False, turn%2+1, passes, free-1)
            if value > current_max:
                current_max = value
                best_move = child[1]
    return best_move

def print_board():
    # system('clear')
    for i in range(size):
        line = ''
        for j in range(size):
            if board[i][j] == 0:
                line += ". "
            elif board[i][j] == 1:
                line += "○ "
            else:
                line += "● "
        print(line)
    # time.sleep(0.4)

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


start_t = time.time()
counter = 0
GAMES = 1000
for i in range(GAMES):
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
    free = 60
    turn = 1
    passes = (0, 0)
    while not is_terminal(free, passes):
        move = 0
        if turn == 1:
            move = smart_agent(board, passes, free, turn)
            if move == 0 and passes[0] != 1:
                passes = (1, passes[1])
        else:
            move = random_bot(board, turn)
            # move = smart_agent(board, passes, free, turn)
            if move == 0 and passes[1] != 1:
                passes = (passes[0], 1)
        if move != 0:
            passes = (0, 0)
            board = move
            free -= 1
            
        # print('player:', turn)
        # print('passes:', passes)
        # print('free:', free)
        # print_board()
        # print(50*'-')
        turn = turn%2+1

    counter += result()
end_t = time.time()
print('Games number:', GAMES)
print('Lost games', counter)
print('time:', end_t - start_t)