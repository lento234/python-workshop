# Game of Life

## Description
Implement a [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) 2D 2D simulator. The rules of game of life are simple. Imagine a 2D grid with a initial random population of states: `live` or `dead`. Every cell interacts with its `8` neighbours, which are the cells horizontally, vertically, or diagonally adjacent. At each iteration, the states change according to the following rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Challenge

Implement using any numerical library such as `numpy` and visualize the states at each iteration using `matplotlib` and export the animation to `mp4` or `gif`. *Optionally: You may use other libary of choice (e.g. `numba`, `pytorch`, `taichi`, ...)*. Use the following initial conditions for your simulation:

* Image size: 512 x 512 px
* Initial probability of a cell to be `alive`: 15%
