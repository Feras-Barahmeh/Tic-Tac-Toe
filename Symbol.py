from Configuration import *

class Symbol:
    def __init__(self, x, y, typeSymbol):
        self.x = x
        self.y = y
        self.typeSymbol = typeSymbol

    def createSymbol(self, shingle):
        font = pygame.font.SysFont("italic", 100)
        symbol = font.render(self.typeSymbol, True, WHITE)
        fontSize = font.size(self.typeSymbol)
        coordinateX = self.x + (TILE_AREA / 2) - fontSize[0] / 2
        coordinateY = self.y + (TILE_AREA / 2) - fontSize[1] / 2

        shingle.blit(symbol, (coordinateX, coordinateY))
