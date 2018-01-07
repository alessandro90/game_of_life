class Settings:
    '''All relevant settings for the Game of Life.'''
    def __init__(self):
        # Screen settings.
        self.screen_color = 30, 30, 30
        self.screen_width = 1280
        self.screen_height = 720

        # Cells settings.
        self.cell_width = 10
        self.cell_height = 10
        self.cell_color = 255, 255, 51

        # Boundary conditions.
        # This should not be changed.
        self.periodic_boundaries = True
        # This can be changed.
        self.periodic_boundaries_interactive = True

        # Speed bar settings.
        self.speed_bar_width = 20
        self.speed_bar_height = 200
        self.speed_bar_max_height = 400
        self.speed_bar_color = 102, 0, 204
        self.initial_speed = 0.25

        # Main menu options
        self.options_color = (255, 255, 0)
        self.options_text_color = (0, 0, 0)
