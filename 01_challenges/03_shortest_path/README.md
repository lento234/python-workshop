# Shortest path

## Description

Given a `risk map` consisting of integer values from 1 to 9, find the shortest path that will minimize the total cost from top-left to bottom-right.

You start in the top left position, your destination is the bottom right position, and you **cannot move diagonally**. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. For example, the shortest path for the following risk map will give you a total cost of **40**.:

    1163751742
    1381373672
    2136511328
    3694931569
    7463417111
    1319128137
    1359912421
    3125421639
    1293138521
    2311944581

## Challenge

1. Find an efficient way to find the path and the total cost of the shortest path. Hint: There is an efficient algorithm for shortest path search. Minimum package dependency is `python standard libraries`, and `numpy`. First validate your approach for the above example. If you have verified the solution, solve a more challenging problem [map.txt](map.txt)

2. Plot the shortest path using `matplotlib` or similar plotting package.

3. (Optional): Package the approach as a python library. A functional-approach will suffice. See [python packaging user guide](https://packaging.python.org/en/latest/) and [poetry](https://python-poetry.org/docs/).
