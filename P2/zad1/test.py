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

proper_rows = [[3, 3], [2, 4, 2], [1, 2, 1], [1, 1], [2, 2], [3, 3], [3, 3], [6], [4], [2]]
proper_columns = [[5], [2, 3], [1, 3], [2, 3], [2, 3], [2, 3], [2, 3], [1, 3], [2, 3], [5]]

picture = [[1, 1, 1, 1, 0, 0, 0, 1, 1, 0], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]]
print(bad_rows(picture, proper_rows))
print(bad_columns(picture, proper_columns))
####   ## 
# ########
## ###  ##
#        #
##      ##
####   ###
  ### ##  
 ######   
   ####   
   ##     

.###..###.
##.####.##
#...##...#
#........#
##......##
###....###
.###..###.
..######..
...####...
....##....