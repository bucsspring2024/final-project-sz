import pygame
from src.player import Player
from src.enemy import Enemy
from src.startmenu import start_menu
from src.gameover import game_over
class Controller:
    def __init__(self, image_file):
        """initializes controller object

        Args:
            image_file (str): file path for game bg
            
        Returns:
            None 
        """
        pygame.init()
        self.image_file = image_file
    
    def mainloop(self):
        """
        Controlls game flow
        Args: 
            None
        Returns: 
            None
        """
        screen = pygame.display.set_mode((1080, 607))
        background = pygame.image.load(self.image_file)
        player = Player(screen, 390,400,"./assets/player.webp")
        enemy = Enemy(screen, 390, 0, "./assets/enemy.png")
        start_game = start_menu(screen)
        if not start_game:
            pygame.quit()
            return
        game_over_condition = False
        while not game_over_condition:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            screen.blit(background, (0, 0))
            player.draw()
            enemy.draw()
            
        
                
            pressed = pygame.key.get_pressed()
            if(pressed[pygame.K_LEFT]):
                player.move_left()
            if(pressed[pygame.K_RIGHT]):
                player.move_right()
            if(pressed[pygame.K_SPACE]):
                player.shoot(enemy)
            enemy.move(player)

            if player.bullets <= 0:
                game_over_condition = True
            pygame.display.flip()
        game_over(screen)