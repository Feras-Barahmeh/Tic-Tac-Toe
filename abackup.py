from copy import deepcopy
from collections import deque
import multiprocessing
from Game import *
from AbstractAction import *
from Shingle import *

class AdversarialSearch(Shingle, AbstractActions):
    def __init__(self, grid : Shingle, level, mark):
        super().__init__(grid.shingle, grid.status, level)
        self.grid = grid
        self.level = level
        self.markComputer = mark
        self.playerMark = 'O' if self.markComputer == 'X' else 'X'
    @staticmethod
    def getEmptyPositions(shingle):
        return [(int(x), int(y)) for x, row in enumerate(shingle) for y, symbol in enumerate(row) if symbol == '']

    def __setStatus(self, board, mark):
        if self.ifWinner(board, mark) and mark == self.markComputer:
            return StatusGame.win

        elif self.ifTie(board, mark):
            return StatusGame.tie
        else:
            return StatusGame.lose


    def virtualPlayer(self, board, mark, level):
        childes = []; coordinates = self.getEmptyPositions(board.shingle)

        for coordinate in coordinates:
            newBoard = deepcopy(board)
            newBoard.shingle[coordinate[0]][coordinate[1]] = mark
            newBoard.status = self.__setStatus(newBoard.shingle, mark)
            newBoard.coordinate = coordinate
            newBoard.level = level

            childes.append(newBoard)
        return childes


    def __getStatus(self, grid):
        playerTurn = Player.human; ifComputerFinsh = ifPersonFinsh = False
        childComputer = childHuman = []
        g = deepcopy(grid)
        childComputer.append(g)
        level = 0
        while not ifPersonFinsh or not ifComputerFinsh:
            if playerTurn.value == Player.human.value and not ifPersonFinsh:
                for board in childComputer:
                    newGrid = deepcopy(board)
                    childHuman = childHuman + self.virtualPlayer(newGrid, self.playerMark, level)
                    level += 1
                ifPersonFinsh = True
                # childComputer = []
            elif not ifComputerFinsh:
                for board in childHuman:
                    newGrid = deepcopy(board)
                    childComputer = childComputer + self.virtualPlayer(newGrid, self.markComputer, level)
                    level += 1
                ifComputerFinsh = True
                # childHuman = []


        return childComputer




    def getBestMove(self):
        # possible Moves To Computer
        coordinates = self.getEmptyPositions(self.grid.shingle)
        numberCoordinates = len(coordinates)
        if numberCoordinates == 1: return coordinates[0]
        if numberCoordinates == len(self.grid.shingle): return 1, 1

        for coordinate in coordinates:
            playMove = deepcopy(self.grid)
            playMove.shingle[coordinate[0]][coordinate[1]] = self.markComputer

            # Get All Status If Computer Play This Move
            childes = self.__getStatus(playMove)
            print(coordinate)
            for i in childes:
                for j in i.shingle:
                    print(j)
                print('-' * 15)
            break






        return True



t = AdversarialSearch(Shingle([
                        ['O', 'X', 'X'],
                        ['', '', ''],
                        ['O', '', '']], StatusGame.tie, 5), 5, "X")
# t = AdversarialSearch(Shingle([
#                         ['O', 'X', 'X'],
#                         ['', 'X', ''],
#                         ['O', 'O', '']], StatusGame.tie, 5), 5, "X")
print(t.getBestMove())