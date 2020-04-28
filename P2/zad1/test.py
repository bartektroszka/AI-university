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

def new_opt_dist(row, deploy): #row = [1,0,0,1,1...] deploy = [2,3,1] .............. [1,0,0,1,0,0,1,1,0] [2,2,1]
    def how_many_moves(list_of_pos):
        final_list = [0 for i in range(len(row))]
        for i in range(len(deploy)):
            for j in range(list_of_pos[i], deploy[i]+list_of_pos[i]) :
                final_list[j] = 1
        counter = 0
        for i in range(len(final_list)):
            if final_list[i] != row[i]:
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

print(new_opt_dist([0,1,0,0,1], [1,2]))
print(new_opt_dist([0,1,0,1,0,0,0,1,1,0], [1,3,2]))
print(new_opt_dist([1,1,0,1,0,1,0,0,1,1], [2,1,1,2]))
print(new_opt_dist([0,0,0,0,0,0,0], [1,2]))
proper_rows = [[3, 3], [2, 4, 2], [1, 2, 1], [1, 1], [2, 2], [3, 3], [3, 3], [6], [4], [2]]
proper_columns = [[5], [2, 3], [1, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [2, 3], [5]]

picture = [[1, 1, 1, 1, 0, 0, 0, 1, 1, 0], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]]
print(bad_rows(picture, proper_rows))
print(bad_columns(picture, proper_columns))
