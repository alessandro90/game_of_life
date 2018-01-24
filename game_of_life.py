import sys
import numpy as np
import pygame
from cell import Cell
import game_functions as gf
from mainmenu import MainMenu
from options import Options
from settings import Settings
from speed import Speed
from status import Status

def run_game():
    '''Run Game of Life.'''
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, 
                                      game_settings.screen_height))
    pygame.display.set_caption("Game of Life")

    # There is only one cell.
    cell = Cell(screen, game_settings)
    # Set main menu.
    main = MainMenu()
    # Set available options.
    options = Options(screen, game_settings)
    # Set speed and speed bar.
    speed = Speed(screen, game_settings)
    # Set pause menu.
    state = Status(screen)

    # Build the matrix for live cells coordinates.
    mat_rows = game_settings.screen_height // game_settings.cell_height + 2
    mat_cols = game_settings.screen_width // game_settings.cell_width + 2
    cells_matrix = np.zeros(shape = (mat_rows, mat_cols)).astype(bool)

    xmouse, ymouse = None, None
    # Set to False the single step option.
    move_to_next_step = [False]

    while 1:
        gf.check_events(state, speed, main, options, xmouse, ymouse, 
                        move_to_next_step)
        if main.menu:
            xmouse, ymouse = pygame.mouse.get_pos()
            gf.main_menu(xmouse, ymouse, game_settings, state, speed, 
                         main, options, cells_matrix)
        elif not state.pause or move_to_next_step[0]:
            gf.game(move_to_next_step, speed, cells_matrix, 
                    game_settings, state)

        gf.update_screen(game_settings, screen, cells_matrix, 
                         state, speed, main, options, cell)

        
    
run_game()
