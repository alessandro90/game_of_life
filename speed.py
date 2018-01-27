import pygame

class Speed:
    '''Class to modify execution speed.'''
    def __init__(self, screen, game_settings):
        self.actual_drop = game_settings.initial_drop
        self.initial_drop = game_settings.initial_drop
        self.step = game_settings.speed_step
        self.max_drop = game_settings.speed_max_drop
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
        if self.actual_drop >= self.step:
            self.actual_drop -= self.step

    def decrease(self):
        '''Decrease current speed.'''
        if self.actual_drop < self.max_drop:
            self.actual_drop += self.step

    def update(self):
        '''Update current speed.'''
        if self.accelerate:
            self.increase()
        if self.decelerate:
            self.decrease()

    def draw(self):
        '''Draw a speed bar on screen.'''
        self.bar_size = int(((self.max_drop - self.actual_drop) / self.max_drop) * (self.max_height - 1) + 1)
        self.rect = pygame.Rect(self.screen_rect.right - 25, 
                                0, 
                                self.width, 
                                self.bar_size)
        self.rect.centery = self.screen_rect.centery
        pygame.draw.rect(self.screen, self.color, self.rect)
