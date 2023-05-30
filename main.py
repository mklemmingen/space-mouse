import time
from rich.console import Console
import maze_solver as ms

con = Console()


def typewriter(text, style: str, highlight: bool):
    """
    Function to print output with typewriter effect.
    This will print all the elements of the string one by one at a certain rate of an element per second.
    It uses a rich console print statement with typewriter().

    modified FORK from pywriter, licence MIT, rights to: Jesse Amarquaye, package: pywrite
    https://github.com/amarquaye/pywriter/blob/master/pywriter/__init__.py

    :param text: The data you would like to print
    :param style: style parameters, see rich documentation
    :param highlight: Bool Value if it should be auto-highlighted
    :return: output of a stylised text to the rich console
    """
    rate: float = 0.02

    for i in range(len(text)):
        con.print(text[i], end="", style=style, highlight=highlight)
        time.sleep(rate)


con.clear()
typewriter("Welcome to Space Mouse, Officer!\n", "default", False)
typewriter("Your mission is to find the Romulan Space Cheese.\n", "default", False)
typewriter("You are the first mouse to ever face the borg!\n\n", "default", False)

typewriter("\nYou have just got a lock on the upper most floor of the borg cube.\n", "default", False)
typewriter("You are about to be beamed in. The cheese is below the lowest floor.\n", "default", False)
typewriter("Can you tell me how many cubes form one edge of the big borg mothership?\n", "default", False)

not_good_enough = True
while not_good_enough:
    side_length = int(input("Please enter a number: "))
    if side_length < 2 or side_length % 2 == 0:
        typewriter("That is not a valid number. Please enter a number greater than 1 and uneven.", "default", False)
    else:
        not_good_enough = False

typewriter("\n*You are beamed in, and you are standing in the middle of the highest floor of the maze.*\n",
           "default", False)

# noinspection PyUnboundLocalVariable
ms.maze_solver(side_length)

# ask user if they want to play again
play_again = input("Do you want to play again? (y/n)")
if play_again == "y":
    typewriter("Restart not available yet. Please restart the program manually.", "default", False)
    time.sleep(1)
    con.clear()
    exit()
else:
    typewriter("Goodbye!", "default", False)
    time.sleep(1)
    con.clear()
    exit()
