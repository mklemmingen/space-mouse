"""
file that includes the maze_solver

it starts in the middle cube of the highest floor in a crater that consist of nothing [pass-through-walls]

we measure if the mouse has gone out of the cube if it has reached the lowestlevel -1 and
gained the status has_finished that ends the while-loop

the mouse has the strong urge to go to the lowest level of the maze, since 1. there is infamous
romulan space cheese down there and 2. in its algorithm of searching for the way, it first checks the
southern wall of the cube, then it checks the surrounding walls on the horizontal floor, at the end it checks
above. if it cant go up, it is stuck, and ends with output: "Agent Mouse to U.S.S. Muridae, I'm stuck.
Reqesting beam up!"


"""

import random
import time
from rich.console import Console

console = Console()
