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
            if move_counter > 100:
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
    heurr = [44.41295918096485, 77.00264196969565, 60, 54, 33, 49, 100, 93, 10, -17, 932, -613]
    summ = 0
    for i in range(9):
        for j in range(7):
            figure = deployment[i][j]
            if figure in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                if board[i][j] == "*" and i>3:
                    summ = heurr[10]
                    return summ
                summ -= ((8 - i) + abs(3 - j)) * heurr[8]
                if board[i][j] == "#" and i < 5:
                    summ += heurr[9]
                summ += heurr[["R", "C", "D", "W", "J", "T", "L", "E"].index(figure)]


            elif figure in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                if board[i][j] == "*" and i<5:
                    summ = heurr[11]
                    return summ
                summ += (abs(0 - i) + abs(3 - j)) * heurr[8]
                if board[i][j] == "#" and i >3:
                    summ -= heurr[9]
                summ -= heurr[["r", "c", "d", "w", "j", "t", "l", "e"].index(figure)]
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


        
big_score = 0
small_score = 0
for i in range(100):
    print("smarter agent score:",  big_score, "zad2 agent score:", small_score)
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
        if counter > 100 or not possible_moves(deployment, turn, values):
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
            if make_move(turn, smart_agent(deployment, turn, values), deployment, kill, values):
                counter = 0
            
        else:
            
            if make_move(turn, smarter_agent(deployment, turn, values, counter), deployment, kill, values):
                counter = 0
        counter += 1

print("smarter agent score:", big_score, "zad2 agent score:", small_score)
