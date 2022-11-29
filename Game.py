from Shingle import *
import pygame
from Configuration import *


class Game:
    def __init__(self):
        self.shingle = None
        self.playing = None
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def newGame(self):
        """ refresh screen after any click """
        self.shingle = Shingle()

    def __showScreen(self):
        self.screen.fill(BACKGROUND_COLOUR)
        self.shingle.divisionShingle(self.screen)
        pygame.display.flip()

    @staticmethod
    def __events():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    def update(self):
        pass

    def startGame(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.__events()
            self.update()
            self.__showScreen()

