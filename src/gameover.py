import pygame
def __init__(self, screen):
        self.screen = screen
def game_over(screen):
    background = pygame.image.load("./assets/space.webp")
    font = pygame.font.Font(None, 40)
    game_over_info = font.render("Game Over", True, (255, 255, 255))
    game_over_info_rect = game_over_info.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    screen.blit(background, (0, 0))
    screen.blit(game_over_info, game_over_info_rect)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()