import copy, random
values = {"R":1 ,"C":2, "D":3, "W":4, "J":5, "T":6, "L":7, "E":8, "r":1 ,"c":2, "d":3, "w":4, "j":5, "t":6, "l":7, "e":8, "N":0, "n":0}
board = [[".",".","#","*","#",".","."],
        [".",".",".","#",".",".","."],
        [".",".",".",".",".",".","."],
        [".","~","~",".","~","~","."],
        [".","~","~",".","~","~","."],
        [".","~","~",".","~","~","."],
        [".",".",".",".",".",".","."],
        [".",".",".","#",".",".","."],
        [".",".","#","*","#",".","."]]

deployment = [["L",".",".",".",".",".","T"],
              [".","D",".",".",".","C","."],
              ["R",".","J",".","W",".","E"],
              [".",".",".",".",".",".","."],
              [".",".",".",".",".",".","."],
              [".",".",".",".",".",".","."],
              ["e",".","w",".","j",".","r"],
              [".","d",".",".",".","c","."],
              ["t",".",".",".",".",".","l"]]

R = 1
C = 2
D = 3
W = 4
J = 5
T = 6
L = 7
E = 8

r = 1
c = 2
d = 3
w = 4
j = 5
t = 6
l = 7
e = 8


def result(deployment, values):
    maks_small = 0
    maks_big = 0
    for i in range(9):
        for j in range(7):
            if deployment[i][j] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                if values[deployment[i][j]] > maks_big:
                    maks_big = values[deployment[i][j]]
            elif deployment[i][j] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                if values[deployment[i][j]] > maks_small:
                    maks_small = values[deployment[i][j]]
                
    if maks_big > maks_small:
        return 1
    else:
        return 2


#1 player big, 2 player small
def can_move(turn, move, deployment, values):
    x1, y1 = move[0]
    x2, y2 = move[1]
    if turn == 1:
        figure = deployment[x1][y1]
        if figure in ["R", "C", "D", "W", "J", "T", "L", "E"] and (x2 != 0 or y2 != 3):
            if abs(x2+y2 - x1 - y1) <=1:
                if figure == "R" and board[x2][y2] == "~":
                    return True
                elif board[x2][y2] == ".":
                    if deployment[x2][y2] == ".":
                        return True
                    elif deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                        if board[x1][y1] != "~":
                            if figure == "R" and deployment[x2][y2] == "e":
                                return True
                                
                            else:
                                if values[figure] >= values[deployment[x2][y2]]:
                                    return True
                    
                elif board[x2][y2] == "#":
                    if deployment[x2][y2] == ".":
                        return True
                    elif deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                        if figure == "R" and deployment[x2][y2] == "e":
                            return 0
                        else: 
                            if values[figure] >= values[deployment[x2][y2]]:
                                return True
                
                elif x2 == 8 and y2 == 3:
                    return True
            
            elif figure == "L" or figure == "T":
                if (x2 == x1 and abs(y2 - y1) == 3):
                    if y2 > y1:
                        trigger = False
                        for i in range(y1+1, y2):
                            if board[x1][i] != "~" or deployment[x1][i] == "r":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                                if figure == "R" and deployment[x2][y2] == "e":
                                    return True
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        return True
                            elif deployment[x2][y2] == ".":
                                return True
                    elif y2 < y1:
                        trigger = False
                        for i in range(y2+1, y1):
                            if board[x1][i] != "~" or deployment[x1][i] == "r":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                                if figure == "R" and deployment[x2][y2] == "e":
                                    return True
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        return True
                            elif deployment[x2][y2] == ".":
                                return True
                elif(y2 == y1 and abs(x2-x1) == 4):
                    if x2 > x1:
                        trigger = False
                        for i in range(x1+1, x2):
                            if board[i][y1] != "~" or deployment[i][y1] == "r":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                                if figure == "R" and deployment[x2][y2] == "e":
                                    return True
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        return True
                            elif deployment[x2][y2] == ".":
                                return True


                    elif x1 > x2:
                        trigger = False
                        for i in range(x2+1, x1):
                            if board[i][y1] != "~" or deployment[i][y1] == "r":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                                if figure == "R" and deployment[x2][y2] == "e":
                                    return True
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        return True
                            elif deployment[x2][y2] == ".":
                                return True


    if turn == 2:
        figure = deployment[x1][y1]
        if figure in ["r", "c", "d", "w", "j", "t", "l", "e"] and (x2 != 8 or y2 != 3):
            if abs(x2+y2 - x1 - y1) <=1:
                if figure == "r" and board[x2][y2] == "~":
                    return True
                elif board[x2][y2] == ".":
                    if deployment[x2][y2] == ".":
                        return True
                    elif deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                        if board[x1][y1] != "~":
                            if figure == "r" and deployment[x2][y2] == "E":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                            else:
                                if values[figure] >= values[deployment[x2][y2]]:
                                    return True
                    
                elif board[x2][y2] == "#":
                    if deployment[x2][y2] == ".":
                        return True
                    elif deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                        if figure == "r" and deployment[x2][y2] == "E":
                            return True
                        else: 
                            if values[figure] >= values[deployment[x2][y2]]:
                                return True
                
                elif x2 == 0 and y2 == 3:
                    return True
            
            elif figure == "l" or figure == "t":
                if (x2 == x1 and abs(y2 - y1) == 3):
                    if y2 > y1:
                        trigger = False
                        for i in range(y1+1, y2):
                            if board[x1][i] != "~" or deployment[x1][i] == "R":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                                if figure == "r" and deployment[x2][y2] == "E":
                                    return True
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        return True
                            elif deployment[x2][y2] == ".":
                                return True
                    elif y2 < y1:
                        trigger = False
                        for i in range(y2+1, y1):
                            if board[x1][i] != "~" or deployment[x1][i] == "R":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                                if figure == "r" and deployment[x2][y2] == "E":
                                    return True
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        return True
                            elif deployment[x2][y2] == ".":
                                return True
                elif(y2 == y1 and abs(x2-x1) == 4):
                    if x2 > x1:
                        trigger = False
                        for i in range(x1+1, x2):
                            if board[i][y1] != "~" or deployment[i][y1] == "R":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                                if figure == "r" and deployment[x2][y2] == "E":
                                    return True
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        return True
                            elif deployment[x2][y2] == ".":
                                return True


                    elif x1 > x2:
                        trigger = False
                        for i in range(x2+1, x1):
                            if board[i][y1] != "~" or deployment[i][y1] == "R":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                                if figure == "r" and deployment[x2][y2] == "E":
                                    return True
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                return True      
                



