import pygame
from src.bullet import Bullet
import random
class Enemy:
    def __init__(self, screen, x, y, img_file):
        self.screen = screen
        self.x = x
        self.y = y
        self.img_file = img_file
        self.img = pygame.image.load(img_file)
        self.amountMove = 5
        self.left = False
    def move_right(self):
        """
        moves pos right by 1
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
    def move(self, enemy):
        if(random.randint(1, 75) == 1):
            self.shoot(enemy)
        if(self.amountMove > 0):
            self.amountMove -= 1
            if(self.left):
                self.move_left()
            else: 
                self.move_right()
        else: 
            self.amountMove = random.randrange(5, 10)
            self.left = True if random.randint(0, 1) == 1 else False
    def shoot(self, enemy):
        bullet = Bullet("./assets/bad_bullet.png", self.screen, False, self.x + 150, self.y+200, enemy)
        bullet.move()
        """
        creates a bullet object
        args: None
        return: Bullet
        """
    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))