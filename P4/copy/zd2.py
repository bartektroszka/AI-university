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


def result():
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
def move(turn, pos_1, pos_2, deployment):
    x1, y1 = pos_1
    x2, y2 = pos_2
    if turn == 1:
        figure = deployment[x1][y1]
        if figure in ["R", "C", "D", "W", "J", "T", "L", "E"] and (x2 != 0 or y2 != 3):
            if abs(x2+y2 - x1 - y1) <=1:
                if figure == "R" and board[x2][y2] == "~":
                    deployment[x2][y2] = figure
                    deployment[x1][y1] = "."
                elif board[x2][y2] == ".":
                    if deployment[x2][y2] == ".":
                        deployment[x2][y2] = figure
                        deployment[x1][y1] = "."
                    elif deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                        if board[x1][y1] != "~":
                            if figure == "R" and deployment[x2][y2] == "e":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                                
                            else:
                                if values[figure] >= values[deployment[x2][y2]]:
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                    
                elif board[x2][y2] == "#":
                    if deployment[x2][y2] == ".":
                        deployment[x2][y2] = figure
                        deployment[x1][y1] = "."
                        values[figure] = 0
                    elif deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                        if figure == "R" and deployment[x2][y2] == "e":
                            deployment[x2][y2] = figure
                            deployment[x1][y1] = "."
                            values[figure] = 0
                        else: 
                            if values[figure] >= values[deployment[x2][y2]]:
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                                values[figure] = 0
                
                elif x2 == 8 and y2 == 3:
                    deployment[x2][y2] = figure
                    deployment[x1][y1] = "."
            
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
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                    elif y2 < y1:
                        trigger = False
                        for i in range(y2+1, y1):
                            if board[x1][i] != "~" or deployment[x1][i] == "r":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                                if figure == "R" and deployment[x2][y2] == "e":
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                elif(y2 == y1 and abs(x2-x1) == 4):
                    if x2 > x1:
                        trigger = False
                        for i in range(x1+1, x2):
                            if board[i][y1] != "~" or deployment[i][y1] == "r":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                                if figure == "R" and deployment[x2][y2] == "e":
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."


                    elif x1 > x2:
                        trigger = False
                        for i in range(x2+1, x1):
                            if board[i][y1] != "~" or deployment[i][y1] == "r":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["r", "c", "d", "w", "j", "t", "l", "e"]:
                                if figure == "R" and deployment[x2][y2] == "e":
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."


    if turn == 2:
        figure = deployment[x1][y1]
        if figure in ["r", "c", "d", "w", "j", "t", "l", "e"] and (x2 != 8 or y2 != 3):
            if abs(x2+y2 - x1 - y1) <=1:
                if figure == "r" and board[x2][y2] == "~":
                    deployment[x2][y2] = figure
                    deployment[x1][y1] = "."
                elif board[x2][y2] == ".":
                    if deployment[x2][y2] == ".":
                        deployment[x2][y2] = figure
                        deployment[x1][y1] = "."
                    elif deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                        if board[x1][y1] != "~":
                            if figure == "r" and deployment[x2][y2] == "E":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                            else:
                                if values[figure] >= values[deployment[x2][y2]]:
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                    
                elif board[x2][y2] == "#":
                    if deployment[x2][y2] == ".":
                        deployment[x2][y2] = figure
                        deployment[x1][y1] = "."
                        values[figure] = 0
                    elif deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                        if figure == "r" and deployment[x2][y2] == "E":
                            deployment[x2][y2] = figure
                            deployment[x1][y1] = "."
                            values[figure] = 0
                        else: 
                            if values[figure] >= values[deployment[x2][y2]]:
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                                values[figure] = 0
                
                elif x2 == 0 and y2 == 3:
                    deployment[x2][y2] = figure
                    deployment[x1][y1] = "."
            
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
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                    elif y2 < y1:
                        trigger = False
                        for i in range(y2+1, y1):
                            if board[x1][i] != "~" or deployment[x1][i] == "R":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                                if figure == "r" and deployment[x2][y2] == "E":
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."
                elif(y2 == y1 and abs(x2-x1) == 4):
                    if x2 > x1:
                        trigger = False
                        for i in range(x1+1, x2):
                            if board[i][y1] != "~" or deployment[i][y1] == "R":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                                if figure == "r" and deployment[x2][y2] == "E":
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."


                    elif x1 > x2:
                        trigger = False
                        for i in range(x2+1, x1):
                            if board[i][y1] != "~" or deployment[i][y1] == "R":
                                trigger = True
                        if not trigger:
                            if deployment[x2][y2] in ["R", "C", "D", "W", "J", "T", "L", "E"]:
                                if figure == "r" and deployment[x2][y2] == "E":
                                    deployment[x2][y2] = figure
                                    deployment[x1][y1] = "."
                                else:
                                    if values[figure] >= values[deployment[x2][y2]]:
                                        deployment[x2][y2] = figure
                                        deployment[x1][y1] = "."
                            elif deployment[x2][y2] == ".":
                                deployment[x2][y2] = figure
                                deployment[x1][y1] = "."         
                
                
