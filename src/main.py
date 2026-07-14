import pygame
import sys 

from const import *

class main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (Width , Height))
        pygame.display.set_caption('Chess')
    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()


    
        
            pygame.display.update()
main = main()
main.mainloop()
print("Pygame version:", pygame.__version__)

