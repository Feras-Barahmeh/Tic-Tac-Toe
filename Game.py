# from AbstractAction import *
# from Shingle import *
import random

from Symbol import *
from Lines import *
from AdversarialSearch import *
from UserInterface import *

class Game(AbstractActions):
    def __init__(self):
        self.shingle = Shingle()
        self.playing = None
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.player = None
        self.computerScore = self.personScore = 0
        self.determinantSymbol = randint(0, 1)
        self.personSymbol = SYMBOLS[self.determinantSymbol - 1]
        self.computerSymbol = SYMBOLS[self.determinantSymbol]
        self.AIName = random.choice(NAMES)

    def newGame(self):
        """ start game  """
        self.shingle = Shingle()
        # The probability that the computer will start playing 75 %
        self.player = randint(Player.human.value, Player.computer.value) or randint(Player.human.value, Player.computer.value)
        self.player = Player.human if self.player == Player.human.value else Player.computer

    def switchPlayer(self, row, col):
        if self.player.value == Player.human.value:
            self.shingle.shingle[row][col] = self.personSymbol
            UserInterface(140, 100, f"{self.AIName} Turn ").draw(self.screen, 60)

        elif self.player.value == Player.computer.value:
            self.shingle.shingle[row][col] = self.computerSymbol
            UserInterface(140, 100, f" YOu Turn ").draw(self.screen, 60)

        self.player = Player.human if self.player.value == Player.computer.value else Player.computer

    def setSymbol(self):
        for i, row in enumerate(self.shingle.shingle):
            for j, symbol in enumerate(row):
                x, y = convertTilePositionToPixel(j, i)
                Symbol(x, y, symbol).createSymbol(self.screen)

    def chickWinner(self, shingle):
        """
        :param shingle: The Shingle We will check
        :return:
        """
        if self.__winLine(shingle, self.computerSymbol):
            self.computerScore += 1
            UserInterface(160, 500, "It's a Lose ): ").draw(self.screen, 40)
            self.playing = False

        elif self.__winLine(shingle, self.personSymbol):
            self.personScore += 1
            UserInterface(160, 500, "It's a Win (: ").draw(self.screen, 40)
            self.playing = False

        if self.shingle.ifShingleFill():
            self.playing = False



    def __showScreen(self):
        self.screen.fill(BACKGROUND_COLOUR)
        self.shingle.divisionShingle(self.screen)
        self.setSymbol()
        self.chickWinner(self.shingle.shingle)
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
                if self.player.value == Player.human.value and not self.shingle.ifShingleFill() and not self.ifWinner(self.shingle.shingle, self.computerSymbol):
                    mouseCoordinateX, mouseCoordinateY = pygame.mouse.get_pos()
                    row, col = self.shingle.ifValidClick(mouseCoordinateX, mouseCoordinateY)
                    if row is not None:
                        # Add symbol
                        self.switchPlayer(row, col)


    def __update(self):
        if self.player.value == Player.computer.value and not self.shingle.ifShingleFill() and not self.ifWinner(self.shingle.shingle, self.personSymbol):
            # row, col = self.testAI()
            row, col = AdversarialSearch(self.shingle.shingle, self.computerSymbol).bestMove
            self.switchPlayer(row, col)
            UserInterface(140, 100, f"{self.AIName} Turn ").draw(self.screen, 60)

    def play(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS) # Frames Per Second (means that for every second at most FPS frames should pass)
            self.__events()
            self.__update()
            self.__showScreen()
        else:
            self.end_screen()

    def __winLine(self, shingle, symbol):
        """
        :param shingle: The patch we want to check
        :param symbol: The player's symbol
        :return: Draw Win Line
        """
        for row in range(SHINGLE_DIVISION):
            if shingle[row][0] == symbol and shingle[row][1] == symbol and shingle[row][2] == symbol:
                Lines(self.screen).horizontalLine(row)
                return None

        for col in range(SHINGLE_DIVISION):
            if shingle[0][col] == symbol and shingle[1][col] == symbol and shingle[2][col] == symbol:
                Lines(self.screen).verticalLine(col)
                return None

        if shingle[0][0] == symbol and shingle[1][1] == symbol and shingle[2][2] == symbol:
            Lines(self.screen).diagonalRight()
            return None

        if shingle[2][0] == symbol and shingle[1][1] == symbol and shingle[0][2] == symbol:
            Lines(self.screen).diagonalLeft()
            return None


    @staticmethod
    def end_screen():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return