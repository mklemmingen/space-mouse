# space-mouse

3D cube maze solver with visualisation and maze generator

-- space mouse against the borg --

generates a cube of a individual size consistent out of a lot of little cubes with random walls.
The mouse can only pass trough open gates or rare one-way gates. 

The space mouse starts in a crater that was created by a plasma torpedo at the top of the cube.

It looks for an opening and goes straight in, always wanting to go downwards to get to that sweet romulan cheese
at the other side of the cube. 

The visualisation mimics a spy-movie radar, where the cube that the mouse is in is visualised by seeing 
the top-down view of the cube and the front view of the cube - on either one the location is marked with a blinking
red dot. 

enjoy!

requirements:

import rich

------------
at the beginning of this project I had never seen either a generator for mazes or a solving algorithm before,
so I challenged myself to make one without looking any up:
- Generator:
maze in dict form, with a dict inside for each cube, that holds 6 keys with a bool value each.
The sum of cubes are determined by the parameter of edge_length of the big cube.
- Solver:
does basically two runs:
1. if the cube we want to be in has not been in before, we check: 1. below 2. right 3. forward 4. left 5. backwards
2. if the cube has been in, we check: 1. left 2. forward 3. right 4. backwards
if the corresponding walls of both the cube the mouse is in and the one she would like to be in are True (open), she moves there and checks again with the same cycle.
------------
the mouse wins if she has reached the lowest floor. 

