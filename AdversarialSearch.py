from copy import deepcopy
from collections import deque
from Game import *
import multiprocessing

class AdversarialSearch(Shingle, AbstractActions):
    

    @staticmethod
    def getEmptyPositions(shingle):
        return [(int(x), int(y)) for x, row in enumerate(shingle) for y, symbol in enumerate(row) if symbol == '']