def  possible_moves(deployment, turn):
    pos_moves = set()
    for i in range(9):
        for j in range(7):
            if deployment[i][j] in ["R", "C", "D", "W", "J", "E", "r", "c", "d", "w", "j", "e", "T", "L", "t", "l"]:
                figure = deployment[i][j]
                moves_to_check = set()
                for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (i + a) < 9 and (i + a)>= 0 and (j + b)< 7 and(j + b) >= 0:
                        new_move = (i + a, j + b)
                        copy_deployment = copy.deepcopy(deployment)
                        move(turn, (i,j), (new_move), copy_deployment)
                        if copy_deployment != deployment:
                            pos_moves.add(((i,j), new_move))
            
            if deployment[i][j] in ["T", "L", "t", "l"]:
                figure = deployment[i][j]
                moves_to_check = set()
                for a,b in [(4,0),(-4,0),(0,3),(0,-3)]:
                    if (i + a) < 8 and (i + a)>= 0 and (j + b)< 6 and(j + b) >= 0:
                        new_move = (i + a, j + b)
                        copy_deployment = copy.deepcopy(deployment)
                        move(turn, (i,j), (new_move), copy_deployment)
                        if copy_deployment != deployment:
                            pos_moves.add(((i,j), new_move))
    return pos_moves

def draw():
    vis_board = [[] for i in range(9)]
    for i in range(9):
        for j in range(7):
            if deployment[i][j] != ".":
                vis_board[i].append(deployment[i][j])
            else:
                vis_board[i].append(board[i][j])
    for i in range(9):
        print(vis_board[i])



def evaluate(deployment, k):
    counter = k
    player_big_score = 0
    player_small_score = 0
    while counter > 0:
        copy_deployment = copy.deepcopy(deployment)
        turn = 2
        move_counter = 0
        while counter > 0:
            turn = turn%2 + 1
            move_counter +=1
            if move_counter > 30:
                if result() == 1:
                    player_big_score += 1
                    break
                else:
                    player_small_score += 1
                    break
            if deployment[0][3] != ".":
                player_small_score += 1
                break
            if deployment[8][3] != ".":
                player_big_score += 1
                break
            random_move = random.sample(possible_moves(copy_deployment, turn), 1)[0]
            if copy_deployment[random_move[1][0]][random_move[1][1]] in ["R", "C", "D", "W", "J", "E", "r", "c", "d", "w", "j", "e", "T", "L", "t", "l"]:
                move_counter = 0
            move(turn, random_move[0], random_move[1], copy_deployment)
            move_counter += 1
            counter -= 1
    return(player_big_score, player_small_score)

def smart_agent(deployment, turn):
    pos_moves = possible_moves(deployment, turn)
    best_result = -1000000
    best_move = 0
    k = 100//len(pos_moves)
    for pos_move in pos_moves:
        copy_deployment = copy.deepcopy(deployment)
        move(turn, pos_move[0], pos_move[1], copy_deployment)
        if turn == 1:
            b, s = evaluate(copy_deployment, k)
            result = b-s
            if result >= best_result:
                best_result = result
                best_move = pos_move
        elif turn == 2:
            b, s = evaluate(copy_deployment, k)
            result = s-b
            if result >= best_result:
                best_result = result
                best_move = pos_move
    return best_move
        
def random_agent(deployment, turn):
    pos_moves = possible_moves(deployment, turn)
    return random.sample(pos_moves, 1)[0]



conquered = False
turn = 0
counter = 0

for i in range(10):
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
    conquered = False
    turn = 0
    counter = 0

    while not conquered:
        #draw()
        turn = (turn)%2 + 1
        if counter > 300:
            print("player", result(), "wins")
            break
        
        if deployment[0][3] != ".":
            print("player 2 small wins!")
            break

        if deployment[8][3] != ".":
            print("player 1 BIG wins!")
            break
        
        else:
            
            #print("player", turn)
            if turn == 2:
                pos_1, pos_2 = random_agent(deployment, turn)
                if deployment[pos_2[0]][pos_2[1]] in ["R", "C", "D", "W", "J", "E", "r", "c", "d", "w", "j", "e", "T", "L", "t", "l"]:
                    counter = 0
                move(turn, pos_1, pos_2, deployment)
            else:
                pos_1, pos_2 = random_agent(deployment, turn)
                if deployment[pos_2[0]][pos_2[1]] in ["R", "C", "D", "W", "J", "E", "r", "c", "d", "w", "j", "e", "T", "L", "t", "l"]:
                    counter = 0
                move(turn, pos_1, pos_2, deployment)
            counter += 1
