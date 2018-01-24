import sys
from time import sleep
import numpy as np
from numba import jit
import pygame
import patterns as pt

def check_events(state, speed, main, options, xmouse, ymouse, 
                 move_to_next_step):
    '''Respond to keypress and mouse.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not main.menu:
                if event.key == pygame.K_p:
                    if not state.pause:
                        state.pause = True
                    elif state.pause:
                        state.pause = False
                if state.pause and event.key == pygame.K_RIGHT:
                    move_to_next_step[0] = True
                if event.key == pygame.K_UP: # Increase speed.
                    speed.accelerate = True
                    speed.visible = True
                if event.key == pygame.K_DOWN: # Decrease speed.
                    speed.decelerate = True
                    speed.visible = True
                if event.key == pygame.K_ESCAPE:
                    main.menu = True
            else:
                if event.key == pygame.K_ESCAPE:
                    main.interactive = False
                if event.key == pygame.K_RETURN and main.interactive:
                    main.start_game = True
        if event.type == pygame.KEYUP and not main.menu:
            if event.key == pygame.K_UP:
                speed.visible = False
                speed.accelerate = False    
            if event.key == pygame.K_DOWN:
                speed.visible = False
                speed.decelerate = False
        if event.type == pygame.MOUSEBUTTONDOWN and main.menu:
            if options.check_any(xmouse, ymouse):
                main.start_game = True
            else:
                if not main.interactive:
                    main.interactive = True
                main.check_cell = True


def update_boundaries(cells_matrix):
    '''
    Set the border of cells_matrix for the
    periodic boundary condition case.
    '''
    cells_matrix[0, :] = cells_matrix[-2, :]
    cells_matrix[-1, :] = cells_matrix[1, :]
    cells_matrix[:, 0] = cells_matrix[:, -2]
    cells_matrix[:, -1] = cells_matrix[:, 1]


@jit
def chek_neighbourhoods(cells_matrix):
    '''
    Check the number of neighbourhood for each cell.
    This function is decorated with numba.jit.
    '''
    dimensions = cells_matrix.shape
    neigh = np.zeros(shape = (dimensions[0] - 2, dimensions[1] - 2))

    for r in range(1, dimensions[0] - 1):
        for c in range(1, dimensions[1] - 1):
            for i in r - 1, r, r + 1:
                for j in c - 1, c, c + 1:
                    if i != r or j != c:
                        if cells_matrix[i, j]:
                            neigh[r - 1, c - 1] += 1
    return neigh


@jit
def update_matrix(cells_matrix, neigh):
    '''
    Update the matrix of cells.
    This function is decorated with numba.jit.
    '''
    # Rules:
    # 1.Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    # 2.Any live cell with two or three live neighbours lives on to the next generation.
    # 3.Any live cell with more than three live neighbours dies, as if by overpopulation.
    # 4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    dimensions = cells_matrix.shape
    for r_index in range(dimensions[0]):
        for c_index in range(dimensions[1]):
            if 0 < c_index < dimensions[1] - 1 and 0 < r_index < dimensions[0] - 1:
                if not cells_matrix[r_index, c_index] and neigh[r_index - 1, c_index - 1] == 3:
                    cells_matrix[r_index, c_index] = True
                elif cells_matrix[r_index, c_index] and neigh[r_index - 1, c_index - 1] < 2:
                    cells_matrix[r_index, c_index] = False
                elif cells_matrix[r_index, c_index] and neigh[r_index - 1, c_index - 1] > 3:
                    cells_matrix[r_index, c_index] = False


def update_cells(cells_matrix, neigh, game_settings):
    '''Update the next generation of cells.'''
    update_matrix(cells_matrix, neigh)
    # If periodic boundaries are active, update the cells matrix boundaries.
    if game_settings.periodic_boundaries:
        update_boundaries(cells_matrix)
  

def reset_game(game_settings, state, speed):
    '''Reset all settings.'''
    state.pause = False
    state.generation = 0
    speed.factor = game_settings.initial_speed


def update_interactive(game_settings, cells_matrix):
    '''Update cells_matrix in interactive mode.'''
    xmouse, ymouse = pygame.mouse.get_pos()
    xc = xmouse // game_settings.cell_width
    yc = ymouse // game_settings.cell_height
    if cells_matrix[yc + 1, xc + 1]:
        cells_matrix[yc + 1, xc + 1] = False
    else:
        cells_matrix[yc + 1, xc + 1] = True


def show_samples(game_settings, options, cells_matrix, xmouse, ymouse):
    '''Check if the mouse cursor is over a configuration.'''
    init_config = None
    if options.random_rect.collidepoint(xmouse, ymouse):
        init_config = "random"    
    if options.glider_rect.collidepoint(xmouse, ymouse):
        init_config = "glider"
    if options.small_exploder_rect.collidepoint(xmouse, ymouse):
        init_config = "small_exploder"
    if options.ten_cells_rect.collidepoint(xmouse, ymouse):
        init_config = "ten_cells"
    if options.crab_rect.collidepoint(xmouse, ymouse):
        init_config = "crab"
    if options.hivenudger_rect.collidepoint(xmouse, ymouse):
        init_config = "hivenudger"
    if options.koks_galaxy_rect.collidepoint(xmouse, ymouse):
        init_config = "koks_galaxy"
    if options.glider_gun_rect.collidepoint(xmouse, ymouse):
        init_config = "glider_gun"
    if options.exploder_rect.collidepoint(xmouse, ymouse):
        init_config = "exploder"
    set_initial_cells(game_settings, options,  init_config, cells_matrix)


def set_initial_cells(game_settings, options, init_config, cells_matrix):
    '''Set the initial configuration of alive cells.'''
    mat_rows = game_settings.screen_height // game_settings.cell_height
    mat_cols = game_settings.screen_width // game_settings.cell_width
   
    if options.first_random:
        cells_matrix[:,:] = np.zeros(shape = (mat_rows + 2, mat_cols + 2)).astype(bool)
    if init_config == "random" and options.first_random:
        options.first_random = False
        game_settings.periodic_boundaries = True
	    # Add two rows and two columns to the matrix (for the boundary consitions).
        temp_mat = np.random.rand(mat_rows + 2, mat_cols + 2) - 0.40
        temp_mat = np.rint(np.absolute(temp_mat)).astype(bool)
        cells_matrix[:,:] = temp_mat
    elif init_config == "glider":
        options.first_random = True
        pt.glider(cells_matrix, game_settings)
    elif init_config == "small_exploder":
        options.first_random = True
        pt.small_exploder(cells_matrix, game_settings)
    elif init_config == "ten_cells":
        options.first_random = True
        pt.ten_cells(cells_matrix, game_settings)
    elif init_config == "crab":
        options.first_random = True
        pt.crab(cells_matrix, game_settings)
    elif init_config == "hivenudger":
        options.first_random = True
        pt.hivenudger(cells_matrix, game_settings)
    elif init_config == "koks_galaxy":
        options.first_random = True
        pt.koks_galaxy(cells_matrix, game_settings)
    elif init_config == "glider_gun":
        options.first_random = True
        pt.glider_gun(cells_matrix, game_settings)
    elif init_config == "exploder":
        options.first_random = True
        pt.exploder(cells_matrix, game_settings)
    elif init_config != "random":
        # This _must_ be the last conditional.
        options.first_random = True
        game_settings.periodic_boundaries = game_settings.periodic_boundaries_interactive

	# Set the proper boundary conditions.
    if not game_settings.periodic_boundaries:
        cells_matrix[0, :] = False
        cells_matrix[-1, :] = False
        cells_matrix[:, 0] = False
        cells_matrix[:, -1] = False
    elif game_settings.periodic_boundaries:
        update_boundaries(cells_matrix)


def main_menu(xmouse, ymouse, game_settings, state, speed, main, options, cells_matrix):
    '''Main menu interface.'''
    reset_game(game_settings, state, speed)
    if not main.interactive:
        show_samples(game_settings, options, cells_matrix, xmouse, ymouse)
    elif main.interactive and main.check_cell:
        update_interactive(game_settings, cells_matrix)
        main.check_cell = False
    if main.start_game:
        main.start_game = False
        main.menu = False
        main.interactive = False


def game(move_to_next_step, speed, cells_matrix, game_settings, state):
    '''Start the game.'''
    move_to_next_step[0] = False
    speed.update()
    neigh = chek_neighbourhoods(cells_matrix)
    update_cells(cells_matrix, neigh, game_settings)
    state.generation += 1
    sleep(speed.factor)


def update_screen(game_settings, screen, cells_matrix, state, 
                  speed, main, options, cell):
    '''Update the screen with the new configuration.'''
    screen.fill(game_settings.screen_color)
    dimensions = cells_matrix.shape

    # Find all the alive cells.
    alive_x, alive_y = np.nonzero(cells_matrix)

    # Draw alive cells.
    for r_index, c_index in zip(alive_x, alive_y):
        if 0 < c_index < dimensions[1] - 1 and 0 < r_index < dimensions[0] - 1:
            cell.draw(c_index - 1, r_index - 1)

    if main.menu and not main.interactive:
        options.draw()

    if state.pause:
        # Draw information visible only when the game is paused.
        state.draw_pause()

    if speed.visible and not state.pause:
        # Draw the speed bar.
        speed.draw()

    pygame.display.flip()
