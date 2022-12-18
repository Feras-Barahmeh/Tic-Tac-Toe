from Configuration import *
class AbstractActions(ABC):

    @staticmethod
    def ifWinner(shingle, symbol):
        """
        :param shingle: The patch we want to check
        :param symbol: The player's symbol
        :return: False if player He Hasn't Won Yet and True if won
        """
        for row in range(SHINGLE_DIVISION):
            if shingle[row][0] == symbol and shingle[row][1] == symbol and shingle[row][2] == symbol:
                return True

        for col in range(SHINGLE_DIVISION):
            if shingle[0][col] == symbol and shingle[1][col] == symbol and shingle[2][col] == symbol:
                return True

        if shingle[0][0] == symbol and shingle[1][1] == symbol and shingle[2][2] == symbol:
            return True

        if shingle[2][0] == symbol and shingle[1][1] == symbol and shingle[0][2] == symbol:
            return True

        return False

    def ifTie(self, board, mark):
        anotherMark = 'O' if mark == 'X' else 'X'

        if not self.ifWinner(board, mark[0]) and not self.ifWinner(board, anotherMark):
            return True
        else:
            return False


    def ifShingleFill(self, shingle=None):
        shingle = shingle if shingle else self.grid
        for i in shingle:
            if filter(lambda e: e == '', i):
                return False
        return True

