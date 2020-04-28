#from fun import *
from queue import PriorityQueue
def read_map():
    picture =[]
    file_handle = open('zad_input.txt')
    counter = 0   # this doesn't change file_name, but it does output something new (let's call that file_handle)
    for line in file_handle:
        if counter == 0:
            stopper = line
            picture.append(stopper)
            counter = 1
        else:
            row = line
            picture.append(row)

    file_handle.close() 
    return picture


def one_move(picture, x_pos, y_pos, move):
    new_picture = unconvert(picture)
    if move == 'U':
        move = (0,-1)
    elif move == 'R':
        move = (1,0)
    elif move == 'D':
        move = (0,1)
    elif move == 'L':
        move = (-1,0)
    
    new_x_pos = x_pos
    new_y_pos = y_pos
    new_x_pos += move[0]
    new_y_pos += move[1]
    moved_x_pos  = new_x_pos
    moved_y_pos = new_y_pos
    moved_x_pos += move[0]
    moved_y_pos += move[1]
    if new_picture[new_y_pos][new_x_pos] == "W":
        return [convert(new_picture), x_pos, y_pos]
    if new_picture[new_y_pos][new_x_pos] == ".":
        if new_picture[y_pos][x_pos] == "+":
            new_picture[new_y_pos][new_x_pos] = "K"
            new_picture[y_pos][x_pos] = "G"
            return [convert(new_picture), new_x_pos, new_y_pos]
        else:
            new_picture[new_y_pos][new_x_pos] = "K"
            new_picture[y_pos][x_pos] = "."
            return [convert(new_picture), new_x_pos, new_y_pos]
    if new_picture[new_y_pos][new_x_pos] == "G":
        if new_picture[y_pos][x_pos] == "+":
            new_picture[new_y_pos][new_x_pos] = "+"
            new_picture[y_pos][x_pos] = "G"
            return [convert(new_picture), new_x_pos, new_y_pos]
        else:
            new_picture[new_y_pos][new_x_pos] = "+"
            new_picture[y_pos][x_pos] = "."
            return [convert(new_picture), new_x_pos, new_y_pos]

    if new_picture[new_y_pos][new_x_pos] == "B" or new_picture[new_y_pos][new_x_pos] == "*":
        if new_picture[moved_y_pos][moved_x_pos] in  ["W", "B", "*"]:
            return [convert(new_picture), x_pos, y_pos]
        elif new_picture[moved_y_pos][moved_x_pos] == ".":
            new_picture[moved_y_pos][moved_x_pos] = "B"
            if new_picture[new_y_pos][new_x_pos] == "B":
                new_picture[new_y_pos][new_x_pos] = "K"
                if new_picture[y_pos][x_pos] == "K":
                    new_picture[y_pos][x_pos] = "."
                    return [convert(new_picture), new_x_pos, new_y_pos]
                elif new_picture[y_pos][x_pos] == "+":
                    new_picture[y_pos][x_pos] = "G"
                    return [convert(new_picture), new_x_pos, new_y_pos]
            elif new_picture[new_y_pos][new_x_pos] == "*":
                new_picture[new_y_pos][new_x_pos] = "+"
                if new_picture[y_pos][x_pos] == "K":
                    new_picture[y_pos][x_pos] = "."
                    return [convert(new_picture), new_x_pos, new_y_pos]
                elif new_picture[y_pos][x_pos] == "+":
                    new_picture[y_pos][x_pos] = "G"
                    return [convert(new_picture), new_x_pos, new_y_pos]
        elif new_picture[moved_y_pos][moved_x_pos] == "G":
            new_picture[moved_y_pos][moved_x_pos] = "*"
            if new_picture[new_y_pos][new_x_pos] == "B":
                new_picture[new_y_pos][new_x_pos] = "K"
                if new_picture[y_pos][x_pos] == "K":
                    new_picture[y_pos][x_pos] = "."
                    return [convert(new_picture), new_x_pos, new_y_pos]
                elif new_picture[y_pos][x_pos] == "+":
                    new_picture[y_pos][x_pos] = "G"
                    return [convert(new_picture), new_x_pos, new_y_pos]
            elif new_picture[new_y_pos][new_x_pos] == "*":
                new_picture[new_y_pos][new_x_pos] = "+"
                if new_picture[y_pos][x_pos] == "K":
                    new_picture[y_pos][x_pos] = "."
                    return [convert(new_picture), new_x_pos, new_y_pos]
                elif new_picture[y_pos][x_pos] == "+":
                    new_picture[y_pos][x_pos] = "G"
                    return [convert(new_picture), new_x_pos, new_y_pos]
    return [convert(new_picture), new_x_pos, new_y_pos]


