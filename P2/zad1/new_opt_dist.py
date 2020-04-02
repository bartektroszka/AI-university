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

print(new_opt_dist([1,0,0,1,0,1,0,1,1,0,0,0], [1,2,3])) 

   

                
                