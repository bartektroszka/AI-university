from chess import *
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
def letter_to_number(letter):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    return alphabet.index(letter)

def change(x):
    return (letter_to_number(x[0]), int(x[1])-1)

#def draw(game):

def draw(game):
    board = [["o ","o ","o ","o ","o ","o ","o ","o "] for i in range(8)]
    board[game[1][1]][game[1][0]] = "♚ "
    board[game[2][1]][game[2][0]] = "♔ "
    board[game[3][1]][game[3][0]] = "♜ "
    print("  1 2 3 4 5 6 7 8")
    for i in range(8):
        print(alphabet[i], "".join(board[i]))
    print("")


with open("in.txt") as source:
    open('out.txt', 'w').close()
    for line in source:
        print("______________________")
        lis = line.split()
        if lis[0] == "black":
            b = BFS((8, change(lis[1]), change(lis[3]), change(lis[2]), 0))
            for i in range(len(b)//5):
                draw(b[5*i:5*i+5])

        else:
            b = BFS((8, change(lis[1]), change(lis[3]), change(lis[2]), 1))
            for i in range(len(b)//5):
                draw(b[5*i:5*i+5])