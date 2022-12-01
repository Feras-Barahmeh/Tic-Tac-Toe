from Shingle import *
from Symbol import *
from Configuration import *
from random import randint


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


    def update(self):
        if self.player and not self.shingle.ifShingleFill() and not self.ifWinner(self.shingle.shingle, 'X'):
            row, col = self.testAI()
            self.switchPlayer(row, col)


    def startGame(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.__events()
            self.update()
            self.__showScreen()


    @staticmethod
    def ifWinner(shingle, symbol) -> bool:
        """
        :param shingle: The patch we want to check
        :param symbol: The player's symbol
        :return: False if player He Hasn't Won Yet and True if won
        """
        for position, row in enumerate(shingle):
            if row.count(symbol) == SHINGLE_DIVISION:
                return True
        if shingle[0][0] == symbol and shingle[1][1] == symbol and shingle[2][2] == symbol:
            return True
        if shingle[2][0] == symbol and shingle[1][1] == symbol and shingle[2][0] == symbol:
            return True

        return False


