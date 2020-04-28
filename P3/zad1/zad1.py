'''
9 9
1 1 1
5 1
1 1 1 1
5 1
6 1
7
6
1 3
2 4
4
1 2 1
8
1 4
7 1
5
5
4
6
        #####
        #.#.#
        .###.
        ##.##
        #####
        '''

import copy


def bad_rows(picture, proper_rows):
        bad = []
        for i in range(height):
            row = []
            last = 0
            for j in range(width):
                if picture[i][j] == 1 and (last == 0 or last == 2):
                    last = 1
                    row.append(1)
                elif picture[i][j] == 1 and last == 1:
                    row[-1] += 1
                    last = 1
                else:
                    last = 0
            if row != proper_rows[i]:
                bad.append(i)
        return bad

def bad_columns(picture, proper_columns):
    bad = []
    for i in range(width):
        column = []
        last = 0
        for j in range(height):
            if picture[j][i] == 1 and (last == 0 or last == 2):
                last = 1
                column.append(1)
            elif picture[j][i] == 1 and last == 1:
                column[-1] += 1
                last = 1
            else:
                last = 0
        if column != proper_columns[i]:
            bad.append(i)
    return bad


proper_rows = []
proper_columns = []
with open("zad_input.txt") as file:
    height, width = file.readline().split(" ")
    height = int(height)
    width = int(width)
    for i in range(height):
        proper_rows.append([])
        proper_rows[i] = file.readline().split(" ")
        for j in range(len(proper_rows[i])):
            proper_rows[i][j] = int(proper_rows[i][j])
    for i in range(width):
        proper_columns.append([])
        proper_columns[i] = file.readline().split(" ")
        for j in range(len(proper_columns[i])):
            proper_columns[i][j] = int(proper_columns[i][j])

picture = [[0 for i in range(width)] for j in range(height)]


def all_possibilities(new_row, new_deploy, checked, history, possibilities):
    if new_deploy == []:
        possibilities.append(history)
        return 0
    free_space = 0
    for i in range(len(new_deploy)-1):
        free_space += new_deploy[i+1] + 1
    for i in range(0, len(new_row)- free_space - new_deploy[0] + 1):
        all_possibilities(new_row[i + new_deploy[0] + 1:], new_deploy[1:], checked + i + new_deploy[0] + 1, history + [i + checked], possibilities)
    return possibilities

def all_options(act_row, deploy):
    row = [0 for i in range(len(act_row))]
    possibilities = all_possibilities(row, deploy, 0, [], [])
    for l in range(len(possibilities)):
        possibility = possibilities[l]
        changed_possibility = [2 for i in range(len(row))]
        for i in range(len(possibility)):  #dla każdego bloku
            for j in range(deploy[i]):  
                changed_possibility[possibility[i] + j] = 1
        possibilities[l] = changed_possibility
    
    result = []
    for i in range(len(possibilities)):
        result.append([possibilities[i], 0])
    for i in range(len(act_row)):
        if act_row[i] == 1 or act_row[i] == 2:
            for j in range(len(possibilities)):
                if possibilities[j][i] != act_row[i]:
                    result[j][1] = 1
    possibilities = []
    for i in range(len(result)):
        if result[i][1] == 0:
            possibilities.append(result[i][0])
    return possibilities
            


def save(picture):
    file = open("zad_output.txt", "w")
    for i in range(height):
        row = []
        for j in range(width):
            row.append(str(picture[i][j]))
        for j in range(width):
            if row[j] == "1":
                row[j] = "#"
            else:
                row[j] = "."
        file.write(''.join(row))
        file.write("\n")

#2 -pola białe, które muszą pozostać puste
while bad_columns(picture, proper_columns) != [] or bad_rows(picture, proper_rows) != []:
    for i in range(height):
        row = picture[i]
        possibilities = all_options(row, proper_rows[i])
        new_row = possibilities[0]
        for j in range(1, len(possibilities)):
            for k in range(width):
                if (new_row[k] == 1 and possibilities[j][k] == 2) or (new_row[k] == 0 and possibilities[j][k] == 1) or (new_row[k] == 2 and possibilities[j][k] == 1):
                    new_row[k] = -1
        for j in range(width):
            if new_row[j] != -1:
                picture[i][j] = new_row[j]
            

    for i in range(width):
        column = []
        for j in range(height):
            column.append(picture[j][i])
        possibilities = all_options(column, proper_columns[i])
        new_column = possibilities[0]

        for j in range(1, len(possibilities)):
            for k in range(height):
                if (new_column[k] == 1 and possibilities[j][k] == 2) or (new_column[k] == 0 and possibilities[j][k] == 1) or (new_column[k] == 2 and possibilities[j][k] == 1):
                    new_column[k] = -1
        for j in range(height):
            if new_column[j] != -1:
                picture[j][i] = new_column[j]

save(picture)