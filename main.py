
import time
from rich.console import Console
import maze_solver as ms

console = Console()

console.print("[bold magenta]Welcome to Space Mouse, Officer![/bold magenta]")
console.print("[bold magenta]Your mission is to find the Romulan Space Cheese.[/bold magenta]")
console.print("[bold magenta]You are the first mouse to ever face the borg![/bold magenta]\n")

time.sleep(2)

console.print("You have just got a lock on the upper most floor of the borg cube.")
console.print("You are about to be beamed in. The cheese is below the lowest floor.\n")
console.print("Can you tell me how many cubes form one edge of the big borg mothership?\n")
side_length = int(input("Please enter a number: "))
console.print("\n*You are beamed in, and you are standing in the middle of the highest floor of the maze.*\n")

ms.maze_solver(side_length)