def make_move(turn, move, deployment, kill, values):
    kill = False
    figure = deployment[move[0][0]][move[0][1]]
    if can_move(turn, move, deployment, values):
        if deployment[move[1][0]][move[1][1]] in ["R", "C", "D", "W", "J", "E", "r", "c", "d", "w", "j", "e", "T", "L", "t", "l"]:
            kill = True
        deployment[move[1][0]][move[1][1]] = figure
        deployment[move[0][0]][move[0][1]] = "."
        if board[move[1][0]][move[1][1]] == "#":
            values[figure] = 0
    return kill            

        




def possible_moves(deployment, turn, values):
    pos_moves = set()
    for i in range(9):
        for j in range(7):
            if deployment[i][j] in ["R", "C", "D", "W", "J", "E", "r", "c", "d", "w", "j", "e", "T", "L", "t", "l"]:
                for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (i + a) < 9 and (i + a)>= 0 and (j + b)< 7 and(j + b) >= 0:
                        new_move = ((i, j),(i + a, j + b))
                        if can_move(turn, new_move, deployment, values):
                            pos_moves.add(new_move)
            
            if deployment[i][j] in ["T", "L", "t", "l"]:
                for a,b in [(4,0),(-4,0),(0,3),(0,-3)]:
                    if (i + a) < 8 and (i + a)>= 0 and (j + b)< 6 and(j + b) >= 0:
                        new_move = ((i, j),(i + a, j + b))
                        if can_move(turn, new_move, deployment, values):
                            pos_moves.add(new_move)

    return pos_moves


def draw(deployment):
    vis_board = [[] for i in range(9)]
    for i in range(9):
        for j in range(7):
            if deployment[i][j] != ".":
                vis_board[i].append(deployment[i][j])
            else:
                vis_board[i].append(board[i][j])
    for i in range(9):
        print(vis_board[i])



