import pygame
from player import Player
from computerplayer import ComputerPlayer
from game import Game

class Controller:
    def __init__(self):
        """ initializes controller
        """
        pygame.init()
    def mainloop(self):
        """
        """
        while True: 
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            #2. detect collisions and update models 
            
            #3. Redraw next frame
            
            #4. Display next frame 
            pygame.display.flip()
            