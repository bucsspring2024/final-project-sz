import pygame
import time
class Bullet:
    def __init__(self, img_link, link, screen, good, x, y, sprite):
        self.screen = screen
        self.good = good
        self.x = x
        self.y = y
        self.img_link = img_link
        self.img = pygame.image.load(img_link)
        self.sprite = sprite
    def move(self):
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