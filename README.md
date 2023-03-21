# Conway's PyGame of Life
This is a Python implementation of Conway's Game of Life using Pygame. The simulation is displayed on a 500x500 screen, where cells are color-coded based on the number of live neighbors they have.

### How to Play
To start the simulation, click the "Start" button. To stop the simulation, click the "Stop" button. To clear the screen, click the "Clear" button. To randomize the cells on the screen, click the "Randomize" button.

### How the Game Works
Conway's Game of Life is a cellular automaton created by mathematician John Conway in 1970. The game is played on a two-dimensional grid of cells, where each cell can be in one of two states: alive or dead.

The game progresses through a series of generations, where the state of each cell in the next generation is determined by its current state and the states of its eight neighbors. The rules for determining the state of each cell are as follows:

* A live cell with fewer than two live neighbors dies (underpopulation).
* A live cell with two or three live neighbors survives to the next generation.
* A live cell with more than three live neighbors dies (overpopulation).
* A dead cell with exactly three live neighbors becomes alive (reproduction).

With these simple rules, complex patterns can emerge, including oscillators, gliders, and spaceships.

To learn more about Conway's Game of Life, see the Wikipedia page: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

![image](https://user-images.githubusercontent.com/115204665/226490892-b9ac684a-bba2-4526-8975-91fb92497d92.png)

### How to Run
To run the game, simply execute the pygame_of_life.py script.
