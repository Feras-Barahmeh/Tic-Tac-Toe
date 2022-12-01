from Configuration import *
class Lines:

    def __init__(self, window):
        self.window = window



    def horizontalLine(self, row):
        positionY = row * TILE_AREA + (PADDING_Y + TILE_AREA / 2)
        pygame.draw.line(self.window, "Green",
                         (PADDING_X + TILE_AREA / 2, positionY),
                         (PADDING_X + 5 * TILE_AREA / 2, positionY),
                         WIDTH_LINE - 1)


    def verticalLine(self, col):
        positionX = col * TILE_AREA + (PADDING_X + TILE_AREA / 2)
        pygame.draw.line(self.window, "Green",
                         (positionX, PADDING_X + TILE_AREA / 2),
                         (positionX, PADDING_Y + 5 * TILE_AREA / 2),
                         WIDTH_LINE - 1)
    def diagonalRight(self):
        pygame.draw.line(self.window, "Green",
                         (PADDING_X + TILE_AREA / 2, PADDING_Y + TILE_AREA / 2),
                         (PADDING_X + 5 * TILE_AREA / 2, PADDING_Y + 5 * TILE_AREA / 2),
                         WIDTH_LINE - 1)

    def diagonalLeft(self):
        pygame.draw.line(self.window, "Green",
                         (PADDING_X + TILE_AREA / 2, PADDING_Y + 5 * TILE_AREA / 2),
                         (PADDING_X + 5 * TILE_AREA / 2, PADDING_Y + TILE_AREA / 2),
                         WIDTH_LINE - 1)
