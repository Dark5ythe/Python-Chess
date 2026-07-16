from square import Square
from const import *
from piece import *
class board:

    def __init__(self):
        self.square = [[0,0,0,0,0,0,0,0] for col in range (Cols)]

        self._create()
        self._add_pieces('White')
        self._add_pieces('Black')

    def _create(self):

        for row in range(Rows):
            for col in range(Cols):
                self.square[row][col] = Square(row,col)

    def _add_pieces(self,color):
        if color == 'White':
            row_pawn , row_other = (6,7)
        else:
            row_pawn , row_other = (1,0)    

        #  all pawns
        for col in range(Cols):
            self.square[row_pawn][col] = Square(row_pawn , col , pawn(color) )

        #  knights
        self.square[row_other][1] = Square(row_other , 1 , Knight(color))
        self.square[row_other][6] = Square(row_other , 6 , Knight(color))

        #  bishops 
        self.square[row_other][2] = Square(row_other , 2 , Bishop(color))
        self.square[row_other][5] = Square(row_other , 3 , Bishop(color))

        # rook 
        self.square[row_other][0] = Square(row_other , 0 , Rook(color))
        self.square[row_other][7] = Square(row_other , 7 , Rook(color))

        # queen
        self.square[row_other][3] = Square(row_other , 3 , Queen(color))

        #  king 
        self.square[row_other][4] = Square(row_other , 4 , King(color))
        