def evaluate(deployment, k, turn, values):
    counter = k
    player_big_score = 0
    player_small_score = 0
    kill = False
    begin_turn = turn
    while counter > 0:
        turn = begin_turn
        copy_deployment = copy.deepcopy(deployment)
        copy_values = copy.deepcopy(values)
        move_counter = 0
        while counter > 0:
            if kill:
                move_counter = 0
                kill = False
            
            move_counter +=1
            if move_counter > 30:
                if result(copy_deployment, copy_values) == 1:
                    player_big_score += 1
                    break
                else:
                    player_small_score += 1
                    break
            if copy_deployment[0][3] != ".":
                player_small_score += 1
                break
            if copy_deployment[8][3] != ".":
                player_big_score += 1
                break
            possi_moves = possible_moves(copy_deployment, turn, copy_values)
            if possi_moves:
                random_move = random.sample(possi_moves, 1)[0]
                make_move(turn, random_move, copy_deployment, kill, copy_values)
                move_counter += 1
                counter -= 1
                turn = turn%2 + 1
            else:
                if result(copy_deployment, copy_values) == 1:
                    player_big_score += 1
                    break
                else:
                    player_small_score += 1
                    break

    return(player_big_score, player_small_score)

def smart_agent(deployment, turn, values):
    pos_moves = possible_moves(deployment, turn, values)
    best_result = -1000000
    best_move = 0
    begin_turn = turn
    k = 20000//len(pos_moves)
    for pos_move in pos_moves:
        copy_deployment = copy.deepcopy(deployment)
        copy_values = copy.deepcopy(values)
        make_move(begin_turn, pos_move, copy_deployment, kill, copy_values)
        turn = begin_turn%2 + 1
        if turn == 1:
            b, s = evaluate(copy_deployment, k, turn, copy_values)
            result = s/(b+s)
            if result >= best_result:
                best_result = result
                best_move = pos_move

        elif turn == 2:
            b, s = evaluate(copy_deployment, k, turn, copy_values)
            result = b/(b+s)
            if result >= best_result:
                best_result = result
                best_move = pos_move
    return best_move
        


def random_agent(deployment, turn, values):
    pos_moves = possible_moves(deployment, turn, values)
    if pos_moves:
        return random.sample(pos_moves, 1)[0]
    else:
        return ((0,0), (0,0))


def is_terminal(deployment, counter):
    if deployment[0][3] != "." or deployment[8][3] != ".":
        return True
    if counter > 30:
        return True
    return False


def heur(deployment, counter):
    summ = 0
    small_rat = False
    big_rat = False
    small_ele = False
    big_ele = False
    if deployment[0][3] != ".":
        summ =  float("-inf")
    elif deployment[8][3] != ".":
        summ =  float("inf")
    else:
        summ -= counter
        for i in range(9):
            for j in range(7):
                figure = deployment[i][j]

                if figure == "R":
                    if board[i][j] == "#" and i > 3:
                        summ += 15
                    elif board[i][j] == "#" and i < 3:
                        summ -= 30
                    big_rat = True
                    summ -= ((8 - i) + abs(3 - j))
                elif figure == "E":
                    if board[i][j] == "#" and i > 3:
                        summ += 15
                    elif board[i][j] == "#" and i < 3:
                        summ -= 30
                    big_ele = True
                    summ += values[figure] - (8 - i) - abs(3 - j)
                elif figure in ["C", "D", "W", "J", "T", "L"]:
                    if board[i][j] == "#" and i > 3:
                        summ += 15
                    elif board[i][j] == "#" and i < 3:
                        summ -= 30
                    big_rat = True
                    summ += values[figure] - (8 - i) - abs(3 - j)

                elif figure == "r":
                    if board[i][j] == "#" and i < 3:
                        summ -= 15
                    elif board[i][j] == "#" and i >3:
                        summ += 30
                    small_rat = True
                    summ += i + abs(3 - j)
                elif figure == "e":
                    if board[i][j] == "#" and i < 3:
                        summ -= 15
                    elif board[i][j] == "#" and i >3:
                        summ += 30
                    small_ele = True
                    summ -= values[figure] + i + abs(3 - j)
                elif figure in ["c", "d", "w", "j", "t", "l"]:
                    if board[i][j] == "#" and i < 3:
                        summ -= 15
                    elif board[i][j] == "#" and i >3:
                        summ += 30
                    summ -= values[figure] + i + abs(3 - j)

        if small_rat and big_ele:
            summ -= 8
        elif small_rat:
            summ -= 2
        if big_rat and small_ele:
            summ += 8
        elif big_rat:
            summ += 2
    return summ

        


