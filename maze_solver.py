"""
File that includes the maze_solver

It starts in the middle cube of the highest floor in a crater that consists of nothing [pass-through-walls]

We measure if the mouse has gone out of the cube if it has reached the lowest-level -1 and
gained the status has_finished that ends the while-loop

the mouse has the strong urge to go to the lowest level of the maze, since 1. there is infamous
romulan space cheese down there and 2. in its algorithm of searching for the way, it first checks the
southern wall of the cube, then it checks the surrounding walls on the horizontal floor, at the end it checks
above. If it cant go up, it is stuck, and ends with output: "Agent Mouse to U.S.S. Muridae, I'm stuck.
Requesting beam up!"


"""

import time
from rich.console import Console
import maze_visualiser as mv
import maze_generator as mg
import text_assets

console = Console()


def maze_solver(length: int):
    """
    Function that solves the maze
    :param length: side_length of the maze
    :return: None
    """
    # first, we need to find the starting point
    global wall_2, succesful, wall_2_non_bool
    current_position = f"{1}.{length // 2 + 1}.{length // 2 + 1}"
    # we need to know if the mouse has finished
    has_finished = False
    # we need to know if the mouse is stuck
    is_stuck = False
    # we need to know if the mouse has been in a cube before
    has_been_in_cube = []
    current_check = ""

    maze, all_cubes = mg.maze_creator(length)

    # while loop that runs until the mouse has finished
    while not has_finished:
        # start of the solving algorithm
        # checks if the walls of the cube from current_position are pass-through and
        # if the wall of the cube behind the wall of direction in current_position is pass-through
        # first checks the floor, then the walls[west, behind, east, forward], then the ceiling
        # does not check the wall if there is no cube behind it
        # does not check the ceiling if there is no cube above it
        # does check the floor if there is no cube below it
        # has_finished if the mouse has reached the lowest level -1

        # splits the current position into its five parts
        # like
        # ["1",   0
        # ".",    1
        # "2",    2
        # ".",    3
        # "3"]    4

        # wall positions:
        # 6: floor
        # 1: ceiling
        # 2: forward
        # 5: behind
        # 3: west
        # 4: east

        cur_ch_split = list(current_position)

        if current_position not in has_been_in_cube:
            has_been_in_cube.append(current_position)

        # wall below
        current_check = f"{str(int(cur_ch_split[0]) + 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"
        if current_check not in has_been_in_cube:
            mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)

            wall_1 = maze[current_position][6]
            wall_2_non_bool = f"{str(int(cur_ch_split[0]) + 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"
            wall_2 = maze[f"{str(int(cur_ch_split[0]) + 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"][1]
            time.sleep(0.2)

            if wall_1 and wall_2:
                if wall_2_non_bool == f"{length}.{cur_ch_split[2]}.{cur_ch_split[4]}":
                    has_finished = True
                    succesful = True
                    break
                current_position = wall_2_non_bool
                continue
            time.sleep(0.2)

        # wall to the right
        current_check = cur_ch_split[0] + "." + f"{str(int(cur_ch_split[2]) + 1)}" + "." + cur_ch_split[4]
        if current_check not in has_been_in_cube:
            mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
            wall_1 = maze[current_position][3]
            if int(cur_ch_split[4]) == length:
                wall_2 = False
            else:
                try:
                    wall_2_non_bool = f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) + 1)}.{cur_ch_split[4]}"
                    wall_2 = maze[f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) + 1)}.{cur_ch_split[4]}"][4]
                except KeyError:
                    # if wall not existent, set False to indicate that there is no cube behind the wall
                    wall_2 = False
                if wall_1 and wall_2:
                    current_position = wall_2_non_bool
                    continue
            time.sleep(0.2)

        # wall in front
        current_check = cur_ch_split[0] + "." + cur_ch_split[2] + "." + f"{str(int(cur_ch_split[4]) - 1)}"
        if current_check not in has_been_in_cube:
            mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
            wall_1 = maze[current_position][2]
            if int(cur_ch_split[4]) == 1:
                wall_2 = False
            else:
                try:
                    wall_2_non_bool = f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) - 1)}"
                    wall_2 = maze[f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) - 1)}"][5]
                except KeyError:
                    # if wall not existent, set False to indicate that there is no cube behind the wall
                    wall_2 = False
                if wall_1 and wall_2:
                    current_position = wall_2_non_bool
                    continue
            time.sleep(0.2)

        # wall to the left
        current_check = cur_ch_split[0] + "." + f"{str(int(cur_ch_split[2]) - 1)}" + "." + cur_ch_split[4]
        if current_check not in has_been_in_cube:
            mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
            wall_1 = maze[current_position][4]
            if int(cur_ch_split[2]) == 1:
                wall_2 = False
            else:
                try:
                    wall_2_non_bool = f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) - 1)}.{cur_ch_split[4]}"
                    wall_2 = maze[f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) - 1)}.{cur_ch_split[4]}"][3]
                except KeyError:
                    # if wall not existent, set False to indicate that there is no cube behind the wall
                    wall_2 = False
                if wall_1 and wall_2:
                    current_position = wall_2_non_bool
                    continue
            time.sleep(0.2)

        # wall in the back
        current_check = cur_ch_split[0] + "." + cur_ch_split[2] + "." + f"{str(int(cur_ch_split[4]) + 1)}"
        if current_check not in has_been_in_cube:
            mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
            wall_1 = maze[current_position][5]
            if int(cur_ch_split[4]) == length:
                wall_2 = False
            else:
                try:
                    wall_2_non_bool = f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) + 1)}"
                    wall_2 = maze[f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) + 1)}"][2]
                except KeyError:
                    # if wall not existent, set False to indicate that there is no cube behind the wall
                    wall_2 = False
                if wall_1 and wall_2:
                    current_position = wall_2_non_bool
                    continue
            time.sleep(0.2)

        # wall above
        current_check = f"{str(int(cur_ch_split[0]) - 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"
        if current_check not in has_been_in_cube:
            mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
            wall_1 = maze[current_position][1]

            if int(cur_ch_split[0]) == 1:
                wall_2 = False
            else:
                try:
                    wall_2_non_bool = f"{str(int(cur_ch_split[0]) - 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"
                    wall_2 = maze[f"{str(int(cur_ch_split[0]) - 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"][6]
                except KeyError:
                    # if wall not existent, set False to indicate that there is no cube behind the wall
                    wall_2 = False
            if wall_1 and wall_2:
                current_position = wall_2_non_bool
                continue
            time.sleep(0.2)

        # wall to the right
        current_check = cur_ch_split[0] + "." + f"{str(int(cur_ch_split[2]) + 1)}" + "." + cur_ch_split[4]
        mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
        wall_1 = maze[current_position][3]
        if int(cur_ch_split[4]) == length:
            wall_2 = False
        else:
            try:
                wall_2_non_bool = f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) + 1)}.{cur_ch_split[4]}"
                wall_2 = maze[f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) + 1)}.{cur_ch_split[4]}"][4]
            except KeyError:
                # if wall not existent, set False to indicate that there is no cube behind the wall
                wall_2 = False
            if wall_1 and wall_2:
                current_position = wall_2_non_bool
                continue
        time.sleep(0.2)

        # wall in front
        current_check = cur_ch_split[0] + "." + cur_ch_split[2] + "." + f"{str(int(cur_ch_split[4]) - 1)}"
        mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
        wall_1 = maze[current_position][2]
        if int(cur_ch_split[4]) == 1:
            wall_2 = False
        else:
            try:
                wall_2_non_bool = f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) - 1)}"
                wall_2 = maze[f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) - 1)}"][5]
            except KeyError:
                # if wall not existent, set False to indicate that there is no cube behind the wall
                wall_2 = False
            if wall_1 and wall_2:
                current_position = wall_2_non_bool
                continue
        time.sleep(0.2)

        # wall to the left
        current_check = cur_ch_split[0] + "." + f"{str(int(cur_ch_split[2]) - 1)}" + "." + cur_ch_split[4]
        mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
        wall_1 = maze[current_position][4]
        if int(cur_ch_split[2]) == 1:
            wall_2 = False
        else:
            try:
                wall_2_non_bool = f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) - 1)}.{cur_ch_split[4]}"
                wall_2 = maze[f"{cur_ch_split[0]}.{str(int(cur_ch_split[2]) - 1)}.{cur_ch_split[4]}"][3]
            except KeyError:
                # if wall not existent, set False to indicate that there is no cube behind the wall
                wall_2 = False
            if wall_1 and wall_2:
                current_position = wall_2_non_bool
                continue
        time.sleep(0.2)

        # wall in the back
        current_check = cur_ch_split[0] + "." + cur_ch_split[2] + "." + f"{str(int(cur_ch_split[4]) + 1)}"
        mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
        wall_1 = maze[current_position][5]
        if int(cur_ch_split[4]) == length:
            wall_2 = False
        else:
            try:
                wall_2_non_bool = f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) + 1)}"
                wall_2 = maze[f"{cur_ch_split[0]}.{cur_ch_split[2]}.{str(int(cur_ch_split[4]) + 1)}"][2]
            except KeyError:
                # if wall not existent, set False to indicate that there is no cube behind the wall
                wall_2 = False
            if wall_1 and wall_2:
                current_position = wall_2_non_bool
                continue
        time.sleep(0.2)

        # wall above
        current_check = f"{str(int(cur_ch_split[0]) - 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"
        mv.visualise_maze(length, all_cubes, current_check, current_position, has_been_in_cube)
        wall_1 = maze[current_position][1]

        if int(cur_ch_split[0]) == 1:
            wall_2 = False
        else:
            try:
                wall_2_non_bool = f"{str(int(cur_ch_split[0]) - 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"
                wall_2 = maze[f"{str(int(cur_ch_split[0]) - 1)}.{cur_ch_split[2]}.{cur_ch_split[4]}"][6]
            except KeyError:
                # if wall not existent, set False to indicate that there is no cube behind the wall
                wall_2 = False
        if wall_1 and wall_2:
            current_position = wall_2_non_bool
            continue
        time.sleep(0.2)

    if succesful:
        console.print(text_assets.mouse_art_win, highlight=False)
        console.print("The mouse has reached the cheese!")
    else:
        console.print("The mouse has not reached the cheese!")
        console.print(text_assets.mouse_art_lose, highlight=False)
    time.sleep(0.2)
    console.print("The mouse has been in the following cubes:")
    time.sleep(0.2)
    console.print(has_been_in_cube)
    time.sleep(0.2)
