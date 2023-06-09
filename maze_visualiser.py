# Authors: Martin Lauterbach

from rich.console import Console
# imports assets from the python code text.assets
import text_assets


def visualise_maze(length_of_side: int, all_cubes: list,
                   current_check: str, current_position: str,
                   passed_cubes: list) -> None:
    """
    visualises the maze
    :param all_cubes: list of all cubes,
    :param passed_cubes: list of cubes that have been passed
    :param length_of_side: the length of the cubes edges
    :param current_check: the current check of the mouse,
    :param current_position: the current position of the mouse
    :return: a printed with rich colours and terminal size adjusted maze
    """
    """
    the maze is a 3d array, with the first dimension being the floor,
    the second being the row,
    and the third being column
    """
    # wall positions:
    # 6: floor
    # 1: ceiling
    # 2: forward
    # 5: behind
    # 3: west
    # 4: east
    """
    visualization should look like that:
                    1.1.5 1.2.5 1.3.5 1.4.5 1.5.5
                 1.1.4 1.2.4 1.3.4 1.4.4 1.5.4
            1.1.3 1.2.3 1.3.3 1.4.3 1.5.3
        1.1.2 1.2.2 1.3.2 1.4.2 1.5.2
    1.1.1 1.2.1 1.3.1 1.4.1 1.5.1
    
                    2.1.5 2.2.5 2.3.5 2.4.5 2.5.5
                2.1.4 2.2.4 2.3.4 2.4.4 2.5.4
            2.1.3 2.2.3 2.3.3 2.4.3 2.5.3
        2.1.2 2.2.2 2.3.2 2.4.2 2.5.2
    2.1.1 2.2.1 2.3.1 2.4.1 2.5.1
    
                    3.1.5 3.2.5 3.3.5 3.4.5 3.5.5
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
    
    the cubes' wall being checked currently is orange, 
    if it is checked positive for the wall being passable and
    the wall behind it being passable too, it turns green and the mouse position is updated to it.
    if it is False for position change, it goes to the system standard colour again and checks the next one.
    
    whether a wall is being checked or not is determined by the current_check variable, which is a string.
    what the position of the mouse is is determined by the current_position variable, which is a string.
    
    """
    # creates a console object
    console = Console()
    # clears the console
    console.clear()
    # variables containing styles of specific events
    mouse = "#f90404"
    checking = "#f99304"
    positive = "#56f904"
    passed = "#04f9f9"

    # checks whether the current_check is north, south, east, west before or after the current_position
    # and prints and prints a mouse from text_assets that is facing the right direction

    # splits the current position into its five parts
    # like ["1",".","2",".","3"]
    cur_ch_split = list(current_position)

    # if current_check is same_floor-1.same_row.same_column -> mouse is facing down
    if current_check == f"{str(int(cur_ch_split[0]) - 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}":
        console.print(text_assets.mouse_down, style=mouse, highlight=False)
    # if current_check is same_floor.same_row.same_column+1 -> mouse is facing backwards
    elif current_check == f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) + 1)}":
        console.print(text_assets.mouse_backwards, style=mouse, highlight=False)
    # if current_check is same_floor.same_row.same_column-1 -> mouse is facing forwards
    elif current_check == f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) - 1)}":
        console.print(text_assets.mouse_forwards, style=mouse, highlight=False)
    # if current_check is same_floor.same_row+1.same_column -> mouse is facing right
    elif current_check == f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) + 1)}.{cur_ch_split[4]}":
        console.print(text_assets.mouse_right, style=mouse, highlight=False)
    # if current_check is same_floor.same_row-1.same_column -> mouse is facing left
    elif current_check == f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) - 1)}.{cur_ch_split[4]}":
        console.print(text_assets.mouse_left, style=mouse, highlight=False)
    # if current_check is same_floor+1.same_row.same_column -> mouse is facing up
    elif current_check == f"{str(int(cur_ch_split[0]) + 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}":
        console.print(text_assets.mouse_up, style=mouse, highlight=False)

    # for-loop that goes through a list of all possible names for cubes in the maze.
    # like in the docstring above, each floor is its own block of cubes, with each row being a line of cubes
    # and each column being a column of cubes. with each row into the back, a tab is added.
    # if the number is the same as the checking number, it is coloured orange.
    # if the number is the same as the mouse number, it is coloured red.
    # if the number is the same as the positive number, it is coloured green.
    # if the number is in the list of passed cubes, it is coloured blue.
    # if cube is the first from left in the last row, it has length_of_side-1 tabs added to it

    space = " "
    for cube in all_cubes:
        split_cube = list(cube)
        # if cube is the first from the left in a row, adds the number of tabs equal to the row number
        if cube == f"{split_cube[0]}.1.{split_cube[4]}":
            filler = space * (int(split_cube[4]) - 1)
            console.print(filler, end="")

        if cube == current_check:
            console.print(cube, style=checking, end=" ", highlight=False)
        elif cube == current_position:
            console.print(cube, style=mouse, end=" ", highlight=False)
        elif cube == positive:
            console.print(cube, style=positive, end=" ", highlight=False)
        elif cube in passed_cubes:
            console.print(cube, style=passed, end=" ", highlight=False)
        else:
            console.print(cube, end=" ", highlight=False)

        if cube == f"{split_cube[0]}.{length_of_side}.{split_cube[4]}":
            console.print("\n", end="")
        if cube == f"{split_cube[0]}.{length_of_side}.1":
            console.print("\n", end="")

    return