def smarter_agent(deployment, turn, values, counter):
    def alphabeta(deployment, depth, a, b, maximizingplayer, turn, values, counter):
        move_counter = counter
        if is_terminal(deployment, counter) or depth == 0:
            return heur(deployment, counter)
        elif maximizingplayer:
            value = float("-inf")
            pos_moves = possible_moves(deployment, turn, values)
            kill = False
            for pos_move in pos_moves:
                copy_deployment = copy.deepcopy(deployment)
                copy_values = copy.deepcopy(values)
                if make_move(turn, pos_move, copy_deployment, kill, copy_values):
                    move_counter = 0
                    kill = False
                value = max(value, alphabeta(copy_deployment, depth - 1, a, b, False, turn%2 + 1, copy_values, move_counter+1))
                a = max(a, value)
                if a >= b:
                    break
            return value
        else:
            value = float("inf")
            pos_moves = possible_moves(deployment, turn, values)
            kill = False
            for pos_move in pos_moves:
                copy_deployment = copy.deepcopy(deployment)
                copy_values = copy.deepcopy(values)
                if make_move(turn, pos_move, copy_deployment, kill, copy_values):
                    move_counter = 0
                    kill = False
                value = min(value, alphabeta(copy_deployment, depth - 1, a, b, True, turn%2 + 1, copy_values, move_counter+1))
                b = min(b, value)
                if a >= b:
                    break
            return value
    

    if turn == 1:
        move_counter = counter
        pos_moves = possible_moves(deployment, turn, values)
        best_result = float("-inf")
        best_move = ((0,0), (0,0))
        for pos_move in pos_moves:
            copy_deployment = copy.deepcopy(deployment)
            copy_values = copy.deepcopy(values)
            if make_move(turn, pos_move, copy_deployment, kill, copy_values):
                move_counter = 0
            val = alphabeta(copy_deployment, 4, float("-inf"), float("inf"), False, turn%2 + 1, copy_values, move_counter+1)
            if val > best_result:
                best_result = val
                best_move = pos_move
        return best_move

    else:
        move_counter = counter
        pos_moves = possible_moves(deployment, turn, values)
        best_result = float("inf")
        best_move = ((0,0), (0,0))
        for pos_move in pos_moves:
            copy_deployment = copy.deepcopy(deployment)
            copy_values = copy.deepcopy(values)
            if make_move(turn, pos_move, copy_deployment, kill, copy_values):
                move_counter = 0
            val = alphabeta(copy_deployment, 4, float("-inf"), float("inf"), True, turn%2 + 1, copy_values, move_counter+1)
            if val < best_result:
                best_result = val
                best_move = pos_move
        return best_move



#EVOLUTION ALGORITHMS
#HEURISTIC: (r_value, c_value, d_value, w_value, j_value, t_value, l_value, e_value, dist_to_enemy_cave, own_traps_penalty, win_bonus, lose_penalty)
def random_heuristics(n):
    list_of_heur = []
    for i in range(n):
        r_value = random.randint(0,100)
        c_value = random.randint(0,100)
        d_value = random.randint(0,100)
        w_value = random.randint(0,100)
        j_value = random.randint(0,100)
        t_value = random.randint(0,100)
        l_value = random.randint(0,100)
        e_value = random.randint(0,100)
        dist_to_enemy_cave = random.randint(0,4)
        own_traps_penalty = random.randint(-100, 0)
        win_bonus = random.randint(100,1000)
        lose_penalty = random.randint(-1000, -100)
        list_of_heur.append([[r_value, c_value, d_value, w_value, j_value, t_value, l_value, e_value, dist_to_enemy_cave,  own_traps_penalty, win_bonus, lose_penalty], 0])
    return list_of_heur

