import random
from copy import deepcopy
from AbstractAction import *
from Shingle import *
from random import randint
from GeneralTree import *

class AdversarialSearch(AbstractActions):
    def __init__(self, grid : list, mark):
        super().__init__()
        self.computerMark = mark
        self.personMark = 'X' if mark == 'O' else 'O'
        self.grid = grid; self.playerTurn = Player.computer
        self.maxDepth = None


    @staticmethod
    def getEmptyPositions(shingle : list):
        return [(int(x), int(y)) for x, row in enumerate(shingle) for y, symbol in enumerate(row) if symbol == '']

    def __utility(self, grid : list):
        if self.ifWinner(grid, self.computerMark):
            return StatusGame.win
        elif self.ifWinner(grid, self.personMark):
            return StatusGame.lose
        else:
            return StatusGame.tie


    @property
    def __switchPlayer(self):
        self.playerTurn = Player.human if self.playerTurn.value == Player.computer.value else Player.computer
        return self.playerTurn

    @property
    def __setMark(self):
        return self.computerMark if self.playerTurn.value == Player.computer.value else self.personMark


    def __appendChild(self, root : TreeNode):
        coordinates = self.getEmptyPositions(root.board)
        for coordinate in coordinates:
            newNode = deepcopy(root)
            newNode.board[coordinate[0]][coordinate[1]] = self.__setMark
            newNode.status = self.__utility(newNode.board)
            root.addChild(newNode)
            if self.ifShingleFill(root.board):
                return root
        self.playerTurn = self.__switchPlayer
        return root


    def __builtSubTree(self, grid : TreeNode):
        if self.ifShingleFill(grid.board) :
            self.maxDepth = grid.getLevel
            return grid
        grid = self.__appendChild(grid)
        for child in grid.childes:
            self.__builtSubTree(child)
        return grid

    def minmax(self, board, ):
        pass


    @property
    def bestMove(self):
        if self.ifShingleFill(self.grid): return None

        root = deepcopy(self.grid)
        root = TreeNode(root)
        tree = self.__builtSubTree(root)

        tree.displayTree()







# t = AdversarialSearch([
#     ['', 'O', ''],
#     ['', 'X', 'O'],
#     ['', 'O', 'X']], "X")
t = AdversarialSearch([
    ['O', 'O', 'X'],
    ['X', 'X', 'O'],
    ['', '', 'X']], "O")
print(t.bestMove)

