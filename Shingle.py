from Configuration import *
import pygame

class Shingle:
    def __init__(self):
        self.shingle = [['' for _ in range(SHINGLE_DIVISION)] for _ in range(SHINGLE_DIVISION)]

    @staticmethod
    def divisionShingle(screen):
        # pygame.draw.line(surface, colour, (startX, startY), (endX, endY), width)
        for row in range(0, TILE_AREA * 2, TILE_AREA):
            pygame.draw.line(screen,
                             WHITE,
                             (MARGIN_X + row + TILE_AREA, MARGIN_Y),
                             (MARGIN_X + row + TILE_AREA, MARGIN_Y + SHINGLE_DIVISION * TILE_AREA),
                             5)


        for col in range(0, TILE_AREA * 2, TILE_AREA):
            pygame.draw.line(screen,
                             WHITE,
                             (MARGIN_X, MARGIN_Y + col + TILE_AREA),
                             (MARGIN_X + SHINGLE_DIVISION * TILE_AREA, MARGIN_Y + col + TILE_AREA),
                             5)

    def __clickPosition(self, mouseX, mouseY):
        for row in range(len(self.shingle)):
            for col in range(len(self.shingle[row])):
                x, y = shingleToPixel(col, row)
                if x <= mouseX <= x * TILE_AREA and y <= mouseY <= y + TILE_AREA and self.shingle[row][col] == '':
                    return row, col
        return None, None


    def ifShingleFill(self):
        for i in self.shingle:
            if filter(lambda x: x == '', i):
                return False
        return True

