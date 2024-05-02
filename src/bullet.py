import pygame
import time
class Bullet:
    def __init__(self, img_link, screen, good, x, y, sprite):
        """initializes bullet obj

        Args:
            img_link (str): image file for the bullet
            link (_type_): _description_
            screen: screen object that bullet is drawn
            good (bool): bullet is enemy/player's 
            x (int): x coordinate of bullet
            y (int): y coordinate of bullet
            sprite: bullet's target
        Returns: 
            None
        """
        self.screen = screen
        self.good = good
        self.x = x
        self.y = y
        self.img_link = img_link
        self.img = pygame.image.load(img_link)
        self.sprite = sprite
    def move(self):
        """updates pos of bullet, checks for collisions with the target sprite. program exits when that occurs
        Args:
            None
        Returns:
            None
        """
        while(self.y > 0 if self.good else self.y < 607):
            self.y = self.y - 1 if self.good else self.y + 1
            self.screen.blit(self.img, (self.x, self.y))
            pygame.display.flip()
        if(self.good):
            if(abs((self.sprite.x + 150)-self.x) < 10):
                exit()
            else: 
                if(abs((self.sprite.x + 124)-self.x)< 10):
                    exit()