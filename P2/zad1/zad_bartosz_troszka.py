import random
#proper_rows = [[2],[4,5],1...] list of deploys
#proper_columns = [blabla...]
#picture = [[], []...] list of rows



def solve(proper_rows, proper_columns):
    height = len(proper_rows)
    width = len(proper_columns)
    picture = [[random.randint(0,1)  for i in range(width)] for j in range(height)]
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


    def bad_rows(picture, proper_rows):
        bad = []
        for i in range(height):
            row = []
            last = 0
            for j in range(width):
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
        for i in range(width):
            column = []
            last = 0
            for j in range(height):
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
#PODEJRZANA STREFA
####################################################################
    def one_step(proper_rows, proper_columns, picture):
        if bad_rows(picture, proper_rows) != []:
            random_row = random.choice(bad_rows(picture, proper_rows))    
            current_diff = 40           #ta liczba na pewno bedzie mniejsza w przyszłości
            changing = 0                #aktualnie najlepsza kolumna
            for i in range(width):         #sprawdzamy po kolei kolumny
                old_row = [picture[random_row][j] for j in range(width)]
                new_row = [picture[random_row][j] for j in range(width)] #wiersz po zmianie
                new_row[i] = (new_row[i] + 1)%2
                old_column = [picture[j][i] for j in range(height)]
                new_column = [picture[j][i] for j in range(height)]     #kolumna po zmianie
                new_column[random_row] = (new_column[random_row] + 1)%2
                difference = new_opt_dist(new_row, proper_rows[random_row]) + new_opt_dist(new_column, proper_columns[i]) - new_opt_dist(old_row, proper_rows[random_row]) - new_opt_dist(old_column, proper_columns[i])  #różnica w optymalności danego wiersza i kolumny po zmianie, im mniejsza tym lepsza
                if difference < current_diff: #jeśli jest mniejsza niż dotychczasowa najmniejsza to znaczy że jest lepsza
                    current_diff = difference
                    changing = i
            picture[random_row][changing] = (picture[random_row][changing] + 1) % 2
        
        elif bad_columns(picture, proper_columns) != []:
            random_column = random.choice(bad_columns(picture, proper_columns))
            current_diff = 40
            changing = 0
            for i in range(height):
                old_row = [picture[i][j] for j in range(width)]
                new_row = [picture[i][j] for j in range(width)]
                new_row[random_column] = (new_row[random_column] + 1)%2
                old_column = [picture[j][random_column] for j in range(height)]
                new_column = [picture[j][random_column] for j in range(height)]
                new_column[i] = (new_column[i] + 1)%2
                difference = new_opt_dist(new_row, proper_rows[i]) + new_opt_dist(new_column, proper_columns[random_column]) - new_opt_dist(old_row, proper_rows[i]) - new_opt_dist(old_column, proper_columns[random_column])
                if difference < current_diff:
                    current_diff = difference
                    changing = i
            picture[changing][random_column] = (picture[changing][random_column] + 1) % 2
        else:
            pass
#######################################################################################  
    def draw(picture):
        for i in range(height):
            row = []
            for j in range(width):
                row.append(str(picture[i][j]))
            for j in range(width):
                if row[j] == "1":
                    row[j] = "#"
                else:
                    row[j] = " "
            print(''.join(row))
        print()    

    while(bad_columns(picture, proper_columns) != [] or bad_rows(picture, proper_rows) != []):
        picture = [[random.randint(0,1)  for i in range(width)] for j in range(height)]
        for i in range(5 * width * height):
            non_optimal = random.randint(0,100)
            if non_optimal < 1:
                random_row = random.randint(0, height - 1)
                random_column = random.randint(0, width - 1)
                picture[random_row][random_column] = (picture[random_row][random_column] + 1)%2
            elif (bad_columns(picture, proper_columns) != [] or bad_rows(picture, proper_rows) != []):
                one_step(proper_rows, proper_columns, picture)
            else:
                break
            
        draw(picture)
    return 0

"""
proper_rows = []
proper_columns = []
height, width = input().split(" ")
height = int(height)
width = int(width)
for i in range(height):
    proper_rows.append([])
    proper_rows[i] = input().split(" ")
    for j in range(len(proper_rows[i])):
        proper_rows[i][j] = int(proper_rows[i][j])
for i in range(width):
    proper_columns.append([])
    proper_columns[i] = input().split(" ")
    for j in range(len(proper_columns[i])):
        proper_columns[i][j] = int(proper_columns[i][j])

   ...####...
    ..######..
    .###.####.
    ####.#####
    ####.#####
    #####.####
    .#####.##.
    ..######..
    ..######..
    ..##..##..    
"""


solve([[5],[1,1,1],[3],[2,2],[5]],
    [[2,2],[1,3],[3,1],[1,3],[2,2]])
    
solve( [[4], [6], [3,4], [4,5], [4,5], [5,4], [5,2], [6], [6], [2,2]], 
       [[3], [5], [9], [10], [2,4], [5,3], [6,3], [9], [5], [3]])
solve( [[3,3], [2,4,2], [1,2,1], [1,1], [2,2], [3,3], [3,3], [6], [4], [2]], 
  [[5], [2,3], [1,3], [2,3], [2,3], [2,3], [2,3], [1,3], [2,3], [5]] ) #serce
  
solve([[4],[1,1,6],[1,1,6],[1,1,6],[4,9],[1,1],[1,1],[2,7,2],[1,1,1,1],[2,2]],
    [[4],[1,2],[1,1],[5,1],[1,2],[1,1],[5,1],[1,1],[4,1],[4,1],[4,2],[4,1],[4,1],[4,2],[4]])

solve( [ [5], [9], [5,5], [13], [3,5,3], [15], [1,5,5,1], [15], [2,2], [2,2], [1,1], [1,1], [1,1], [2,2], [5]], [[3], [3,1], [6], [7], [3,3,5], [10,2], [9,1], [2,3,1,1], [9,1], [10,2], [3,3,5], [7], [6], [3,1], [3]])    

solve(
[[5],[2,2],[1,1],[1,1],[4,4],[2,2,1,2],[1,3,1],[1,1,1,1],[2,7,2],[4,1,5],[2,1,1],[1,1,2],[1,1,1],[2,5,2],[3,4]],
    [[4],[2,2],[1,5],[1,2,2],[5,2,1],[2,1,1,2],[1,3,1],[1,1,6],[1,3,1],[2,1,2,2],[4,2,1],[1,1,1],[1,3,2],[2,2,3],[4]])     


solve( [[4],[2,2],[2,2],[2,4,2],[2,1,1,2],[2,4,2],[1,2],[4,4,4],[1,1,1,1,1,1],[4,1,1,4],[1,1,1],[1,1,3],[10],[2,1],[4,1]],
    [[5,1],[2,1,1,1],[2,1,1,2],[2,3,3],[2,1],[2,3,6],[1,1,1,1,1],[1,1,1,1,1],[2,3,6],[2,1],[2,3,1],[2,1,1,1],[2,1,1,4],[7],[1,1]])  

   
