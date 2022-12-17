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
        self.result = {}

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

    @staticmethod
    def __simulationPlay(board : list, coordinate):
        board = board[coordinate[0]][coordinate[1]]
        return board

    @property
    def __switchPlayer(self):
        self.playerTurn = Player.human if self.playerTurn.value == Player.computer.value else Player.computer
        return self.playerTurn

    @property
    def __setMark(self):
        return self.computerMark if self.playerTurn.value == Player.computer.value else self.personMark

    @staticmethod
    def __chooseMove(statistics):
        maxVal = statistics[0]["win"]
        coor = statistics[0]["coordinate"]
        for statistic in statistics:
            if statistic["win"] > maxVal:
                maxVal = statistic["win"]
                coor = statistic["coordinate"]
        return coor

    def __getStatistics(self, board):
        if board.status == StatusGame.win:
            self.result["win"] += 1
        elif board.status == StatusGame.lose:
            self.result["lose"] += 1
        else:
            self.result["tie"] += 1

        for child in board.childes:
            self.__getStatistics(child)

        return self.result

    def __appendChild(self, root : TreeNode):
        coordinates = self.getEmptyPositions(root.board)
        for coordinate in coordinates:
            newNode = deepcopy(root)
            newNode.board[coordinate[0]][coordinate[1]] = self.__setMark
            newNode.status = self.__utility(newNode.board)
            root.addChild(newNode)
        self.playerTurn = self.__switchPlayer
        return root

    @staticmethod
    def removeRepeatNode(grid):
        del grid.childes[0]
        if grid.childes:
            for child in grid.childes:
                child.r()
        return grid
    def __builtSubTree(self, grid : TreeNode):
        if not self.ifShingleFill(grid.board) :
            grid = self.__appendChild(grid)
            for child in grid.childes:
                self.__builtSubTree(child)
        else:
            grid = self.removeRepeatNode(grid)

        return grid

    @staticmethod
    def getFillBlock(shingle):
        counter = 0
        for i in shingle:
            for j in i:
                counter += j.count('X')
                counter += j.count('O')
        return counter

    @property
    def bestMove(self):
        statistics = []; coordinates = None
        if self.ifShingleFill(self.grid): return None
        coordinates = self.getEmptyPositions(self.grid)
        if self.getFillBlock(self.grid) <= 4:
            return random.choice(coordinates)


        for coordinate in coordinates:
            newChild = deepcopy(self.grid)

            newChild[coordinate[0]][coordinate[1]] = self.computerMark
            self.playerTurn = Player.human
            parent = TreeNode(newChild)
            self.result["coordinate"] = coordinate
            self.result["win"] = 0
            self.result["lose"] = 0
            self.result["tie"] = 0

            parent = self.__builtSubTree(parent)
            parent.displayTree()
            values = self.__getStatistics(parent)

            statistics.append(values)
            self.result = {}
            break
        return self.__chooseMove(statistics)

    def ifShingleFill(self, shingle=None):
        shingle = shingle if shingle else self.grid
        for i in shingle:
            if filter(lambda e: e == '', i):
                return False
        return True


# t = AdversarialSearch([
#     ['', 'O', ''],
#     ['', 'X', 'O'],
#     ['', 'O', 'X']], "X")
# t = AdversarialSearch([
#     ['O', 'O', 'X'],
#     ['X', '', 'O'],
#     ['', '', 'X']], "X")
# print(t.bestMove)