def evaluate_board(heur, deployment):
    summ = 0
    for i in range(9):
        for j in range(7):
            figure = deployment[i][j]
            if figure in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                if board[i][j] == "*" and i>3:
                    summ = heur[0][10]
                    return summ
                summ -= ((8 - i) + abs(3 - j)) * heur[0][8]
                if board[i][j] == "#" and i < 5:
                    summ += heur[0][9]
                summ += heur[0][["R", "C", "D", "W", "J", "T", "L", "E"].index(figure)]


            elif figure in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                if board[i][j] == "*" and i<5:
                    summ = heur[0][11]
                    return summ
                summ += (abs(0 - i) + abs(3 - j)) * heur[0][8]
                if board[i][j] == "#" and i >3:
                    summ -= heur[0][9]
                summ -= heur[0][["r", "c", "d", "w", "j", "t", "l", "e"].index(figure)]
    return summ

def heur_move(heur, deployment, turn, values, kill):
    kill = False
    if turn == 1:
        best_move = ((0,0),(0,0))
        best_move_score = -10000
        pos_moves = possible_moves(deployment, turn, values)
        for pos_move in pos_moves:
            copy_deployment = copy.deepcopy(deployment)
            copy_values = copy.deepcopy(values)
            make_move(turn, pos_move, copy_deployment, kill, copy_values)
            if evaluate_board(heur, copy_deployment) > best_move_score:
                best_move_score = evaluate_board(heur, copy_deployment)
                best_move = pos_move
        return best_move

    elif turn == 2:
        best_move = ((0,0), (0,0))
        best_move_score = 1000000
        pos_moves = possible_moves(deployment, turn, values)
        for pos_move in pos_moves:
            copy_deployment = copy.deepcopy(deployment)
            copy_values = copy.deepcopy(values)
            make_move(turn, pos_move, copy_deployment, kill, copy_values)
            if evaluate_board(heur, copy_deployment) < best_move_score:
                best_move_score = evaluate_board(heur, copy_deployment)
                best_move = pos_move
        return best_move

def play_game(heur_1, heur_2, deployment, values):
    counter = 0
    turn = 1
    kill = False
    while True:
        kill = False
        if deployment[0][3] != ".":
            return 2
        elif deployment[8][3] != ".":
            return 1
        if counter >= 100:
            return result(deployment, values)
        if turn == 1:
            if make_move(turn, heur_move(heur_1, deployment, turn, values, kill), deployment, kill, values):
                counter = 0
            
        elif turn == 2:
            if make_move(turn, heur_move(heur_2, deployment, turn, values, kill), deployment, kill, values):
                counter = 0
        counter += 1

def play_game_vs_random(heur_1, deployment, values):
    counter = 0
    turn = 1
    kill = False
    while True:
        if not possible_moves(deployment, turn, values):
            return turn%2 + 1
        
        kill = False
        if deployment[0][3] != ".":
            return 2
        elif deployment[8][3] != ".":
            return 1
        if counter >= 100:
            return result(deployment, values)
        if turn == 1:
            if make_move(turn, heur_move(heur_1, deployment, turn, values, kill), deployment, kill, values):
                counter = 0
            
        elif turn == 2:
            if make_move(turn, random.choice(tuple(possible_moves(deployment, turn, values))), deployment, kill, values):
                counter = 0
        counter += 1
        turn = turn%2 + 1
    

def cross(heur_1, heur_2):
    r_value = random.choice([heur_1[0][0], heur_2[0][0]])
    c_value = random.choice([heur_1[0][1], heur_2[0][1]])
    d_value = random.choice([heur_1[0][2], heur_2[0][2]])
    w_value = random.choice([heur_1[0][3], heur_2[0][3]])
    j_value = random.choice([heur_1[0][4], heur_2[0][4]])
    t_value = random.choice([heur_1[0][5], heur_2[0][5]])
    l_value = random.choice([heur_1[0][6], heur_2[0][6]])
    e_value = random.choice([heur_1[0][7], heur_2[0][7]])
    dist_to_enemy_cave = random.choice([heur_1[0][8], heur_2[0][8]])
    own_traps_penalty = random.choice([heur_1[0][9], heur_2[0][9]])
    win_bonus = random.choice([heur_1[0][10], heur_2[0][10]])
    lose_penalty = random.choice([heur_1[0][11], heur_2[0][11]])
    return [[r_value, c_value, d_value, w_value, j_value, t_value, l_value, e_value, dist_to_enemy_cave,  own_traps_penalty, win_bonus, lose_penalty], 0]

def cross_generation(heurs, final_pop, mutation_factor):
    result = []
    for i in range(final_pop):
        result.append(cross(random.choice(heurs), random.choice(heurs)))
    for heur in result:
        mutation(heur, mutation_factor)
    return result

