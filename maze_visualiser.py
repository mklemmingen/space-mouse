"""
code that visualizes the maze

visualization:
            1.1.5 1.2.5 1.3.5 1.4.5 1.5.5
          1.1.4 1.2.4 1.3.4 1.4.4 1.5.4
        1.1.3 1.2.3 1.3.3 1.4.3 1.5.3
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

the cubes' wall being checked currently is orange, if it is checked positive for position-change,
it goes green, and the mouse position is updated to it.
if it is False for position change, it goes to the system standard again and checks the next one.
"""

# dict of name maze with dict inside the cubes with 6 keys with the names 1-6 with bool values


