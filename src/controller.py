import pygame
from src.player import Player
from src.enemy import Enemy
from src.start_menu import StartMenu
from src.game_over import GameOver
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
        self.screen = pygame.display.set_mode((1080, 607))
        self.start_menu = StartMenu(self.screen)
        self.game_over = None
    
    def mainloop(self):
        """
        Controlls game flow
        Args: 
            None
        Returns: 
            None
        """
        background = pygame.image.load(self.image_file)
        
        player = Player(self.screen, 390, 400,"./assets/player.webp")
        enemy = Enemy(self.screen, 390, 0, "./assets/enemy.png")
        
        running = True 
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K.SPACE:
                        self.start_game(player, enemy)
                    elif event.key == pygame.K.RIGHT:
                        player.move_right()
                    elif event.key == pygame.K_q:
                        running = False
            self.screen.blit(background, (0, 0))
                       
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                player.move_left()
            if pressed[pygame.K_RIGHT]:
                player.move_right()
            if pressed[pygame.K_SPACE]:
                player.shoot(enemy)
            
            enemy.move(player)
            
            player.draw()
            enemy.draw()
            
            pygame.display.flip()
            
        game_over_screen = GameOver(self.screen, "GAME OVER")
        game_over_screen.display()
                    
        pygame.quit()
                                        
        
            