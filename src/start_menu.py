import pygame

class StartMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.instr_text = "Press Space to start, or press Q to quit"
        self.instr_surface = self.font.render(self.instr_text, True, (255, 255, 255))
        self.instr_rect = self.instr_surface.get_rect(center=(screen.get_wdith() // 2, screen.get_height() // 2))
        
    def display(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.instr_surface, self.instr_rect)
        pygame.display.flip()