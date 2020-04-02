import random
#proper_rows = [2,4,5,1...]
#proper_columns = [blabla...]
#picture = [[], []...] list of rows

def solve(proper_rows, proper_columns):
    length = len(proper_rows)
    picture = [[0  for i in range(length)] for j in range(length)]
    def opt_dist(array, D):
        options = []
        for i in range(len(array) - D + 1):
            number_of_ones_inside = 0
            number_of_ones = 0
            for j in range(D):
                if array[i+j] == 1:
                    number_of_ones_inside += 1
            for j in range(len(array)):
                if array[j] == 1:
                    number_of_ones += 1
            options.append(D - number_of_ones_inside + number_of_ones - number_of_ones_inside)
        return min(options)


    def bad_rows(picture, proper_rows):
        bad = []
        for i in range(len(picture)):
            counter = 0
            for j in range(len(picture)):
                if counter != 0 and picture[i][j] == 0 and counter != proper_rows[i]:
                    bad.append(i)
                    break
                elif picture[i][j] == 1:
                    counter += 1
            if counter != proper_rows[i]:
                bad.append(i)
        return bad

    def bad_columns(picture, proper_columns):
        bad = []
        for i in range(len(picture)):
            counter = 0
            for j in range(len(picture)):
                if counter != 0 and picture[j][i] == 0 and counter != proper_columns[i]:
                    bad.append(i)
                    break
                elif picture[j][i] == 1:
                    counter += 1
            if counter != proper_columns[i]:
                bad.append(i)
        return bad

    def one_step(proper_rows, proper_columns, picture):
        length = len(proper_rows)
        if bad_rows(picture, proper_rows) != []:
            random_row = random.choice(bad_rows(picture, proper_rows))
            first_column = [picture[i][0] for i in range(length)]
            begin_opt = opt_dist(first_column, proper_columns[0]) + opt_dist(picture[random_row], proper_rows[random_row])
            current_diff = 1
            changing = 0
            for i in range(length):
                old_row = [picture[random_row][j] for j in range(length)]
                new_row = [picture[random_row][j] for j in range(length)]
                new_row[i] = (new_row[i] + 1)%2
                old_column = [picture[j][i] for j in range(length)]
                new_column = [picture[j][i] for j in range(length)]
                new_column[random_row] = (new_column[random_row] + 1)%2
                old_opt = opt_dist(old_row, proper_rows[random_row]) + opt_dist(old_column, proper_columns[i])
                difference = opt_dist(new_row, proper_rows[random_row]) + opt_dist(new_column, proper_columns[i]) - old_opt
                if difference < current_diff:
                    current_diff = difference
                    changing = i
            picture[random_row][changing] = (picture[random_row][changing] + 1) % 2
        
        elif bad_columns(picture, proper_columns) != []:
            random_column = random.choice(bad_columns(picture, proper_columns))
            first_row = [picture[0][i] for i in range(length)]
            current_opt = opt_dist(first_row, proper_rows[0]) + opt_dist([picture[i][random_column] for i in range(length)], proper_columns[random_column])
            current_diff = 1
            changing = 0
            for i in range(length):
                old_row = [picture[i][j] for j in range(length)]
                new_row = [picture[i][j] for j in range(length)]
                new_row[random_column] = (new_row[random_column] + 1)%2
                old_column = [picture[j][random_column] for j in range(length)]
                new_column = [picture[j][random_column] for j in range(length)]
                new_column[i] = (new_column[i] + 1)%2
                old_opt = opt_dist(old_row, proper_rows[random_column]) + opt_dist(old_column, proper_columns[i])
                difference = opt_dist(new_row, proper_rows[random_column]) + opt_dist(new_column, proper_columns[i]) - old_opt
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
            print(''.join(row))

    while(bad_columns(picture, proper_columns) != [] or bad_rows(picture, proper_rows) != []):
        picture = [[0  for i in range(length)] for j in range(length)]
        for i in range(1000):
            non_optimal = random.randint(0,100)
            if non_optimal < 10:
                random_row = random.randint(0, length - 1)
                random_column = random.randint(0, length - 1)
                picture[random_row][random_column] = (picture[random_row][random_column] + 1)%2
            elif (bad_columns(picture, proper_columns) != [] or bad_rows(picture, proper_rows) != []):
                one_step(proper_rows, proper_columns, picture)
            else:
                break
    draw(picture)
    return 0

solve([7,5,3,1,1,1,1], [1,2,3,7,3,2,1])  
print("________________")
solve([2,2,7,7,2,2,2], [2,2,7,7,2,2,2])