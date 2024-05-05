import pygame
from src.bullet import Bullet
class Player:
    def __init__(self, screen, x, y, img_file):
        self.screen = screen
        self.x = x
        self.y = y
        self.img_file = img_file
        self.img = pygame.image.load(img_file)
        self.bullets = 3
    def move_right(self):
        """
        moves position right by 1
        args: None
        return: None
        """
        self.x+=2
    def move_left(self):
        """
        moves position left by 1
        args: None
        return: None
        """
        self.x-=2
    def shoot(self, enemy):
        self.bullets -= 1
        if(self.bullets <= 0):
            exit()
        bullet = Bullet("./assets/bullet.png", self.screen, True, self.x + 124, self.y+50, enemy)
        bullet.move()
        """
        creates a bullet object
        args: None
        return: Bullet
        """

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))   