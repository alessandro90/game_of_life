import pygame

class Speed:
    '''Class to modify execution speed.'''
    def __init__(self, screen, game_settings):
        self.factor = game_settings.initial_speed
        self.initial_speed = game_settings.initial_speed
        self.accelerate = False
        self.decelerate = False
        self.visible = False
        self.color = game_settings.speed_bar_color
        self.width = game_settings.speed_bar_width
        self.height = game_settings.speed_bar_height
        self.max_height = game_settings.speed_bar_max_height
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.bar_size = 0
        
    def increase(self):
        '''Increase current speed.'''
        if self.factor > 1e-6:
            self.factor -= 1e-2
        if self.factor < 1e-6:
            self.factor = 0.

    def decrease(self):
        '''Decrease current speed.'''
        if self.factor < 2 * self.initial_speed:
            self.factor += 1e-2

    def update(self):
        '''Update current speed.'''
        if self.accelerate:
            self.increase()
        if self.decelerate:
            self.decrease()

    def draw(self):
        '''Draw a speed bar on screen.'''
        self.bar_size = (2 * self.initial_speed - self.factor) * (self.max_height - 1) + 1
        self.rect = pygame.Rect(self.screen_rect.right - 25, 
                                0, 
                                self.width, 
                                self.bar_size)
        self.rect.centery = self.screen_rect.centery
        pygame.draw.rect(self.screen, self.color, self.rect)
