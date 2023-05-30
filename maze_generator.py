# Author: Martin Lauterbach
import random

"""
Script with functions to create a 3-dimensional maze

The code should create a 3-dimensional cube maze with one in and one out,
consistent out of a changeable but quadratic number of blocks.

 The blocks have the number: [floor number top to bottom].[column number east to west].[number from front to back]

 Parameter: edge_length

             1.1.5 1.2.5 1.3.5 1.4.5 1.5.5
           1.1.4 1.2.4 1.3.4 1.4.4 1.5.4
         1.1.3 1.2.3 !1.3.3! 1.4.3 1.5.3
       1.1.2 1.2.2 1.3.2 1.4.2 1.5.2
     1.1.1 1.2.1 1.3.1 1.4.1 1.5.1

              2.1.5 2.3.5 2.3.5 2.4.5 2.5.5
           2.1.4 2.2.4 2.3.4 2.4.4 2.5.4
         2.1.3 2.2.3 2.3.3 2.4.3 2.5.3
       2.1.2 2.2.2 2.3.2 2.4.2 2.5.2
     2.1.1 2.2.1 2.3.1 2.4.1 2.5.1

           3.1.4 3.2.4 3.3.4 3.4.4 3.5.5
         3.1.3 3.2.3 3.3.3 3.4.3 3.5.3
       3.1.2 3.2.2 3.3.2 3.4.2 3.5.2
     3.1.1 3.2.1 3.3.1 3.4.1 3.5.1

             4.1.5 4.2.5 4.3.5 4.4.5 4.5.5
           4.1.4 4.2.4 4.3.4 4.4.4 4.5.4
         4.1.3 4.2.3 4.3.3 4.4.3 4.5.3
       4.1.2 4.2.2 4.3.2 4.4.2 4.5.2
     4.1.1 4.2.1 4.3.1 4.4.1 4.5.1

             5.1.5 5.2.5 5.3.5 5.4.5 5.5.5
           5.1.4 5.2.4 5.3.4 5.4.4 5.5.4
         5.1.3 5.2.3 5.3.3 5.4.3 5.5.3
       5.1.2 5.2.2 5.3.2 5.4.2 5.5.2
     5.1.1 5.2.1 5.3.1 5.4.1 5.5.1

 These blocks have 6 walls. Each wall has a number from one to 6 that is the same at every cube.
 We clone these cubes.
 Randomly, these walls receive either the value:
 0. non-pass-through 1. Pass-through
 to be implemented late stage: 2. pass-through-once

 There is a crater in the top floor of the cube and in the lowest

 The in for the space-mouse is a crater on top of the cube.
   Above him should be an impenetrable barrier, so that the computer cannot go up.
   The while loop should stop if none of the craters' walls are tested pass-through
 the out for the space-mouse is a crater at the bottom of the cube.

 1 parameter:
 what length should the edges have?
"""


def maze_creator(length: int):
    """
    Dict of name maze with cube names inside that hold 6 keys with the names 1-6 plus a bool value.
    Gives back a list of all cubes with name too.
    :param length:
    :return: A fully created 3-dimensional maze of cubes with 6 walls with bool values and a list of all cubes
    """
    maze = {}
    all_cubes = []
    # create the maze
    for floor in range(1, length + 1):
        for row in range(length, 0, -1):
            for column in range(1, length + 1):
                # creates the cubes with names like 1.1.1 in a dict
                maze[f"{floor}.{column}.{row}"] = {1: choose_TF(),
                                                   2: choose_TF(),
                                                   3: choose_TF(),
                                                   4: choose_TF(),
                                                   5: choose_TF(),
                                                   6: choose_TF()}
                # creates a list of all the cubes
                all_cubes.append(f"{floor}.{column}.{row}")
    return maze, all_cubes


def choose_TF() -> bool:
    """
    gives a random bool value
    :return: bool
    """
    return bool(random.choice([True, False]))
