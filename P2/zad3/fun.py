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