def draw(picture):
    for i in range(len(picture)):
        print(picture[i])


def done(picture):
    picture = unconvert(picture)
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            if picture[i][j] == "B" or picture[i][j] == "+":
                return False
    return True

def possible(picture, move, x_pos, y_pos):
    picture = unconvert(picture)
    if move == 'U':
        move = (0,-1)
    elif move == 'R':
        move = (1,0)
    elif move == 'D':
        move = (0,1)
    elif move == 'L':
        move = (-1,0)
    new_x_pos = x_pos
    new_y_pos = y_pos
    new_x_pos += move[0]
    new_y_pos += move[1]
    moved_x_pos  = new_x_pos
    moved_y_pos = new_y_pos
    moved_x_pos += move[0]
    moved_y_pos += move[1]
    if picture[new_y_pos][new_x_pos] == "W":
        return False
    if picture[new_y_pos][new_x_pos] == "B" or picture[new_y_pos][new_x_pos] == "*":
        if picture[moved_y_pos][moved_x_pos] in  ["W", "B", "*"]:
            return False
    return True


def convert(picture):
    result = ()
    for i in range(len(picture)):
        result += ("".join(picture[i]),)
    return result

def unconvert(picture):
    result = []
    for i in range(len(picture)):
        result.append(list(picture[i]))
    return result



















'''
WWWWWW
W.GWWW
W..WWW
W*K..W
W..B.W
W..WWW
WWWWWW
'''

'''
WWWWWWWW
W.....WW
WKBBB.WW
W..WGGGW
WW....WW
WWWWWWWW
'''

'''
WWWWWWWWWWWW
WWWWWW.WWWWW
W....WWW...W
W.BB.....WKW
W.B.WGGG...W
W...WWWWWWWW
WWWWWWWWWWWW
'''

def heur(picture, x_pos, y_pos):
    result = 0
    height = len(picture)
    width = len(picture[0])
    copy = []
    for i in range(height):
        copy.append([])
        for j in range(width):
            copy[i].append(picture[i][j])
    for i in range(height):
        for j in range(width):
            if copy[i][j] == "B":
                box_position = (i,j)
                list_of_goals = []
                minimum = 30
                closest_box = []
                for k in range(height):
                    for l in range(width):
                        if copy[k][l] == "G" or copy[k][l] == "+":
                            list_of_goals.append((k,l))
                for goal in list_of_goals:
                    if abs(box_position[0] - goal[0]) + abs(box_position[1] - goal[1]) < minimum:
                        minimum = abs(box_position[0] - goal[0]) + abs(box_position[1] - goal[1])
                        closest_box = (goal[0], goal[1])
                result += minimum
                copy[i][j] = "D"
                copy[closest_box[0]][closest_box[1]] = "D"
    return result              



'''
WWWWWWWW
W.....WW
WKBBB.WW
W..WGGGW
WW....WW
WWWWWWWW
        '''


def Algo(picture, x_pos, y_pos):
    queue = PriorityQueue()
    queue.put((heur(picture, x_pos, y_pos), [picture, x_pos, y_pos, "", 0]))
    checked = set()
    def one_step(picture, x_pos, y_pos, history, cost):
        for move in ["U", "R", "D", "L"]:
            new_picture = one_move(picture, x_pos, y_pos, move)[0]
            if possible(picture, move, x_pos, y_pos):
                new_picture, new_x_pos, new_y_pos = one_move(picture, x_pos, y_pos, move)
                new_history = history + move
                if new_picture not in checked:
                    queue.put((cost + heur(new_picture, new_x_pos, new_y_pos), [new_picture, new_x_pos, new_y_pos, new_history, cost + 1]))
                    checked.add(new_picture)
    while not queue.empty():
        picture, x_pos, y_pos, history, cost = queue.get()[1]
        if done(picture):
            #print(history)
            f = open("zad_output.txt", "a")
            f.write(history)
            f.close()
            #print(len(history))
            return 0
        one_step(picture, x_pos, y_pos, history, cost)
    print(queue)

picture = read_map()
height = len(picture)
width = len(picture[0])
for i in range(height):
    for j in range(width):
        if picture[i][j] == "K" or picture[i][j] == "+":
            x_pos = j
            y_pos = i
'''
while True:
    print("___________________")
    move = input()
    picture, x_pos, y_pos = one_move(picture, x_pos, y_pos, move)[0:3]
    print(heur(picture, x_pos, y_pos))
    draw(picture)
    '''
Algo(picture, x_pos, y_pos)
