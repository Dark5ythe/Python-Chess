import pygame
import sys 

from const import *
from game import Game

class main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (Width , Height))  # this is the dimention of the screen 
        pygame.display.set_caption('Chess') # this is the name displayed 
        self.game = Game()



    def mainloop(self):   # this is the most imp part of the programe which runs the file and updates it 
        while True:
            self.game.show_bg(self.screen)

            for event in pygame.event.get():  # evrry mouse click is stored as an event 
                if event.type == pygame.QUIT: # when X is pressed the game exits 
                    pygame.quit()
                    sys.quit()


    
        
            pygame.display.update()
main = main()
main.mainloop()
print("Pygame version:", pygame.__version__)

