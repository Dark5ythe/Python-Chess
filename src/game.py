import pygame

from const import *
from board import board

class Game:

    def __init__(self):
        self.board = board()

    #  show method
    
    def show_bg(self,surface):  #this is going to show the background 
        for row in range(Rows):
            for col in range(Cols):
                if (row + col) % 2 == 0:
                    color = (234,235,200)       #light green
                else:
                    color = (119,154,88)        #dark green 
                

                rect = (col * Sqsize , row * Sqsize , Sqsize , Sqsize)

                pygame.draw.rect(surface,color,rect)

    def show_pieces(self,surface):
        for row in range(Rows):
            for col in range(Cols):
                # piece ?
                square = self.board.square[row][col]
                if square.has_piece():
                    piece = square.piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * Sqsize + Sqsize // 2, row * Sqsize + Sqsize // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img , piece.texture_rect)


        
