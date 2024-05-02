import pygame
from src.player import Player
from src.enemy import Enemy
class Controller:
    def __init__(self, image_file):
        pygame.init()
        self.image_file = image_file
    
    def mainloop(self):
        screen = pygame.display.set_mode((1080, 607))
        background = pygame.image.load(self.image_file)
        player = Player(screen, 390, 400,"./assets/player.webp")
        enemy = Enemy(screen, 390, 0, "./assets/enemy/png")
        while(True):
            screen.blit(background, (0, 0))
            player.draw()
            enemy.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            pressed = pygame.key.get_pressed()
            if(pressed[pygame.K_LEFT]):
                player.move_left()
            if(pressed[pygame.K_RIGHT]):
                player.move_left()
            if(pressed[pygame.K_SPACE]):
                player.shoot(enemy)
            enemy.move(player)
            pygame.display.flip()
            