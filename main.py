import random
import time
from rich.console import console
from rich.console import Console
import maze_visualiser as mv
import maze_generator as mg
import maze_solver as ms

console = Console()

console.print("[bold magenta]Welcome to Space Mouse, Officer![/bold magenta]!", justify="center")
console.print("[bold magenta]Your mission is to find the Romulan Space Cheese![/bold magenta]", justify="center")
console.print("[bold magenta]You are the first mouse to ever face the borg![/bold magenta]", justify="center")

time.sleep(2)

console.print("You have just got a lock on the upper most floor of the borg cube.", justify="center")
console.print("You are about to be beamed in, and you can practically smell the Romulan Space Cheese "
              "on the lowest floor.", justify="center")
console.print("How many cubes form one edge of the big borg mothership?", justify="center")
side_length = int(input("Please enter a number: "))
console.print("You are beamed in, and you are standing in the middle of the highest floor of the maze.",
              justify="center")

ms.maze_solver(side_length)
