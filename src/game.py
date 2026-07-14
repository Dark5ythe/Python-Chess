import pygame

from const import *

class Game:

    def __init__(self):
        pass

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