def mutation(heur, mutation_factor):
    for i in range(len(heur[0])):
        heur[0][i] = heur[0][i] * random.gauss(1.001, mutation_factor)
    return heur

def selection(heurs, final_number, number_of_fights):
    for heur in heurs:
        for i in range(number_of_fights):
            enemy = random.choice(heurs)
            if play_game(heur, enemy, deployment, values) == 1:
                heur[1] += 1
            else:
                enemy[1] += 1

          
              
    heurs.sort(key=lambda elem: elem[1])
    result = []
    for i in range(final_number):
        result.append(heurs[-i-1])
    return result
    

def evolution(number_of_generations, mutation_factor, number_of_fights, final_number, number_of_heurs):
    heurs = random_heuristics(number_of_heurs)
    for i in range(number_of_generations):
        selected_heurs = selection(heurs, final_number, number_of_fights)
        heurs = cross_generation(selected_heurs, number_of_heurs, mutation_factor)
    heurs = selection(heurs, final_number, number_of_fights)
    return heurs





values = {"R":1 ,"C":2, "D":3, "W":4, "J":5, "T":6, "L":7, "E":8, "r":1 ,"c":2, "d":3, "w":4, "j":5, "t":6, "l":7, "e":8, "N":0, "n":0}
board = [[".",".","#","*","#",".","."],
            [".",".",".","#",".",".","."],
            [".",".",".",".",".",".","."],
            [".","~","~",".","~","~","."],
            [".","~","~",".","~","~","."],
            [".","~","~",".","~","~","."],
            [".",".",".",".",".",".","."],
            [".",".",".","#",".",".","."],
            [".",".","#","*","#",".","."]]

deployment = [["L",".",".",".",".",".","T"],
                [".","D",".",".",".","C","."],
                ["R",".","J",".","W",".","E"],
                [".",".",".",".",".",".","."],
                [".",".",".",".",".",".","."],
                [".",".",".",".",".",".","."],
                ["e",".","w",".","j",".","r"],
                [".","d",".",".",".","c","."],
                ["t",".",".",".",".",".","l"]]

#print(random.choice(evolution(10000, 0.01, 50, 40, 100)))

vs_random_score = 0
for j in range(10):
    values = {"R":1 ,"C":2, "D":3, "W":4, "J":5, "T":6, "L":7, "E":8, "r":1 ,"c":2, "d":3, "w":4, "j":5, "t":6, "l":7, "e":8, "N":0, "n":0}
    board = [[".",".","#","*","#",".","."],
                [".",".",".","#",".",".","."],
                [".",".",".",".",".",".","."],
                [".","~","~",".","~","~","."],
                [".","~","~",".","~","~","."],
                [".","~","~",".","~","~","."],
                [".",".",".",".",".",".","."],
                [".",".",".","#",".",".","."],
                [".",".","#","*","#",".","."]]

    deployment = [["L",".",".",".",".",".","T"],
                    [".","D",".",".",".","C","."],
                    ["R",".","J",".","W",".","E"],
                    [".",".",".",".",".",".","."],
                    [".",".",".",".",".",".","."],
                    [".",".",".",".",".",".","."],
                    ["e",".","w",".","j",".","r"],
                    [".","d",".",".",".","c","."],
                    ["t",".",".",".",".",".","l"]]

    heur = random.choice(evolution(1000, 0.02, 30, 20, 100)) 
    heur_score = 0
    for i in range(1000):
        values = {"R":1 ,"C":2, "D":3, "W":4, "J":5, "T":6, "L":7, "E":8, "r":1 ,"c":2, "d":3, "w":4, "j":5, "t":6, "l":7, "e":8, "N":0, "n":0}
        board = [[".",".","#","*","#",".","."],
                    [".",".",".","#",".",".","."],
                    [".",".",".",".",".",".","."],
                    [".","~","~",".","~","~","."],
                    [".","~","~",".","~","~","."],
                    [".","~","~",".","~","~","."],
                    [".",".",".",".",".",".","."],
                    [".",".",".","#",".",".","."],
                    [".",".","#","*","#",".","."]]

        deployment = [["L",".",".",".",".",".","T"],
                        [".","D",".",".",".","C","."],
                        ["R",".","J",".","W",".","E"],
                        [".",".",".",".",".",".","."],
                        [".",".",".",".",".",".","."],
                        [".",".",".",".",".",".","."],
                        ["e",".","w",".","j",".","r"],
                        [".","d",".",".",".","c","."],
                        ["t",".",".",".",".",".","l"]]
        if play_game_vs_random(heur, deployment, values) == 1:  #heuristic function playing against random
            heur_score += 1
    print("heuristic won :", heur_score, "gmes")
    print(heur)

    '''[[118.08098512948888, 77.84355562131702, 55.594979453344074, 43.762664677759474, 5.299674991346628, 95.59021967270616, 125.10893657550106, 27.799960145479826, 1.9661592296096493, -72.93106422249275, 1866.9932979867006, -491.300605199275], 30]'''

    









































