		                       ****************
			               The Game of Life
			               ****************

This is a python (version 3.6.3) Game of Life implementation
(https://en.wikipedia.org/wiki/Conway's_Game_of_Life). The rules are:

1.Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2.Any live cell with two or three live neighbours lives on to the next generation.
3.Any live cell with more than three live neighbours dies, as if by overpopulation.
4.Any dead cell with exactly three live neighbours becomes a live cell, as if by 
reproduction.

The game runs in a 1280x720 pixels screen. It is possible to change this and other settings
(such as colours) in settings.py.

You can choose the initial configuration from a list displayed. To see the configuration 
just move the mouse's cursor over the name. To confirm a configuration click the name.
If you click in the black area you can make your own pattern in an interactive way. 
Press 'enter' once your configuration is ready.
The boundary conditions in the 'interactive mode' are periodic, e.i. upper and lower 
boundary are connected; the same applies for the left and right borders.

To pause the game press 'p'. To resume the game press 'p' again. When paused, the number of 
iterations is shown. When the game is paused, it is possible to advance to the next 
iteration by pressing the 'righ arrow' key.

To adjust the speed press the 'up arrow' key (to speed up) and the  'down arrow' key (to 
slow down). The lowest possible speed is roughly 2 iterations per second. The highest 
possible speed depends on your system.

To play the game just launch game_of_life.py. To exit the game click on the 'x' on the 
screen.

At any time you can return to the initial menu by pressing the 'escape' key.

The game uses three external libraries (all libraries are available via pip install):

-Pygame 
 (https://www.pygame.org/news). 
 Used for the graphics.
-Numpy 
 (http://www.numpy.org/). 
 Used to manage some arrays.
-Numba 
 (https://numba.pydata.org/). 
 Used to speed up the execution.


