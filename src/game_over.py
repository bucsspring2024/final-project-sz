import pygame
class GameOver:
    def __init__(self, screen, message):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.msg_surface = self.font.render(message, True, (255, 255, 255))
        self.msg_rect = self.msg_surface.get_rect(center=(screen.get_wodth() // 2, screen.get_height() // 2))
        
    def display(self):
        """displays game over message
        
        Args: 
            None
            
        Returns:
            None
        """
        self.screen.fill(0, 0, 0)
        self.screen.blit(self.msg_surface, self.msg_rect)
        pygame.display.flip()