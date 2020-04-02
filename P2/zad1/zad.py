import random
#proper_rows = [[2],[4,5],1...] list of deploys
#proper_columns = [blabla...]
#picture = [[], []...] list of rows



def solve(proper_rows, proper_columns):
    length = len(proper_rows)
    picture = [[0  for i in range(length)] for j in range(length)]
    def new_opt_dist(row, deploy): #row = [1,0,0,1,1...] deploy = [2,3,1] .............. [1,0,0,1,0,0,1,1,0] [2,2,1]
        def how_many_moves(list_of_pos):
            checked = 0
            counter = 0
            for i in range(len(list_of_pos)):
                for j in range(checked, list_of_pos[i]):
                    if row[j] == 1:
                        counter += 1
                for j in range(list_of_pos[i], list_of_pos[i] + deploy[i]):
                    if row[j] != 1:
                        counter += 1
                if row[list_of_pos[i] + deploy[i]-1] == 1:
                    counter += 1
                checked = list_of_pos[i] + deploy[i] + 1
            for i in range(checked, len(row)):
                if row[i] == 1:
                    counter += 1
            return counter

        possibilities = []
        def all_possibilities(new_row, new_deploy, checked, history):
            if new_deploy == []:
                possibilities.append(history)
                return 0
            free_space = 0
            for i in range(len(new_deploy)-1):
                free_space += new_deploy[i+1] + 1
            for i in range(0, len(new_row)- free_space - new_deploy[0] + 1):
                all_possibilities(new_row[i + new_deploy[0] + 1:], new_deploy[1:], checked + i + new_deploy[0] + 1, history + [i + checked])

        all_possibilities(row, deploy, 0, [])
        minimum = len(row)
        for poss in possibilities:
            if how_many_moves(poss) < minimum:
                minimum = how_many_moves(poss)
        return minimum


    def bad_rows(picture, proper_rows):
        bad = []
        for i in range(len(picture)):
            row = []
            last = 0
            for j in range(len(picture)):
                if picture[i][j] == 1 and last == 0:
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
        for i in range(len(picture)):
            column = []
            last = 0
            for j in range(len(picture)):
                if picture[j][i] == 1 and last == 0:
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

    def one_step(proper_rows, proper_columns, picture):
        length = len(proper_rows)
        if bad_rows(picture, proper_rows) != []:
            random_row = random.choice(bad_rows(picture, proper_rows))
            first_column = [picture[i][0] for i in range(length)]
            begin_opt = new_opt_dist(first_column, proper_columns[0]) + new_opt_dist(picture[random_row], proper_rows[random_row])
            current_diff = 1
            changing = 0
            for i in range(length):
                old_row = [picture[random_row][j] for j in range(length)]
                new_row = [picture[random_row][j] for j in range(length)]
                new_row[i] = (new_row[i] + 1)%2
                old_column = [picture[j][i] for j in range(length)]
                new_column = [picture[j][i] for j in range(length)]
                new_column[random_row] = (new_column[random_row] + 1)%2
                old_opt = new_opt_dist(old_row, proper_rows[random_row]) + new_opt_dist(old_column, proper_columns[i])
                difference = new_opt_dist(new_row, proper_rows[random_row]) + new_opt_dist(new_column, proper_columns[i]) - old_opt
                if difference < current_diff:
                    current_diff = difference
                    changing = i
            picture[random_row][changing] = (picture[random_row][changing] + 1) % 2
        
        elif bad_columns(picture, proper_columns) != []:
            random_column = random.choice(bad_columns(picture, proper_columns))
            first_row = [picture[0][i] for i in range(length)]
            current_opt = new_opt_dist(first_row, proper_rows[0]) + new_opt_dist([picture[i][random_column] for i in range(length)], proper_columns[random_column])
            current_diff = 1
            changing = 0
            for i in range(length):
                old_row = [picture[i][j] for j in range(length)]
                new_row = [picture[i][j] for j in range(length)]
                new_row[random_column] = (new_row[random_column] + 1)%2
                old_column = [picture[j][random_column] for j in range(length)]
                new_column = [picture[j][random_column] for j in range(length)]
                new_column[i] = (new_column[i] + 1)%2
                old_opt = new_opt_dist(old_row, proper_rows[random_column]) + new_opt_dist(old_column, proper_columns[i])
                difference = new_opt_dist(new_row, proper_rows[random_column]) + new_opt_dist(new_column, proper_columns[i]) - old_opt
                if difference < current_diff:
                    current_diff = difference
                    changing = i
            picture[changing][random_column] = (picture[changing][random_column] + 1) % 2
        else:
            pass
    
    def draw(picture):
        for i in range(length):
            row = []
            for j in range(length):
                row.append(str(picture[i][j]))
            for j in range(length):
                if row[j] == "1":
                    row[j] = "#"
                else:
                    row[j] = " "
            print(''.join(row))

    while(bad_columns(picture, proper_columns) != [] or bad_rows(picture, proper_rows) != []):
        picture = [[0  for i in range(length)] for j in range(length)]
        for i in range(2000):
            non_optimal = random.randint(0,100)
            if non_optimal < 5:
                random_row = random.randint(0, length - 1)
                random_column = random.randint(0, length - 1)
                picture[random_row][random_column] = (picture[random_row][random_column] + 1)%2
            elif (bad_columns(picture, proper_columns) != [] or bad_rows(picture, proper_rows) != []):
                one_step(proper_rows, proper_columns, picture)
            else:
                break
        draw(picture)
    return 0

proper_rows = []
proper_columns = []
size = input()
size = size[:2]
size = int(size)
for i in range(size):
    proper_rows.append([])
    proper_rows[i] = input().split(" ")
    for j in range(len(proper_rows[i])):
        proper_rows[i][j] = int(proper_rows[i][j])
for i in range(size):
    proper_columns.append([])
    proper_columns[i] = input().split(" ")
    for j in range(len(proper_columns[i])):
        proper_columns[i][j] = int(proper_columns[i][j])



solve(proper_rows, proper_columns)  
print("________________")


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
'''