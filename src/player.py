import pygame
from src.bullet import Bullet
class Player:
    
    def __init__(self, screen, x, y, img_file):
        """initialzes player obj

        Args:
            screen (pygame.Surface): surface that player is drawn
            x (int): initial x coordinate of player
            y (int): initial y coorrdinate of player
            img_file (str): file path of image for player sprite
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.img_file = img_file
        self.img = pygame.image.load(img_file)
        self.bullets = 4
    def move_right(self):
        """
        moves position right by 2
        args: None
        return: None
        """
        self.x+=2
    def move_left(self):
        """
        moves position left by 2
        args: None
        return: None
        """
    def shoot(self, enemy):
        self.bullets -= 1
        if(self.bullets <= 0):
            exit()
        bullet = Bullet("./assets/bullet.png", self.screen, True, self.x + 124, self.y+50, enemy)
        bullet.move()
        """
        creates bullet object, enables it to move
        Args: 
            enemy: target enemy obj
        Returns: 
            none
        """
    
    def draw(self):
        """draws player sprite to screen
        Args: 
            None
        Returns:
            None
        """
        self.screen.blit(self.img, (self.x, self.y))