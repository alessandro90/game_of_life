# Game of Life

This is a python (version 3.6.3) [Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) implementation. The rules are:

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by 
reproduction.

The game runs in a 1280x720 pixels screen. It is possible to change this and other settings
(such as colours) in `settings.py`.

You can choose the initial configuration from a list displayed. To see the configuration 
just move the mouse's cursor over the name. To confirm a configuration click the name.
If you click in the black area you can make your own pattern in an interactive way. 
Press `ENTER` once your configuration is ready.
The boundary conditions in the "interactive mode" are periodic, *e.i.* upper and lower 
boundary are connected; the same applies for the left and right borders.

To pause the game press `P`. To resume the game press `P` again. When paused, the number of 
iterations is shown. When the game is paused, it is possible to advance to the next 
iteration by pressing the `RIGHT` arrow key.

To adjust the speed press the `UP` arrow key (to speed up) and the  `DOWN` arrow key (to 
slow down).

To play the game just launch `game_of_life.py`. To exit the game click on the `x` on the 
screen.

At any time you can return to the initial menu by pressing the `ESCAPE` key.

#### Dependencies

- [Pygame](https://www.pygame.org/news); 
- [Numpy](http://www.numpy.org/);
- [Numba](https://numba.pydata.org/).


