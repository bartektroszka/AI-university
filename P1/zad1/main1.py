from chess import *

def letter_to_number(letter):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    return alphabet.index(letter)

def change(x):
    return (letter_to_number(x[0]), int(x[1])-1)

#def draw(game):



with open("in.txt") as source:
    open('out.txt', 'w').close()
    for line in source:
        lis = line.split()
        if lis[0] == "black":
            with open('out.txt', 'a') as out:
                out.write(str(len(BFS((8, change(lis[1]), change(lis[2]), change(lis[3]), 0)))//5))
                out.write("\n")
        else:
            with open('out.txt', 'a') as out:
                out.write(str(len(BFS((8, change(lis[1]), change(lis[2]), change(lis[3]), 1)))//5))
                out.write("\n")