'''
big_score = 0
small_score = 0
for i in range(50):
    print("heur_1",  big_score, "heur_2", small_score)
    values = {"R":1 ,"C":2, "D":3, "W":4, "J":5, "T":6, "L":7, "E":8, "r":1 ,"c":2, "d":3, "w":4, "j":5, "t":6, "l":7, "e":8, "N":0, "n":0}
    board = [[".",".","#","*","#",".","."],
             [".",".",".","#",".",".","."],
             [".",".",".",".",".",".","."],
             [".","~","~",".","~","~","."],
             [".","~","~",".","~","~","."],
             [".","~","~",".","~","~","."],
             [".",".",".",".",".",".","."],
             [".",".",".","#",".",".","."],
             [".",".","#","*","#",".","."]]

    deployment = [["L",".",".",".",".",".","T"],
                  [".","D",".",".",".","C","."],
                  ["R",".","J",".","W",".","E"],
                  [".",".",".",".",".",".","."],
                  [".",".",".",".",".",".","."],
                  [".",".",".",".",".",".","."],
                  ["e",".","w",".","j",".","r"],
                  [".","d",".",".",".","c","."],
                  ["t",".",".",".",".",".","l"]]

    
    X = play_game(example_heur_1, example_heur_2, deployment, values)
    if X == 1:
        big_score += 1
    else:
        small_score += 1

print("heur_1", big_score, "heur_2", small_score)



for i in range(5):
    print("smarter agent score:". small_score, "zad2 agent score:", big_score)
    values = {"R":1 ,"C":2, "D":3, "W":4, "J":5, "T":6, "L":7, "E":8, "r":1 ,"c":2, "d":3, "w":4, "j":5, "t":6, "l":7, "e":8, "N":0, "n":0}
    board = [[".",".","#","*","#",".","."],
             [".",".",".","#",".",".","."],
             [".",".",".",".",".",".","."],
             [".","~","~",".","~","~","."],
             [".","~","~",".","~","~","."],
             [".","~","~",".","~","~","."],
             [".",".",".",".",".",".","."],
             [".",".",".","#",".",".","."],
             [".",".","#","*","#",".","."]]

    deployment = [["L",".",".",".",".",".","T"],
                  [".","D",".",".",".","C","."],
                  ["R",".","J",".","W",".","E"],
                  [".",".",".",".",".",".","."],
                  [".",".",".",".",".",".","."],
                  [".",".",".",".",".",".","."],
                  ["e",".","w",".","j",".","r"],
                  [".","d",".",".",".","c","."],
                  ["t",".",".",".",".",".","l"]]

    conquered = False
    turn = 0
    counter = 0

    
    while not conquered:
    #for i in range(2):
        kill = False
        turn = (turn)%2 + 1
        if counter > 30 or not possible_moves(deployment, turn, values):
            if result(deployment, values) == 1:
                big_score += 1 
            else: 
                small_score += 1   
            break
        
        if deployment[0][3] != ".":
            #print("player 2 small wins!")
            small_score += 1
            break

        if deployment[8][3] != ".":
            #print("player 1 BIG wins!")
            big_score += 1
            break
        

        #print("player", turn)
        if turn == 2:
            if make_move(turn, smarter_agent(deployment, turn, values, counter), deployment, kill, values):
                counter = 0
            
        else:
            
            if make_move(turn, smart_agent(deployment, turn, values), deployment, kill, values):
                counter = 0
        counter += 1


print("smarter agent score:". small_score, "zad2 agent score:", big_score)'''