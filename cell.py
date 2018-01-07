import pygame

class Cell:
    '''A cell class.'''
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.width = game_settings.cell_width
        self.height = game_settings.cell_height
        self.color = game_settings.cell_color

        # Create cell rect object (save one pixel per dimension).
        self.rect = pygame.Rect(0, 0, self.width - 1, self.height - 1)

    def draw(self, x, y):
        '''Draw the cell on screen (alive cell).'''
        self.x = x * self.width
        self.y = y * self.height
        self.rect.left = self.x
        self.rect.top = self.y
        pygame.draw.rect(self.screen, self.color, self.rect)