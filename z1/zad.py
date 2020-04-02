from random import randint, shuffle

def deploy_queen(N):
    positions = [0 for i in range(N)] #[psitions of queens in columns]
    rows = [[i, 0] for i in range(N)]
    diagonals_1 = [0 for i in range(2*N - 1)] # /
    diagonals_2 = [0 for i in range(2*N - 1)] # \
    stopper = 0
    while stopper == 0:
        counter = N
        for i in range(N):
            shuffle(rows)
            stop = 0
            for j in range(N):
                if rows[j][1] == 0 and diagonals_1[rows[j][0] + i] == 0 and diagonals_2[N - 1 - rows[j][0] + i] == 0:
                    rows[j][1] = 1
                    positions[i] = rows[j][0]
                    diagonals_1[rows[j][0] + i] = 1
                    diagonals_2[N - 1 - rows[j][0] + i] = 1
                    counter -= 1
                    stop += 1
                    break
            if stop == 0:
                positions = [0 for i in range(N)] #[psitions of queens in columns]
                rows = [[i, 0] for i in range(N)]
                diagonals_1 = [0 for i in range(2*N - 1)] # /
                diagonals_2 = [0 for i in range(2*N - 1)] # \
                break
        if counter == 0:
            stopper = 1
    print(positions)

deploy_queen(200)



