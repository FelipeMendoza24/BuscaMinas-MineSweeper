# BuscaMinas / Minesweeper
# By: FelipeMendoza24
# First Codecademy Portolio Project

# Class for creating the game
class BuscaMinas:
    def __init__(self, user, rows, columns, level):
        self.user = user
        self.rows = rows
        self.columns = columns
        self.level = level
        self.mines = int(self.defineMines())
        self.board = self.createBoard(self.rows, self.columns)

    def defineMines(self):
        if self.level == 1:
            return self.rows*self.columns*0.3
        elif self.level == 2:
            return self.rows*self.columns*0.5
        elif self.level == 3:
            return self.rows*self.columns*0.6
        
    def createBoard(self, rows, columns):
        board = [["O" for _ in range(columns)] for _ in range(rows)]
        return board
    
    def showBoard(self):
        for row in self.board:
            print(" ".join(row))


class User:
    def __init__(self, name):
        self.name = name
        self.score = 0


# User define the game:

print("Welcome to Busca Minas! \n Please enter your name: ")
name = input()
user1 = User(name)
print("Welcome {}".format(name))

print("We need to set up the board, how many row should it have: ")
rows = int(input())

print("How many columns: ")
columns = int(input())

level = 0
while level != 1 and  level != 2 and level != 3:
    print("Select \"1\" for easy, \"2\" for normal, \"3\" for hard")
    level = int(input())


game = BuscaMinas(user1, rows, columns, level)
game.showBoard()

