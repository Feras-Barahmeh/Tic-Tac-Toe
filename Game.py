import time

from Shingle import *
from Symbol import *
from random import randint
from Lines import *

class Game:
    def __init__(self):
        self.shingle = Shingle()
        self.playing = None
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.player = None

    def newGame(self):
        """ start game  """
        self.shingle = Shingle()

        # The probability that the computer will start playing 75 %
        self.player = randint(Player.human.value, Player.computer.value) or randint(Player.human.value, Player.computer.value)

    def switchPlayer(self, row, col):
        if not self.player:
            self.shingle.shingle[row][col] = "X"
        else :
            self.shingle.shingle[row][col] = "O"
        self.player = not self.player


    def setSymbol(self):
        for i, row in enumerate(self.shingle.shingle):
            for j, symbol in enumerate(row):
                x, y = convertTilePositionToPixel(j, i)
                Symbol(x, y, symbol).createSymbol(self.screen)


    def __showScreen(self):
        self.screen.fill(BACKGROUND_COLOUR)
        self.shingle.divisionShingle(self.screen)
        self.setSymbol()

        if self.ifWinner(self.shingle.shingle, "X"):
            self.playing = False


        if self.ifWinner(self.shingle.shingle, "O"):
            self.playing = False

        if self.shingle.ifShingleFill():
            self.playing = False

        pygame.display.flip()

    def testAI(self):
        while True:
            x = randint(0, len(self.shingle.shingle) - 1)
            y = randint(0, len(self.shingle.shingle) - 1)
            if self.shingle.shingle[x][y] == '':
                return x, y

    def __events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if e.type == pygame.MOUSEBUTTONDOWN:
                # Human turn
                if not self.player:
                    mouseCoordinateX, mouseCoordinateY = pygame.mouse.get_pos()
                    row, col = self.shingle.ifValidClick(mouseCoordinateX, mouseCoordinateY)
                    if row is not None:
                        # Add symbol
                        self.switchPlayer(row, col)


    def __update(self):
        if self.player and not self.shingle.ifShingleFill() and not self.ifWinner(self.shingle.shingle, 'X'):
            row, col = self.testAI()
            self.switchPlayer(row, col)


    def startGame(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.__events()
            self.__update()
            self.__showScreen()



    def ifWinner(self, shingle, symbol):
        """
        :param shingle: The patch we want to check
        :param symbol: The player's symbol
        :return: False if player He Hasn't Won Yet and True if won
        """
        print(shingle)
        for row in range(SHINGLE_DIVISION):
            if shingle[row][0] == symbol and shingle[row][1] == symbol and shingle[row][2] == symbol:
                Lines(self.screen).horizontalLine(row)
                return True

        for col in range(SHINGLE_DIVISION):
            if shingle[0][col] == symbol and shingle[1][col] == symbol and shingle[2][col] == symbol:
                Lines(self.screen).verticalLine(col)
                return True


        if shingle[0][0] == symbol and shingle[1][1] == symbol and shingle[2][2] == symbol:
            Lines(self.screen).diagonalRight()
            return True

        if shingle[2][0] == symbol and shingle[1][1] == symbol and shingle[0][2] == symbol:
            Lines(self.screen).diagonalLeft()
            return True

        return False


