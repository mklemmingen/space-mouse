# script with functions to create a 3 dimensional maze

# the code should create a 3 dimensional cube maze with one in and one out, 
# consistent out of a changeable but quadratic number of blocks.

# the blocks have the number: [floor number bottom to top].[column number east to west].[number from front to back]
# these blocks have 6 walls. each wall has a number from one to 6 that is the same at every cube.
# we clone these cubes. 
# randomly, these walls receive either the value:
# 0. non-pass-through 1. pass-through 2. pass-through-once

# the in for the space-mouse is a crater on top of the cube. 
# the out for the space-mouse is a crater at the bottom of the cube. 

# 2 parameters:
# depth of the cube and how to tall it is
