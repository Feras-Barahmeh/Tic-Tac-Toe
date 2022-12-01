from Configuration import *


class Shingle:
    def __init__(self):
        self.shingle = [['' for _ in range(SHINGLE_DIVISION)] for _ in range(SHINGLE_DIVISION)]

    @staticmethod
    def divisionShingle(screen):
        # pygame.draw.line(surface, colour, (startX, startY), (endX, endY), width)
        for row in range(0, TILE_AREA * 2, TILE_AREA):
            pygame.draw.line(screen,
                             WHITE,
                             (PADDING_X + row + TILE_AREA, PADDING_Y),
                             (PADDING_X + row + TILE_AREA, PADDING_Y + SHINGLE_DIVISION * TILE_AREA),
                             WIDTH_LINE)

        for col in range(0, TILE_AREA * 2, TILE_AREA):
            pygame.draw.line(screen,
                             WHITE,
                             (PADDING_X, PADDING_Y + col + TILE_AREA),
                             (PADDING_X + SHINGLE_DIVISION * TILE_AREA, PADDING_Y + col + TILE_AREA),
                             WIDTH_LINE)

    def ifValidClick(self, mouseX, mouseY):
        """
        :param mouseX: position of clicked mouse in x coordinate
        :param mouseY: position of clicked mouse in y coordinate
        :return: None, None: if the click out of the tiles and position tile if valid click
        """

        for row in range(len(self.shingle)):
            for col in range(len(self.shingle[row])):
                x, y = convertTilePositionToPixel(col, row)
                if x <= mouseX <= x + TILE_AREA and y <= mouseY <= y + TILE_AREA and self.shingle[row][col] == '':
                    return row, col

        return None, None


    def ifShingleFill(self):
        for i in self.shingle:
            if filter(lambda e: e == '', i):
                return False
        return True

