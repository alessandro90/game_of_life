# This file contains all the available patterns.

def row_col(game_settings):
    return game_settings.screen_height // game_settings.cell_height, game_settings.screen_width // game_settings.cell_width

def glider(cells_matrix, game_settings):
    game_settings.periodic_boundaries = True
    rows, cols = row_col(game_settings)
    cells_matrix[rows // 2 + 1 , cols // 2 - 1:cols // 2 + 2] = True
    cells_matrix[rows // 2, cols // 2 + 1] = True
    cells_matrix[rows // 2 - 1, cols // 2] = True


def small_exploder(cells_matrix, game_settings):
    game_settings.periodic_boundaries = False
    rows, cols = row_col(game_settings)
    cells_matrix[rows // 2 - 2, cols // 2] = True
    cells_matrix[rows // 2 - 1, cols // 2 - 1:cols //2 + 2] = True
    cells_matrix[rows // 2, cols // 2 - 1:cols // 2 + 3:2] = True
    cells_matrix[rows // 2 + 1, cols // 2] = True


def ten_cells(cells_matrix, game_settings):
    game_settings.periodic_boundaries = False
    rows, cols = row_col(game_settings)
    cells_matrix[rows // 2, cols // 2 - 5:cols // 2 + 5] = True


def crab(cells_matrix, game_settings):
    game_settings.periodic_boundaries = True
    rows, cols = row_col(game_settings)
    cells_matrix[rows // 2, cols // 2] = True
    cells_matrix[rows // 2, cols // 2 + 1] = True
    cells_matrix[rows // 2, cols // 2 + 7] = True
    cells_matrix[rows // 2, cols // 2 + 8] = True

    cells_matrix[rows // 2 - 1, cols // 2 + 8] = True
    cells_matrix[rows // 2 - 1, cols // 2 + 11] = True

    cells_matrix[rows // 2 - 3, cols // 2 + 9] = True

    cells_matrix[rows // 2 - 4, cols // 2 + 10] = True
    cells_matrix[rows // 2 - 4, cols // 2 + 11] = True

    cells_matrix[rows // 2 - 5, cols // 2 + 8] = True

    cells_matrix[rows // 2 - 6, cols // 2 + 6] = True
    cells_matrix[rows // 2 - 6, cols // 2 + 7] = True

    cells_matrix[rows // 2 - 7, cols // 2 + 7] = True
    cells_matrix[rows // 2 - 7, cols // 2 + 8] = True

    cells_matrix[rows // 2 + 1, cols // 2] = True
    cells_matrix[rows // 2 + 1, cols // 2 - 1] = True
    cells_matrix[rows // 2 + 1, cols // 2 + 6] = True

    cells_matrix[rows // 2 + 2, cols // 2 + 1] = True
    cells_matrix[rows // 2 + 2, cols // 2 + 6] = True
    cells_matrix[rows // 2 + 2, cols // 2 + 8] = True

    cells_matrix[rows // 2 + 3, cols // 2 + 3] = True
    cells_matrix[rows // 2 + 3, cols // 2 + 4] = True
    cells_matrix[rows // 2 + 3, cols // 2 + 7] = True

    cells_matrix[rows // 2 + 4, cols // 2 + 3] = True
    cells_matrix[rows // 2 + 4, cols // 2 + 4] = True


def hivenudger(cells_matrix, game_settings):
    game_settings.periodic_boundaries = True
    rows, cols = row_col(game_settings)
    cells_matrix[rows // 2, cols // 2] = True
    cells_matrix[rows // 2, cols // 2 + 1] = True
    cells_matrix[rows // 2, cols // 2 + 2] = True
    cells_matrix[rows // 2, cols // 2 + 3] = True
    cells_matrix[rows // 2, cols // 2 + 9] = True
    cells_matrix[rows // 2, cols // 2 + 12] = True

    cells_matrix[rows // 2 + 1, cols // 2] = True
    cells_matrix[rows // 2 + 1, cols // 2 + 4] = True
    cells_matrix[rows // 2 + 1, cols // 2 + 8] = True

    cells_matrix[rows // 2 + 2, cols // 2] = True
    cells_matrix[rows // 2 + 2, cols // 2 + 8] = True
    cells_matrix[rows // 2 + 2, cols // 2 + 12] = True

    cells_matrix[rows // 2 + 3, cols // 2 + 1] = True
    cells_matrix[rows // 2 + 3, cols // 2 + 4] = True
    cells_matrix[rows // 2 + 3, cols // 2 + 8] = True
    cells_matrix[rows // 2 + 3, cols // 2 + 9] = True
    cells_matrix[rows // 2 + 3, cols // 2 + 10] = True
    cells_matrix[rows // 2 + 3, cols // 2 + 11] = True

    cells_matrix[rows // 2 + 5, cols // 2 + 5] = True
    cells_matrix[rows // 2 + 5, cols // 2 + 6] = True

    cells_matrix[rows // 2 + 6, cols // 2 + 5] = True
    cells_matrix[rows // 2 + 6, cols // 2 + 6] = True

    cells_matrix[rows // 2 + 7, cols // 2 + 5] = True
    cells_matrix[rows // 2 + 7, cols // 2 + 6] = True

    cells_matrix[rows // 2 + 9, cols // 2 + 1] = True
    cells_matrix[rows // 2 + 9, cols // 2 + 4] = True
    cells_matrix[rows // 2 + 9, cols // 2 + 8] = True
    cells_matrix[rows // 2 + 9, cols // 2 + 9] = True
    cells_matrix[rows // 2 + 9, cols // 2 + 10] = True
    cells_matrix[rows // 2 + 9, cols // 2 + 11] = True

    cells_matrix[rows // 2 + 10, cols // 2] = True
    cells_matrix[rows // 2 + 10, cols // 2 + 8] = True
    cells_matrix[rows // 2 + 10, cols // 2 + 12] = True

    cells_matrix[rows // 2 + 11, cols // 2] = True
    cells_matrix[rows // 2 + 11, cols // 2 + 4] = True
    cells_matrix[rows // 2 + 11, cols // 2 + 8] = True

    cells_matrix[rows // 2 + 12, cols // 2] = True
    cells_matrix[rows // 2 + 12, cols // 2 + 1] = True
    cells_matrix[rows // 2 + 12, cols // 2 + 2] = True
    cells_matrix[rows // 2 + 12, cols // 2 + 3] = True
    cells_matrix[rows // 2 + 12, cols // 2 + 9] = True
    cells_matrix[rows // 2 + 12, cols // 2 + 12] = True


def koks_galaxy(cells_matrix, game_settings):
    game_settings.periodic_boundaries = False
    rows, cols = row_col(game_settings)
    cells_matrix[rows // 2 - 5, cols // 2 - 1:cols // 2 + 5] = True
    cells_matrix[rows // 2 - 4, cols // 2 - 1:cols // 2 + 5] = True

    cells_matrix[rows // 2 + 2, cols // 2 - 4:cols // 2 + 2] = True
    cells_matrix[rows // 2 + 3, cols // 2 - 4:cols // 2 + 2] = True

    cells_matrix[rows // 2 - 5:rows // 2  + 1, cols // 2 - 4:cols // 2 - 2] = True
    cells_matrix[rows // 2 - 2:rows // 2  + 4, cols // 2 + 3:cols // 2 + 5] = True


# Auxiliary functions for the glider gun.
def square(cells_matrix, x, y):
    cells_matrix[x, y] = True
    cells_matrix[x - 1, y] = True
    cells_matrix[x, y + 1] = True
    cells_matrix[x - 1, y + 1] = True


def six_block(cells_matrix, x, y):
    cells_matrix[x + 1, y] = True
    cells_matrix[x - 1, y] = True
    cells_matrix[x, y + 1] = True
    cells_matrix[x - 1, y + 1] = True
    cells_matrix[x, y - 1] = True
    cells_matrix[x + 1, y - 1] = True


def vglider(cells_matrix, x, y):
    cells_matrix[x + 1, y - 1] = True
    cells_matrix[x, y - 1] = True
    cells_matrix[x - 1, y - 1] = True
    cells_matrix[x - 1, y] = True
    cells_matrix[x, y + 1] = True


def hglider(cells_matrix, x, y):
    cells_matrix[x - 1, y - 1] = True
    cells_matrix[x - 1, y] = True
    cells_matrix[x - 1, y + 1] = True
    cells_matrix[x, y - 1] = True
    cells_matrix[x + 1, y] = True
#######################################


def glider_gun(cells_matrix, game_settings):
    game_settings.periodic_boundaries = False
    rows, cols = row_col(game_settings)
    square(cells_matrix, rows // 2 - 2, cols // 2 - 17)
    square(cells_matrix, rows // 2 - 4, cols // 2 + 17)

    vglider(cells_matrix, rows // 2, cols // 2)
    vglider(cells_matrix, rows // 2 + 3, cols // 2 + 19)
    hglider(cells_matrix, rows // 2 + 8, cols // 2 + 8)

    six_block(cells_matrix, rows // 2 - 2, cols // 2 - 8)
    six_block(cells_matrix, rows // 2 - 4, cols // 2 + 6)


def exploder(cells_matrix, game_settings):
    game_settings.periodic_boundaries = False
    rows, cols = row_col(game_settings)
    cells_matrix[rows // 2 - 2:rows // 2 + 3, cols // 2 - 2] = True
    cells_matrix[rows // 2 - 2:rows // 2 + 3, cols // 2 + 2] = True
    cells_matrix[[rows // 2 - 2, rows // 2 + 2], cols // 2] = True
