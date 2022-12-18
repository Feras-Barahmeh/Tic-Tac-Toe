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

    @staticmethod
    def removeRepeatNode(grid):
        del grid.childes[0]
        if grid.childes:
            for child in grid.childes:
                child.removeRepeatNode()
        return grid

    def __builtSubTree(self, grid : TreeNode):

        if self.ifShingleFill(grid.board) :
            self.maxDepth = grid.getLevel
            return grid


        if not grid.childes:
            for child in self.__appendChild(grid).childes:
                self.__builtSubTree(child)
            self.__builtSubTree(grid)
        return grid


    def minmax(self, board : list, depth, isComputer):
        if self.ifWinner(board, self.computerMark):
            return -1
        elif self.ifWinner(board, self.personMark):
            return 1
        elif not self.ifTie(board):
            return StatusGame.tie

        

        if isComputer:
            best = float('-inf')

            # Get Possible Move
            coordinates = self.getEmptyPositions(board)
            for coordinate in coordinates:
                child = deepcopy(board)

                child[coordinate[0]][coordinate[1]] = self.personMark

                best = max(best, self.minmax(child, depth + 1, Player.computer.value))
            return best
        else:
            best = float('inf')
            coordinates = self.getEmptyPositions(board)

            for coordinate in coordinates:
                child = deepcopy(board)
                child[coordinate[0]][coordinate[1]] = self.computerMark

                best = min(best, self.minmax(child, depth + 1, Player.human.value))
            return best




    @property
    def bestMove(self):
        bestVal = -1000
        bestMove = (-1, -1)

        for coordinate in self.getEmptyPositions(self.grid):
            child = deepcopy(self.grid)
            child[coordinate[0]][coordinate[1]] = self.personMark

            moveValue = self.minmax(child, 0, Player.human.value) # board, depth, turn Player

            if moveValue > bestVal:
                bestMove = coordinate
                bestVal = moveValue
        return bestMove







# t = AdversarialSearch([
#     ['', 'O', ''],
#     ['', 'X', 'O'],
#     ['', 'O', 'X']], "X")
t = AdversarialSearch([
    ['O', 'O', 'X'],
    ['X', 'X', 'O'],
    ['', '', '']], "X")
print(t.bestMove)

