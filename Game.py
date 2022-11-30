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
        pass

    def startGame(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.__events()
            self.update()
            self.__showScreen()