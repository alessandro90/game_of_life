import pygame

class Options:
    '''Different start-game options.'''
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 25)
        self.color = game_settings.options_color
        self.text_color = game_settings.options_text_color
        self.width, self.height = 180, 30
        self.first_random = True

        # Random option.
        self.random_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.random_rect.left = self.screen_rect.left
        self.random_rect.top = self.screen_rect.top + 100
        
        self.msg_random = self.font.render("Random", True, self.text_color,
                                          self.color)
        self.msg_random_rect = self.msg_random.get_rect()
        self.msg_random_rect.center = self.random_rect.center

        # Glider option.
        self.glider_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.glider_rect.left = self.screen_rect.left
        self.glider_rect.top = self.random_rect.bottom + 20
        
        self.msg_glider = self.font.render("Glider", True, self.text_color,
                                          self.color)
        self.msg_glider_rect = self.msg_glider.get_rect()
        self.msg_glider_rect.center = self.glider_rect.center

        # Small exploder option.
        self.small_exploder_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.small_exploder_rect.left = self.screen_rect.left
        self.small_exploder_rect.top = self.glider_rect.bottom + 20
        
        self.msg_small_exploder = self.font.render("Small Exploder", True, self.text_color,
                                          self.color)
        self.msg_small_exploder_rect = self.msg_small_exploder.get_rect()
        self.msg_small_exploder_rect.center = self.small_exploder_rect.center

        # Ten cells row option.
        self.ten_cells_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.ten_cells_rect.left = self.screen_rect.left
        self.ten_cells_rect.top = self.small_exploder_rect.bottom + 20
        
        self.msg_ten_cells = self.font.render("Ten Cells Row", True, self.text_color,
                                          self.color)
        self.msg_ten_cells_rect = self.msg_ten_cells.get_rect()
        self.msg_ten_cells_rect.center = self.ten_cells_rect.center

        # Crab.
        self.crab_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.crab_rect.left = self.screen_rect.left
        self.crab_rect.top = self.ten_cells_rect.bottom + 20
        
        self.msg_crab = self.font.render("Crab", True, self.text_color,
                                          self.color)
        self.msg_crab_rect = self.msg_crab.get_rect()
        self.msg_crab_rect.center = self.crab_rect.center

        # hivenudger
        self.hivenudger_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.hivenudger_rect.left = self.screen_rect.left
        self.hivenudger_rect.top = self.crab_rect.bottom + 20
        
        self.msg_hivenudger = self.font.render("Hivenudger", True, self.text_color,
                                          self.color)
        self.msg_hivenudger_rect = self.msg_hivenudger.get_rect()
        self.msg_hivenudger_rect.center = self.hivenudger_rect.center

        # kok's galaxy
        self.koks_galaxy_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.koks_galaxy_rect.left = self.screen_rect.left
        self.koks_galaxy_rect.top = self.hivenudger_rect.bottom + 20
        
        self.msg_koks_galaxy = self.font.render("Kok's Galaxy", True, self.text_color,
                                          self.color)
        self.msg_koks_galaxy_rect = self.msg_koks_galaxy.get_rect()
        self.msg_koks_galaxy_rect.center = self.koks_galaxy_rect.center

        # Gosper Glider Gun.
        self.glider_gun_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.glider_gun_rect.left = self.screen_rect.left
        self.glider_gun_rect.top = self.koks_galaxy_rect.bottom + 20
        
        self.msg_glider_gun = self.font.render("Gosper Glider Gun", True, self.text_color,
                                          self.color)
        self.msg_glider_gun_rect = self.msg_glider_gun.get_rect()
        self.msg_glider_gun_rect.center = self.glider_gun_rect.center

        # Exploder
        self.exploder_rect = pygame.Rect(0, 0, self.width, 
                                          self.height)
        self.exploder_rect.left = self.screen_rect.left
        self.exploder_rect.top = self.glider_gun_rect.bottom + 20
        
        self.msg_exploder = self.font.render("Exploder", True, self.text_color,
                                          self.color)
        self.msg_exploder_rect = self.msg_exploder.get_rect()
        self.msg_exploder_rect.center = self.exploder_rect.center

    def check_any(self, xmouse, ymouse):
        '''Check whether an option has been chosen.'''
        if self.random_rect.collidepoint(xmouse, ymouse):
            return True
        if self.glider_rect.collidepoint(xmouse, ymouse):
            return True
        if self.small_exploder_rect.collidepoint(xmouse, ymouse):
            return True
        if self.ten_cells_rect.collidepoint(xmouse, ymouse):
            return True
        if self.crab_rect.collidepoint(xmouse, ymouse):
            return True
        if self.hivenudger_rect.collidepoint(xmouse, ymouse):
            return True
        if self.koks_galaxy_rect.collidepoint(xmouse, ymouse):
            return True
        if self.glider_gun_rect.collidepoint(xmouse, ymouse):
            return True
        if self.exploder_rect.collidepoint(xmouse, ymouse):
            return True
        return False


    def draw(self):
        '''Draw options to start the game on screen.'''
        self.screen.fill(self.color, self.glider_rect)
        self.screen.blit(self.msg_glider, self.msg_glider_rect)

        self.screen.fill(self.color, self.small_exploder_rect)
        self.screen.blit(self.msg_small_exploder, self.msg_small_exploder_rect)

        self.screen.fill(self.color, self.ten_cells_rect)
        self.screen.blit(self.msg_ten_cells, self.msg_ten_cells_rect)

        self.screen.fill(self.color, self.random_rect)
        self.screen.blit(self.msg_random, self.msg_random_rect)

        self.screen.fill(self.color, self.crab_rect)
        self.screen.blit(self.msg_crab, self.msg_crab_rect)

        self.screen.fill(self.color, self.hivenudger_rect)
        self.screen.blit(self.msg_hivenudger, self.msg_hivenudger_rect)

        self.screen.fill(self.color, self.koks_galaxy_rect)
        self.screen.blit(self.msg_koks_galaxy, self.msg_koks_galaxy_rect)

        self.screen.fill(self.color, self.glider_gun_rect)
        self.screen.blit(self.msg_glider_gun, self.msg_glider_gun_rect)

        self.screen.fill(self.color, self.exploder_rect)
        self.screen.blit(self.msg_exploder, self.msg_exploder_rect)
