from square import Square
from const import *

class board:

    def __init__(self):
        self.square = [[0,0,0,0,0,0,0,0] for col in range (Cols)]

        self._create()

    def _create(self):

        for row in range(Rows):
            for col in range(Cols):
                self.square[row][col] = Square(row,col)

    def _add_pieces(self,color):
        pass    