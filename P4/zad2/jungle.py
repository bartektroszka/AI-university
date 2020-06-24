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
                    maks_big = values[deployment[i][j]]
                
    if maks_big > maks_small:
        return 1
    else:
        return 2


#1 player big, 2 player small
def move(turn, x1, y1, x2, y2):
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
                            if deployment[x2][y2] in ["r", "c" "d", "w", "j", "t", "l", "e"]:
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


conquered = False
turn = 0
counter = 0
while not conquered:
    draw()
    turn = (turn)%2 + 1
    if counter > 30:
        print("player", result(), "wins")
        break
    
    if deployment[0][3] != ".":
        print("player 2 small wins!")
        break

    if deployment[8][3] != ".":
        print("player 1 BIG wins!")
        break
    
    else:
        print("player", turn)
        x1, y1, x2, y2 = input().split(" ")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        move(turn, x1, y1, x2, y2)
        counter += 1