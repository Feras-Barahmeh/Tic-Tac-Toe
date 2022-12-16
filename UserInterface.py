import pygame

from Configuration import *
class userInterface:
    def __init__(self, xCoordinate, yCoordinate, content):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.content = content


    def draw(self, screen, fontSize, color=WHITE):
        font = pygame.font.SysFont("italic", fontSize)
        content = font.render(self.content, True, color)
        screen.blit(content, (self.xCoordinate, self.yCoordinate))
