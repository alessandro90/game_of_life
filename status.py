import pygame.font

class Status:
    def __init__(self, screen):
        '''Initialize status attributes.'''
        self.pause = False
        self.message = "Pause"
        self.generation = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set 'pause' label dimensions and properties.
        self.pause_color = (255, 0, 0)
        self.pause_text_color = (0, 0, 0)
        self.pause_font = pygame.font.SysFont(None, 30)

        # Set 'current generation' label dimensions and properties.
        self.gen_color = (0, 0, 0)
        self.gen_text_color = (255, 255, 255)
        self.gen_font = pygame.font.SysFont(None, 22)

        # prep 'pause' label.
        self.pause_prep_msg()

    def pause_prep_msg(self):
        '''Turn message into a rendered image.'''
        self.msg_image = self.pause_font.render(self.message, True, self.pause_text_color,
                                          self.pause_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.topleft = self.screen_rect.topleft

    def prep_gen(self):
        '''Turn current generation into a rendered image.'''
        self.gen_image = self.gen_font.render("Generation" + " " + str(self.generation), 
                                          True, self.gen_text_color,
                                          self.gen_color)
        self.gen_image_rect = self.gen_image.get_rect()
        self.gen_image_rect.centerx = self.screen_rect.centerx
        self.gen_image_rect.top = self.screen_rect.top

    def draw_pause(self):
        """Draw 'pause' message plus current generation."""
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.prep_gen()
        self.screen.blit(self.gen_image, self.gen_image_rect)
