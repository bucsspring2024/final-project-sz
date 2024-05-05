import pygame
def start_menu(screen):
    """shows the start menu if user chooses to do so, or quits if the user chooses to quit

    Args:
        screen (pygame.Surface): surface where menu is drawn

    Returns:
        bool: if game starrts, true, else false
    """
    background = pygame.image.load("./assets/space.webp")
    font = pygame.font.Font(None, 40)
    instructions = font.render("You have three bullets to kill the enemy.", True, (255, 255, 255))
    instructions_rect = instructions.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    s = font.render("Click 'S' to start the game", True, (255, 255, 255))
    s_rect = s.get_rect(center = (screen.get_width() // 2, screen.get_height() // 2 + 50))
    q = font.render("Click 'q' to quit the game", True, (255, 255, 255))
    q_rect = q.get_rect(center = (screen.get_width() // 2, screen.get_height() // 2 + 100)) 
    screen.blit(background, (0, 0))
    screen.blit(instructions, instructions_rect)
    screen.blit(s, s_rect)
    screen.blit(q, q_rect)             
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    return False