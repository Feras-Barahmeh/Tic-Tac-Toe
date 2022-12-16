
from copy import deepcopy
from AbstractAction import *
from Shingle import *
from random import randint
from GeneralTree import *

class AdversarialSearch(Shingle, AbstractActions):
    def __init__(self, grid : list, mark):
        super().__init__()
        self.computerMark = mark
        self.personMark = 'X' if mark == 'O' else 'O'
        self.grid = grid
        self.player = Player.computer
        self.result = []



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
        self.player = Player.human if self.player.value == Player.computer.value else Player.computer
        return self.player

    @property
    def __setMark(self):
        return self.computerMark if self.player.value == Player.computer.value else self.personMark

    @staticmethod
    def __chooseMove(statistics):
        maxVal = statistics[0]["win"]
        coor = statistics[0]["coordinate"]
        for statistic in statistics:
            if statistic["win"] > maxVal:
                maxVal = statistic["win"]
                coor = statistic["coordinate"]
        return coor


    def __getStatistics(self, board, result):
        if board.status == StatusGame.win:
            result["win"] += 1
        elif board.status == StatusGame.lose:
            result["lose"] += 1
        else:
            result["tie"] += 1

        if board.childes:
            for child in board.childes:
                self.__getStatistics(child, result)
        return result

    def __appendChild(self, root : TreeNode):
        coordinates = self.getEmptyPositions(root.board)
        for coordinate in coordinates:
            newNode = deepcopy(root)
            newNode.board[coordinate[0]][coordinate[1]] = self.__setMark
            newNode.status = self.__utility(newNode.board)
            root.addChild(newNode)
        self.player = self.__switchPlayer
        return root

    def __builtSubTree(self, grid : TreeNode):
        if not self.ifShingleFill(grid.board) :
            grid = self.__appendChild(grid)
            for child in grid.childes:
                self.__builtSubTree(child)
        return grid

    @property
    def bestMove(self):
        result = {}
        statistics = []
        if self.ifShingleFill(self.grid): return None
        if len(self.shingle) * SHINGLE_DIVISION == len(self.getEmptyPositions(self.shingle)):
            return randint(0, 2), randint(0, 2)

        for coordinate in self.getEmptyPositions(self.grid):
            newChild = deepcopy(self.grid)

            newChild[coordinate[0]][coordinate[1]] = self.computerMark
            self.player = Player.human
            parent = TreeNode(newChild)
            result["coordinate"] = coordinate
            result["win"] = 0
            result["lose"] = 0
            result["tie"] = 0

            parent = self.__builtSubTree(parent)
            # parent.displayTree()

            values = self.__getStatistics(parent, result)
            statistics.append(values)

        return self.__chooseMove(statistics)

# t = AdversarialSearch([
#     ['O', 'O', 'X'],
#     ['X', '', 'O'],
#     ['', '', 'X']], "X")
# t.bestMove()