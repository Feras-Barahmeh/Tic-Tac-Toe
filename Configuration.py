import pygame
from enum import Enum
from abc import ABC
from Timer import *

# Color
WHITE = (255, 255, 255)
BLACK = (45, 45, 45)
LIGHTGREY = (100, 100, 100)

# Screen Characteristics
WIDTH_SCREEN = 500
HEIGHT_SCREEN = 600
FPS = 60
TITLE = "Tic Tac Toe"
BACKGROUND_COLOUR = BLACK

# Tile Edit
TILE_AREA = 120
SHINGLE_DIVISION = 3
WIDTH_LINE = 5


# Measurements
PADDING_X = int((WIDTH_SCREEN - (SHINGLE_DIVISION * TILE_AREA)) /2) # (SHINGLE_DIVISION * TILE_AREA) : Width Shingle
PADDING_Y = int((HEIGHT_SCREEN - (SHINGLE_DIVISION * TILE_AREA)) /2)


def convertTilePositionToPixel(index_X, index_Y) -> tuple:
    """
    :param index_X: position in x coordinate in list
    :param index_Y: position in y coordinate in list
    :return: position tile in pixel
    """
    return PADDING_X + TILE_AREA * index_X, PADDING_Y + TILE_AREA * index_Y


# Players
class Player(Enum):
    computer = 1; human = 0

SYMBOLS = ['X', 'O']

NAMES = [
    "Hind",
    "Bunder",
    "Saber",
    "Tareq",
    "Nofe",
]

# Game Configuration
class StatusGame(Enum):
    lose = -1; tie = 0; win = 1

