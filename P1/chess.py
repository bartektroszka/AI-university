class Board:
    def __init__(self, size,whitefigures, blackfigures, whiteking, blackking):
        self.size = size
        self.board = [[] for i in range(self.size)]
        self.whitefigures = whitefigures
        self.blackfigures = blackfigures
        self.whiteking = whiteking
        self.blackking = blackking
        for i in range(self.size):
            for j in range(self.size):
                self.board[i].append((j+i)%2)

    def CheckForWhite(self, movex, movey):
        for figure2 in self.whitefigures:
            if figure2.PosMove((self.blackking.posx + movex), self.blackking.posy + movey):
                return True
        if self.whiteking.PosMove(self.blackking.posx + movex, self.blackking.posy + movey):
            return True
        return False

    def CheckForBlack(self, movex, movey):
        if self.blackking.PosMove(self.blackking.posx + movex, self.blackking.posy + movey):
            return True
        return False


    def CheckMForWhite(self):
        for i in range(3):
            for j in range(3):
                if (0<=1-i<self.size and 0<=1-j<self.size):
                    if not self.CheckForWhite(self, 1 - i, 1 - j):
                        return False
        return True
                    

class Figure:
    def __init__(self, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color

class Rook(Figure):
    def PosMove(self, x,y):
        if (x == self.posx or y == self.posy) and (x != self.posx or y != self.posy):
            return True
        return False

    def Move(self, x,y):
        if self.PosMove(x,y):
            self.posx = x
            self.posy = y
        
    
class Blackking(Figure):
    def PosMove(self, x, y):
        if abs(self.posx - x) <= 1 and abs(self.posy - y) <=1:
            if not self.board.CheckForWhite(x - self.posx, y - self.posy):
                return True
        return False

    def Move(self, x,y):
        if self.PosMove(x,y):
            self.posx = x
            self.posy = y

class Whiteking(Figure):
    def PosMove(self, x, y):
        if abs(self.posx - x) <= 1 and abs(self.posy - y) <=1:
            if not self.board.CheckForBlack(x - self.posx, y - self.posy):
                return True
        return False

    def Move(self, x,y):
        if self.PosMove(x,y):
            self.posx = x
            self.posy = y