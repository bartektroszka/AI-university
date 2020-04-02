from fun import *
'''WWWWWW
W.GWWW
W..WWW
W*K..W
W..B.W
W..WWW
WWWWWW'''


def BFS(picture, x_pos, y_pos):
    queue = [[picture, x_pos, y_pos, ""]]
    checked = set()
    def one_step(picture, x_pos, y_pos, history):
        for move in ["U", "R", "D", "L"]:
            new_picture = one_move(picture, x_pos, y_pos, move)[0]
            if possible(picture, move, x_pos, y_pos):
                new_picture, new_x_pos, new_y_pos = one_move(picture, x_pos, y_pos, move)
                new_history = history + move
                if new_picture not in checked:
                    queue.append([new_picture, new_x_pos, new_y_pos, new_history])
                    checked.add(new_picture)
    for poss in queue:
        picture, x_pos, y_pos, history = poss
        if done(picture):
            print(history)
            return 0
        one_step(picture, x_pos, y_pos, history)
    print(queue)


picture = read_map()
height = len(picture)
width = len(picture[0])
for i in range(height):
    for j in range(width):
        if picture[i][j] == "K" or picture[i][j] == "+":
            x_pos = j
            y_pos = i
draw(picture)
while True:
    print("___________________")
    move = input()
    picture, x_pos, y_pos = one_move(picture, x_pos, y_pos, move)[0:3]
    draw(picture)

#BFS(picture, x_pos, y_pos)
#DLURRRDLULLDDRULURUULDRDDRRULDLUU
#DLURRRDLULLDDRULURUULDRDDRRULDLUU