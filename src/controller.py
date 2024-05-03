import pygame
from src.player import Player
from src.enemy import Enemy
from src.menu import StartMenu, GameOver
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
        self.start_menu = StartMenu()
        self.game_over = None
    
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
        
        player = Player(screen, 390, 400,"./assets/player.webp")
        enemy = Enemy(screen, 390, 0, "./assets/enemy/png")
        
        running = True 
        while running:
            screen.blit(background, (0, 0))
            player.draw()
            enemy.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_Left:
                        player.move_left()
                    elif event.key == pygame.K.RIGHT:
                        player.move_right()
                    elif event.key == pygame.K_SPACE:
                        player.shoot(enemy)
                    elif event.key == pygame.K_q:
                        running = False
                    elif event.ley == pygame.K_s:
                        self.game_over = None
                        
            if self.game_over:
                self.game_over.draw(screen)
            else: 
                self.start_menu.draw(screen)
            
            pygame.display.flip()
            
        pygame.quit()
                                        
        
            