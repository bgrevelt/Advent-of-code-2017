'''
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

    ne,ne,ne is 3 steps away.
    ne,ne,sw,sw is 0 steps away (back where you started).
    ne,ne,s,s is 2 steps away (se,se).
    se,sw,se,sw,sw is 3 steps away (s,s,sw).

--- Part Two ---

How many steps away is the furthest he ever got from his starting position?


'''
puzzle_input = '''n,ne,ne,se,se,se,se,s,se,se,sw,s,s,s,s,s,sw,sw,s,sw,sw,sw,sw,s,sw,sw,sw,nw,nw,n,nw,n,sw,sw,nw,nw,nw,nw,nw,n,s,nw,nw,nw,n,se,nw,n,s,ne,se,n,n,nw,ne,n,nw,nw,n,nw,sw,n,n,n,n,n,s,n,n,n,ne,ne,ne,ne,se,n,ne,n,n,n,n,ne,ne,sw,n,n,ne,ne,ne,ne,ne,ne,sw,ne,se,ne,ne,ne,ne,se,ne,ne,sw,ne,s,n,n,s,se,ne,se,n,se,ne,se,se,ne,ne,ne,ne,ne,ne,ne,se,ne,ne,se,se,se,ne,se,s,nw,se,ne,se,n,se,se,s,se,se,se,sw,n,se,se,se,se,se,se,n,se,s,se,sw,se,nw,se,se,se,se,se,se,se,sw,sw,s,nw,s,se,nw,se,se,s,s,se,se,s,se,nw,nw,se,s,se,se,s,s,s,s,se,s,s,s,nw,s,se,ne,s,s,n,s,s,sw,s,nw,se,nw,s,s,s,n,s,s,s,nw,s,sw,s,s,s,se,s,s,n,nw,s,s,s,s,s,sw,s,s,se,s,s,s,s,sw,ne,s,s,s,s,s,sw,ne,s,s,s,sw,sw,nw,s,s,s,sw,nw,s,ne,sw,s,s,s,s,s,sw,s,sw,ne,sw,sw,sw,s,sw,sw,nw,s,s,s,s,s,n,sw,sw,ne,sw,sw,s,nw,sw,sw,s,sw,sw,sw,nw,sw,s,sw,s,sw,ne,s,sw,nw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,sw,n,s,sw,sw,sw,sw,sw,nw,sw,sw,se,sw,sw,sw,sw,sw,se,sw,sw,sw,sw,nw,sw,sw,nw,sw,sw,sw,nw,nw,sw,sw,sw,sw,nw,sw,nw,ne,sw,sw,sw,n,ne,nw,sw,se,nw,sw,nw,nw,sw,sw,sw,ne,nw,sw,sw,sw,sw,ne,sw,s,sw,sw,sw,sw,nw,s,se,sw,nw,nw,nw,nw,s,sw,sw,sw,nw,s,nw,nw,se,n,sw,nw,nw,nw,sw,nw,sw,nw,ne,n,se,nw,nw,sw,s,sw,nw,nw,sw,sw,s,nw,nw,nw,nw,nw,sw,sw,sw,s,sw,nw,nw,nw,sw,sw,nw,nw,sw,se,nw,nw,nw,sw,s,ne,s,sw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,sw,nw,n,nw,nw,nw,nw,nw,s,sw,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,s,nw,n,nw,nw,n,nw,nw,nw,nw,nw,s,nw,n,nw,nw,se,n,ne,s,nw,nw,nw,nw,nw,nw,nw,nw,se,s,se,nw,s,nw,se,nw,n,n,sw,nw,nw,nw,nw,nw,n,nw,nw,nw,n,n,nw,n,n,nw,nw,sw,sw,s,nw,nw,nw,ne,s,se,n,ne,nw,nw,nw,n,n,nw,n,sw,n,s,n,nw,nw,n,n,se,n,n,nw,n,n,n,nw,nw,n,n,ne,ne,nw,se,nw,n,n,nw,n,n,sw,nw,n,nw,n,n,n,n,n,n,nw,sw,n,nw,n,se,nw,n,nw,n,n,n,n,n,n,nw,sw,n,n,n,nw,n,nw,n,nw,nw,s,nw,n,n,n,n,nw,nw,nw,n,n,n,n,nw,n,nw,n,ne,s,n,nw,nw,n,n,nw,n,n,n,n,n,n,nw,s,n,n,nw,se,n,n,n,n,nw,n,n,s,n,se,n,n,n,n,n,se,n,n,nw,n,se,n,n,n,n,n,n,ne,se,se,nw,n,nw,n,n,ne,se,n,n,n,n,ne,n,n,s,n,n,n,n,s,s,sw,ne,n,n,n,se,n,n,n,se,n,n,ne,ne,n,n,ne,ne,ne,n,n,n,n,n,ne,ne,s,n,n,sw,n,n,n,sw,ne,n,n,n,ne,ne,ne,ne,n,ne,nw,ne,n,ne,n,ne,sw,sw,s,n,ne,n,n,ne,s,ne,nw,n,ne,ne,se,n,ne,n,ne,sw,n,n,ne,ne,ne,n,ne,n,ne,n,nw,ne,n,ne,ne,s,nw,ne,n,n,ne,ne,n,n,n,n,n,n,s,n,n,ne,n,ne,n,n,n,sw,n,sw,ne,s,ne,ne,n,s,n,n,n,n,s,s,nw,ne,s,ne,ne,n,n,ne,ne,n,n,n,sw,ne,n,ne,ne,s,n,ne,ne,ne,ne,n,ne,s,n,ne,nw,ne,ne,ne,n,n,se,n,ne,ne,ne,se,n,ne,ne,n,n,ne,ne,n,se,ne,ne,nw,ne,ne,s,n,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,n,n,ne,n,ne,n,s,nw,ne,ne,ne,sw,ne,ne,s,n,s,nw,ne,s,n,ne,n,ne,n,ne,ne,ne,nw,ne,nw,ne,n,ne,s,ne,n,se,n,ne,s,ne,ne,s,se,n,ne,ne,ne,ne,ne,ne,ne,n,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,sw,ne,nw,s,s,ne,ne,ne,ne,ne,ne,se,ne,se,se,ne,nw,ne,nw,s,ne,se,se,ne,se,ne,nw,ne,n,ne,s,se,ne,ne,sw,n,nw,ne,se,ne,s,ne,ne,s,nw,ne,ne,ne,se,ne,nw,ne,ne,se,ne,ne,ne,ne,ne,ne,s,ne,ne,se,ne,nw,ne,ne,ne,ne,s,ne,ne,n,s,ne,ne,nw,se,ne,s,n,s,ne,ne,nw,ne,sw,ne,se,se,ne,s,n,se,ne,s,ne,ne,ne,ne,se,se,n,se,ne,se,se,ne,se,ne,nw,ne,ne,ne,se,n,ne,se,se,ne,ne,ne,ne,ne,ne,ne,s,se,ne,sw,se,n,ne,se,ne,ne,se,se,se,ne,se,ne,ne,se,se,ne,se,ne,ne,se,nw,se,nw,se,s,se,ne,se,s,se,se,s,sw,se,ne,ne,ne,se,s,ne,se,se,se,se,se,ne,ne,ne,se,se,se,n,se,ne,se,ne,ne,se,se,ne,ne,ne,nw,n,ne,se,n,ne,nw,se,ne,n,se,se,se,ne,ne,se,s,n,ne,s,se,se,s,ne,se,ne,se,se,se,se,se,ne,se,ne,ne,se,se,ne,ne,se,ne,se,nw,n,se,ne,ne,se,n,se,se,se,se,ne,se,se,se,se,se,se,n,se,se,s,se,se,se,se,se,ne,s,se,nw,se,se,se,ne,se,nw,ne,nw,se,se,se,s,se,se,s,s,s,se,ne,se,se,se,se,se,se,se,se,ne,se,se,ne,ne,se,se,se,se,ne,sw,sw,se,sw,se,nw,n,se,se,nw,n,se,ne,se,se,n,se,se,se,se,s,se,se,se,se,se,ne,se,s,ne,ne,ne,se,se,ne,se,se,ne,se,se,se,se,se,se,se,se,s,se,se,se,ne,se,se,s,se,se,se,n,se,se,se,se,sw,se,se,se,se,se,se,ne,n,se,se,se,ne,se,se,se,ne,se,se,s,se,n,se,se,nw,se,se,ne,n,se,se,se,sw,se,se,nw,se,n,nw,se,se,se,se,se,se,se,se,se,se,se,s,se,se,se,se,n,sw,se,se,se,sw,se,se,s,se,se,se,se,s,se,se,se,se,sw,sw,se,se,s,se,n,se,n,s,se,se,se,se,ne,s,sw,sw,s,se,se,nw,se,n,s,se,se,se,se,s,nw,nw,s,s,n,nw,se,se,se,se,se,sw,se,s,sw,se,ne,se,se,se,se,nw,se,se,sw,n,se,se,se,se,se,sw,se,ne,s,se,nw,s,n,se,se,se,se,nw,ne,se,se,s,se,se,ne,se,se,s,se,se,se,se,nw,s,s,se,se,s,se,se,se,se,s,se,se,se,sw,se,n,n,se,nw,se,sw,se,se,se,se,se,se,se,n,ne,s,se,ne,s,se,nw,s,s,se,nw,se,se,se,s,ne,se,s,se,sw,se,s,se,se,se,se,se,se,se,s,s,se,se,se,s,se,se,se,se,se,nw,se,s,n,se,se,se,ne,se,sw,se,nw,s,s,n,sw,n,se,ne,se,s,se,n,se,se,se,se,se,ne,se,sw,s,nw,s,se,ne,s,se,se,se,s,se,s,sw,s,n,s,se,se,se,se,s,se,se,se,se,s,se,se,nw,ne,se,s,s,nw,s,se,s,se,se,se,se,s,se,nw,s,s,se,se,ne,s,se,s,nw,se,n,nw,s,se,s,s,s,sw,ne,se,s,s,nw,se,s,se,s,s,s,s,nw,s,s,s,se,s,se,se,se,n,se,s,se,s,n,sw,se,se,s,nw,se,s,se,ne,ne,se,se,nw,ne,se,se,s,se,se,nw,sw,se,ne,ne,s,s,se,n,s,n,se,ne,s,s,se,sw,s,s,se,se,s,s,se,se,s,s,ne,s,sw,se,s,se,sw,s,s,s,se,s,ne,s,n,nw,s,s,s,s,sw,s,s,n,s,s,sw,s,s,se,s,sw,se,s,se,se,n,s,se,s,nw,se,s,se,se,s,nw,s,se,s,n,s,s,s,s,s,s,s,s,se,sw,s,s,s,se,s,ne,n,s,se,se,se,ne,s,se,ne,s,sw,s,ne,s,ne,s,s,sw,s,n,s,s,nw,s,sw,s,sw,s,s,s,n,s,s,n,s,nw,s,s,s,s,se,se,s,ne,s,se,s,s,s,s,s,s,s,s,se,s,s,s,s,s,sw,se,s,s,s,s,n,se,s,s,s,s,ne,nw,nw,s,s,se,s,s,s,s,s,s,s,s,s,s,ne,s,se,se,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,n,n,s,s,s,s,n,se,s,n,nw,s,n,s,s,s,s,s,s,s,s,n,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,se,s,s,s,s,n,s,s,s,s,s,sw,s,sw,s,sw,s,s,s,s,s,s,n,s,s,s,s,s,s,s,se,s,s,s,n,s,n,s,s,s,ne,ne,s,sw,nw,s,s,s,s,sw,s,s,s,s,se,nw,s,s,sw,s,sw,s,s,nw,s,s,n,s,sw,s,n,s,n,nw,s,n,s,s,s,s,s,s,sw,n,s,s,s,s,sw,s,s,s,s,s,s,nw,se,s,s,nw,s,s,s,s,s,sw,s,sw,s,s,nw,se,sw,s,s,s,s,nw,sw,sw,nw,sw,s,s,sw,nw,s,sw,s,s,s,s,sw,s,s,s,s,s,s,s,s,s,s,s,ne,s,s,s,s,s,se,nw,s,s,n,s,s,s,sw,s,s,sw,s,s,s,s,s,s,nw,sw,s,s,sw,n,s,s,sw,sw,s,ne,s,nw,se,s,nw,sw,s,s,s,sw,s,s,s,sw,s,nw,se,sw,s,sw,s,s,s,s,sw,sw,sw,s,s,s,nw,ne,sw,s,sw,n,s,s,se,ne,sw,sw,nw,s,s,s,s,s,sw,sw,s,s,s,sw,sw,s,s,s,n,s,ne,nw,sw,sw,s,s,sw,nw,sw,s,sw,se,s,n,s,s,s,s,s,s,nw,sw,sw,sw,n,nw,sw,s,s,s,se,s,s,nw,s,s,s,s,nw,s,s,sw,s,ne,s,sw,s,sw,s,s,sw,sw,sw,sw,s,s,s,s,sw,s,s,sw,nw,s,s,s,ne,s,s,s,sw,s,se,s,sw,s,s,s,s,sw,s,sw,s,ne,sw,se,s,s,sw,s,n,sw,se,sw,sw,s,s,sw,ne,se,s,se,sw,sw,sw,sw,s,sw,nw,s,s,s,s,sw,n,sw,nw,sw,s,sw,sw,sw,s,sw,s,sw,sw,s,sw,sw,sw,s,sw,s,s,sw,s,sw,s,sw,sw,s,s,s,sw,s,n,sw,sw,sw,s,sw,sw,sw,s,ne,sw,sw,sw,se,s,s,s,s,sw,s,sw,n,n,s,s,se,s,sw,sw,nw,sw,nw,sw,s,s,ne,n,sw,s,s,s,s,s,sw,sw,sw,s,sw,ne,s,sw,se,sw,sw,s,sw,ne,s,sw,sw,sw,sw,sw,sw,s,sw,sw,s,s,sw,s,sw,ne,sw,sw,sw,s,sw,sw,s,s,sw,sw,sw,s,sw,s,se,sw,se,sw,sw,sw,sw,sw,s,sw,sw,sw,se,sw,sw,sw,ne,s,sw,sw,sw,sw,se,s,n,s,s,sw,sw,sw,sw,s,sw,sw,n,se,s,sw,n,sw,sw,s,n,sw,s,sw,n,n,s,ne,sw,sw,sw,ne,sw,sw,sw,sw,sw,sw,s,se,sw,se,sw,sw,sw,sw,sw,sw,s,sw,sw,s,s,sw,n,sw,sw,sw,sw,nw,sw,nw,sw,s,sw,ne,s,sw,ne,sw,se,sw,s,sw,n,sw,sw,nw,ne,s,sw,sw,s,se,se,sw,s,se,se,sw,s,sw,sw,se,sw,ne,sw,ne,sw,n,s,sw,s,s,sw,sw,sw,sw,s,s,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,se,ne,sw,nw,sw,sw,sw,sw,sw,sw,ne,sw,s,s,s,s,sw,s,sw,s,sw,s,sw,sw,sw,sw,s,sw,sw,s,sw,ne,se,s,s,nw,sw,n,sw,sw,s,sw,sw,sw,se,sw,sw,nw,sw,sw,sw,sw,sw,sw,sw,sw,s,n,ne,sw,s,sw,sw,n,ne,sw,sw,sw,se,sw,sw,ne,sw,sw,se,sw,sw,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,nw,nw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,ne,sw,sw,sw,nw,ne,s,sw,s,sw,sw,sw,ne,sw,sw,sw,sw,sw,sw,sw,sw,se,s,se,sw,n,sw,sw,s,sw,n,n,s,sw,sw,sw,nw,sw,sw,sw,sw,sw,se,sw,sw,sw,nw,ne,sw,n,sw,nw,sw,sw,sw,n,sw,sw,sw,sw,se,sw,se,nw,nw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,n,sw,sw,ne,sw,sw,sw,sw,sw,se,sw,sw,n,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,ne,sw,sw,n,sw,nw,sw,sw,sw,se,s,sw,sw,n,sw,sw,sw,sw,s,n,sw,ne,sw,sw,n,s,sw,sw,se,sw,sw,nw,sw,ne,sw,sw,sw,ne,sw,se,sw,sw,sw,sw,nw,sw,nw,s,sw,sw,sw,sw,sw,sw,sw,sw,ne,sw,ne,sw,nw,s,sw,sw,nw,sw,sw,sw,se,nw,sw,sw,ne,nw,sw,sw,sw,sw,sw,ne,nw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,s,s,sw,s,nw,sw,sw,sw,sw,nw,sw,se,sw,sw,se,sw,sw,nw,sw,sw,sw,s,sw,sw,nw,sw,nw,sw,sw,sw,sw,se,sw,sw,sw,s,nw,sw,ne,sw,s,sw,sw,nw,sw,nw,sw,sw,nw,n,sw,sw,sw,sw,nw,sw,s,ne,sw,sw,sw,sw,nw,sw,sw,sw,sw,sw,nw,sw,s,sw,sw,sw,n,sw,nw,nw,sw,se,sw,sw,sw,sw,n,sw,sw,sw,sw,sw,sw,s,sw,nw,sw,nw,s,sw,sw,sw,nw,nw,sw,sw,sw,se,s,sw,sw,nw,sw,nw,sw,sw,sw,n,sw,sw,nw,sw,sw,n,sw,se,sw,nw,nw,nw,sw,sw,nw,nw,sw,sw,ne,sw,sw,sw,n,sw,nw,nw,sw,nw,s,sw,sw,nw,sw,sw,sw,s,sw,n,sw,sw,sw,ne,nw,sw,sw,sw,nw,nw,sw,ne,sw,nw,sw,nw,sw,n,nw,sw,sw,sw,nw,s,s,se,sw,sw,sw,nw,sw,sw,nw,nw,sw,sw,n,sw,n,sw,nw,n,sw,nw,nw,se,sw,sw,sw,sw,sw,sw,ne,s,nw,sw,sw,sw,sw,sw,sw,nw,se,ne,se,sw,nw,nw,sw,sw,sw,sw,ne,nw,sw,sw,sw,sw,nw,sw,n,sw,sw,se,nw,sw,nw,nw,sw,sw,nw,nw,sw,sw,sw,nw,s,nw,nw,nw,nw,sw,sw,ne,sw,nw,sw,sw,sw,sw,sw,se,sw,sw,sw,nw,ne,n,s,s,sw,sw,n,sw,sw,sw,sw,sw,s,nw,ne,sw,nw,sw,sw,nw,se,ne,sw,nw,se,sw,sw,sw,nw,s,sw,sw,sw,s,nw,sw,n,se,sw,sw,sw,nw,nw,s,sw,nw,sw,sw,nw,nw,sw,n,sw,sw,nw,sw,sw,sw,nw,sw,n,sw,nw,nw,sw,nw,sw,nw,nw,nw,ne,ne,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,ne,sw,sw,nw,s,ne,s,nw,ne,sw,sw,sw,n,se,nw,sw,nw,sw,nw,sw,n,se,sw,sw,nw,s,sw,ne,nw,sw,sw,nw,ne,nw,sw,sw,nw,nw,sw,sw,n,nw,sw,nw,sw,se,sw,nw,sw,sw,nw,ne,sw,se,nw,se,nw,nw,sw,nw,nw,nw,se,se,sw,sw,nw,nw,sw,sw,nw,nw,sw,nw,nw,sw,sw,s,nw,nw,sw,nw,sw,nw,sw,sw,sw,nw,sw,se,n,sw,nw,nw,sw,nw,sw,ne,nw,nw,sw,sw,nw,nw,nw,sw,nw,sw,sw,n,nw,nw,n,nw,nw,s,sw,se,nw,sw,sw,sw,sw,nw,sw,sw,sw,sw,se,s,sw,sw,nw,nw,s,nw,nw,sw,nw,ne,nw,nw,nw,sw,nw,ne,sw,ne,nw,sw,sw,s,sw,ne,sw,sw,sw,nw,nw,sw,nw,nw,nw,sw,nw,nw,sw,nw,nw,nw,se,nw,nw,nw,sw,nw,nw,sw,sw,sw,nw,sw,ne,se,nw,sw,nw,sw,ne,nw,sw,n,sw,nw,nw,nw,nw,nw,nw,nw,ne,nw,nw,sw,sw,sw,sw,se,n,sw,nw,n,nw,nw,s,ne,nw,n,nw,n,nw,nw,nw,s,nw,sw,sw,nw,s,n,ne,nw,ne,nw,nw,nw,se,ne,n,s,sw,sw,sw,sw,nw,nw,ne,sw,nw,n,ne,nw,nw,nw,sw,nw,nw,nw,nw,sw,nw,nw,sw,nw,se,nw,nw,nw,nw,ne,n,sw,nw,nw,nw,nw,sw,sw,nw,nw,sw,nw,s,nw,nw,s,nw,sw,sw,sw,nw,ne,s,nw,sw,sw,nw,s,sw,nw,sw,sw,nw,s,nw,nw,nw,se,nw,nw,sw,sw,sw,sw,sw,nw,sw,s,nw,se,nw,ne,se,sw,sw,nw,nw,nw,nw,se,nw,nw,s,nw,nw,n,nw,ne,nw,nw,nw,nw,sw,s,nw,nw,nw,nw,s,sw,sw,nw,nw,nw,nw,sw,nw,n,n,sw,sw,nw,sw,nw,nw,sw,nw,s,nw,ne,nw,nw,nw,nw,nw,nw,sw,n,sw,nw,nw,nw,nw,nw,nw,sw,nw,nw,ne,nw,nw,se,nw,sw,nw,nw,ne,nw,nw,nw,n,nw,nw,nw,sw,nw,nw,nw,nw,nw,sw,nw,sw,nw,nw,sw,ne,nw,n,ne,sw,nw,sw,nw,nw,nw,nw,sw,nw,n,nw,ne,nw,sw,nw,nw,sw,sw,nw,sw,nw,nw,nw,nw,se,nw,se,nw,nw,nw,sw,nw,nw,nw,nw,n,s,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,sw,sw,nw,sw,nw,nw,sw,sw,nw,nw,nw,nw,ne,nw,nw,sw,sw,nw,s,nw,sw,nw,ne,nw,nw,nw,nw,nw,nw,nw,sw,nw,sw,s,nw,nw,nw,nw,nw,n,nw,s,ne,nw,nw,sw,se,nw,nw,nw,s,nw,n,se,nw,nw,nw,nw,s,nw,n,sw,nw,s,nw,sw,nw,sw,nw,nw,nw,nw,nw,nw,n,sw,nw,nw,nw,n,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,nw,nw,sw,nw,nw,ne,nw,nw,nw,nw,nw,sw,nw,nw,nw,sw,se,sw,nw,sw,ne,nw,nw,nw,nw,nw,nw,sw,n,nw,nw,sw,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,se,nw,nw,nw,sw,nw,sw,sw,nw,nw,ne,nw,s,sw,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,nw,ne,nw,nw,nw,s,nw,nw,nw,nw,n,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,n,nw,nw,nw,nw,se,nw,n,ne,nw,nw,nw,n,nw,nw,nw,se,n,nw,ne,n,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,se,nw,s,nw,nw,nw,nw,ne,nw,nw,n,n,nw,nw,sw,nw,n,s,nw,nw,nw,nw,nw,n,s,nw,nw,nw,nw,s,nw,n,nw,nw,nw,sw,nw,n,nw,nw,se,s,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,sw,se,s,nw,nw,nw,sw,nw,nw,nw,n,nw,n,nw,nw,nw,nw,nw,nw,nw,ne,n,n,nw,n,n,nw,nw,se,nw,nw,s,s,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,n,nw,nw,nw,sw,nw,nw,nw,se,nw,nw,nw,nw,nw,nw,n,nw,n,n,nw,ne,se,s,nw,nw,nw,nw,nw,nw,sw,nw,sw,n,nw,ne,nw,n,nw,nw,nw,ne,nw,nw,nw,nw,nw,n,nw,nw,n,nw,nw,ne,nw,nw,nw,se,nw,n,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,n,nw,sw,nw,n,n,nw,nw,se,n,n,nw,nw,nw,ne,se,n,se,nw,nw,n,se,nw,nw,n,ne,n,nw,nw,n,nw,nw,n,n,nw,nw,sw,nw,nw,n,nw,n,nw,n,nw,nw,nw,sw,nw,nw,nw,nw,se,nw,nw,nw,nw,nw,n,nw,nw,n,s,n,ne,n,ne,se,nw,nw,n,nw,s,nw,nw,n,nw,nw,sw,nw,sw,nw,nw,nw,n,nw,nw,ne,nw,ne,se,sw,n,sw,n,nw,nw,nw,nw,ne,se,nw,nw,nw,nw,n,nw,nw,nw,nw,sw,nw,sw,n,nw,n,n,nw,n,nw,nw,n,nw,nw,nw,nw,nw,nw,sw,nw,nw,s,nw,nw,nw,n,n,nw,se,n,n,nw,nw,ne,sw,nw,n,n,nw,n,n,nw,nw,sw,n,nw,nw,nw,n,nw,nw,nw,nw,n,nw,n,nw,nw,nw,nw,nw,nw,n,n,n,nw,nw,nw,n,nw,nw,nw,nw,n,nw,nw,sw,s,nw,nw,nw,n,nw,n,n,nw,se,se,ne,nw,nw,s,nw,n,nw,nw,nw,n,s,nw,nw,s,nw,se,se,nw,nw,n,nw,n,nw,sw,nw,nw,s,nw,n,nw,se,ne,nw,nw,nw,s,n,nw,nw,nw,n,nw,ne,nw,n,s,nw,nw,nw,nw,s,n,n,nw,nw,nw,se,nw,n,nw,nw,n,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,se,ne,nw,nw,sw,n,nw,sw,nw,s,n,nw,ne,nw,sw,nw,nw,n,nw,nw,nw,n,nw,nw,se,n,n,sw,sw,nw,ne,nw,n,nw,ne,nw,nw,s,nw,nw,nw,n,sw,n,se,s,n,nw,nw,nw,nw,nw,nw,n,nw,n,s,n,n,nw,nw,nw,n,n,se,nw,n,ne,n,nw,n,nw,nw,nw,nw,n,n,n,ne,nw,nw,sw,n,n,nw,nw,nw,nw,ne,n,nw,nw,n,nw,se,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,nw,n,n,n,sw,nw,n,n,ne,se,sw,nw,n,nw,n,sw,nw,sw,n,n,n,nw,nw,nw,n,sw,nw,n,nw,nw,n,nw,n,n,ne,nw,n,n,n,nw,nw,nw,nw,n,nw,s,nw,n,nw,nw,n,ne,n,nw,n,n,s,nw,nw,n,s,ne,n,nw,ne,nw,nw,ne,n,nw,n,nw,nw,nw,nw,nw,ne,s,se,ne,nw,ne,nw,n,n,nw,n,n,nw,n,nw,nw,n,nw,s,ne,nw,n,s,n,nw,nw,nw,n,n,nw,n,n,nw,nw,ne,nw,nw,nw,n,se,n,nw,n,n,nw,se,nw,ne,nw,n,nw,nw,n,n,n,se,n,nw,ne,n,ne,n,ne,nw,n,n,se,nw,n,n,n,nw,n,ne,n,nw,n,n,se,nw,nw,n,n,s,n,ne,n,nw,sw,n,nw,n,s,n,n,nw,ne,ne,n,sw,n,nw,n,nw,nw,n,n,sw,nw,nw,nw,nw,sw,n,nw,n,nw,n,nw,n,nw,n,n,nw,n,nw,nw,nw,sw,nw,nw,nw,nw,n,n,n,se,s,ne,nw,nw,n,nw,s,n,nw,n,ne,nw,n,nw,n,ne,nw,ne,n,ne,se,n,nw,n,nw,nw,n,nw,s,s,n,nw,nw,n,n,n,nw,nw,n,nw,nw,nw,n,n,n,s,nw,nw,n,nw,nw,n,nw,n,sw,n,n,s,nw,nw,sw,nw,nw,nw,n,n,n,nw,nw,s,nw,nw,nw,nw,s,nw,n,ne,n,nw,n,n,nw,nw,s,n,nw,sw,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,n,nw,nw,sw,s,se,n,ne,nw,ne,s,nw,nw,se,n,nw,nw,n,n,nw,nw,n,nw,n,n,nw,nw,n,nw,nw,sw,sw,se,n,n,s,se,se,nw,se,n,n,se,ne,n,nw,nw,nw,n,n,n,nw,n,sw,n,nw,n,se,se,n,nw,n,sw,n,se,n,n,n,nw,n,nw,n,ne,n,n,nw,nw,n,n,se,n,n,n,n,n,nw,n,n,n,n,nw,nw,n,n,nw,nw,n,nw,s,n,n,n,nw,nw,se,se,n,n,se,n,nw,nw,ne,sw,ne,sw,n,n,sw,nw,nw,se,n,se,sw,sw,nw,n,nw,n,nw,nw,n,n,nw,se,n,nw,n,ne,n,n,nw,nw,n,nw,n,nw,se,n,n,n,n,s,s,n,n,s,nw,nw,nw,nw,nw,nw,nw,n,ne,se,n,nw,n,n,n,n,nw,nw,n,se,sw,n,s,n,n,n,nw,se,nw,n,n,n,ne,nw,n,n,nw,n,n,n,nw,n,n,n,n,n,n,n,n,se,n,sw,sw,nw,nw,nw,n,nw,nw,n,n,n,sw,s,n,nw,n,n,nw,n,nw,n,nw,n,nw,n,n,sw,n,n,n,n,n,n,nw,n,n,nw,nw,n,n,nw,n,n,nw,n,n,ne,n,n,n,n,n,se,n,sw,nw,nw,n,n,n,s,n,n,nw,n,n,n,n,n,n,n,se,n,n,nw,sw,nw,ne,n,nw,s,n,n,n,s,n,nw,nw,n,sw,n,n,sw,n,n,s,n,n,n,n,n,n,n,nw,n,n,n,n,n,n,n,nw,sw,sw,ne,n,s,nw,n,nw,sw,nw,ne,n,n,n,n,n,nw,se,n,nw,n,n,ne,sw,n,ne,n,n,n,n,n,n,n,nw,n,n,n,nw,n,nw,n,n,n,n,nw,n,n,nw,nw,n,n,n,se,se,n,n,s,sw,n,se,n,n,nw,n,n,n,s,nw,n,n,se,n,nw,se,sw,n,n,ne,n,n,n,n,n,sw,nw,n,nw,n,n,n,nw,n,nw,ne,n,n,n,n,n,n,n,se,nw,nw,n,n,n,n,sw,n,sw,s,sw,nw,nw,nw,n,n,sw,nw,n,n,n,n,n,n,n,n,s,nw,n,n,n,n,n,n,nw,nw,nw,s,n,n,n,nw,ne,n,n,ne,s,n,n,n,s,n,n,n,n,sw,sw,nw,n,n,n,n,nw,ne,n,n,s,se,n,n,n,nw,n,n,s,n,n,n,n,n,n,nw,n,n,n,n,sw,n,n,nw,s,se,n,nw,n,n,nw,n,nw,nw,n,ne,sw,nw,se,nw,n,n,n,n,n,sw,nw,n,n,n,n,n,n,nw,n,n,n,nw,n,nw,n,n,s,n,n,nw,sw,n,n,n,n,s,nw,nw,n,n,se,n,n,n,n,n,n,n,sw,nw,n,n,n,n,n,s,n,sw,n,sw,sw,se,sw,n,sw,n,n,nw,n,ne,n,s,n,n,n,n,n,n,n,s,n,n,s,n,n,se,n,n,n,n,n,se,nw,se,sw,n,s,sw,n,n,n,se,n,ne,n,n,n,n,n,n,nw,se,nw,n,n,n,n,sw,nw,sw,s,se,ne,s,sw,se,se,s,nw,se,se,se,se,n,se,ne,se,ne,ne,sw,ne,se,n,ne,ne,sw,n,ne,n,n,n,n,n,n,n,se,n,ne,n,n,n,n,nw,n,nw,n,nw,se,nw,nw,sw,nw,n,s,nw,se,sw,nw,nw,nw,nw,nw,nw,nw,nw,ne,nw,nw,sw,nw,ne,nw,se,sw,sw,sw,nw,sw,nw,sw,sw,se,sw,nw,se,sw,sw,sw,sw,sw,n,sw,sw,n,sw,sw,s,n,nw,sw,s,sw,sw,n,sw,s,se,sw,s,s,n,sw,s,ne,s,n,s,n,n,s,sw,sw,se,s,n,s,s,ne,s,s,sw,sw,s,s,s,s,sw,sw,s,nw,s,n,s,n,s,s,ne,s,s,s,se,ne,se,s,sw,s,nw,sw,s,s,se,se,nw,se,se,se,se,s,se,se,ne,s,s,se,se,se,se,se,se,se,nw,se,s,s,se,se,nw,nw,s,sw,ne,s,s,s,se,se,s,se,nw,se,ne,se,ne,n,s,ne,se,se,s,sw,ne,se,se,se,se,nw,se,sw,se,se,s,se,se,se,sw,s,se,se,se,se,se,nw,sw,se,se,n,se,se,se,se,se,se,se,ne,se,se,ne,ne,se,se,se,ne,se,se,n,ne,ne,se,se,sw,sw,n,se,se,ne,ne,ne,ne,ne,ne,se,ne,se,ne,se,ne,n,se,se,se,ne,se,ne,se,n,ne,ne,ne,ne,se,ne,sw,se,ne,ne,ne,ne,s,ne,se,ne,n,ne,se,ne,se,n,se,ne,ne,ne,s,se,n,ne,ne,se,ne,ne,s,ne,ne,ne,s,ne,nw,ne,sw,ne,ne,ne,ne,nw,ne,sw,ne,ne,ne,ne,s,n,n,ne,s,ne,ne,ne,ne,ne,ne,ne,n,n,n,n,s,n,ne,ne,ne,ne,nw,ne,se,ne,ne,n,n,ne,ne,ne,ne,n,ne,n,ne,sw,nw,se,ne,nw,ne,n,n,ne,s,s,n,nw,nw,nw,se,ne,ne,se,n,ne,n,n,n,n,ne,ne,n,se,n,sw,n,n,n,s,ne,ne,ne,n,ne,n,n,n,s,nw,s,n,n,n,n,n,nw,n,n,s,ne,n,n,n,ne,n,n,n,s,ne,n,s,s,n,ne,n,n,ne,ne,n,n,se,n,n,ne,n,ne,sw,nw,n,n,n,ne,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,s,ne,n,n,sw,n,n,n,n,nw,n,nw,sw,se,n,n,n,n,n,n,n,sw,n,nw,n,nw,nw,nw,n,n,n,ne,nw,n,n,nw,n,n,n,sw,n,s,nw,n,n,n,n,n,n,n,n,n,n,n,n,n,nw,n,nw,se,n,n,nw,s,se,n,sw,n,n,n,sw,n,n,n,nw,se,sw,n,n,nw,nw,n,nw,n,s,n,se,nw,nw,n,n,n,nw,n,nw,nw,se,n,nw,nw,nw,nw,n,n,nw,s,n,n,nw,n,n,nw,nw,n,nw,n,nw,nw,nw,n,nw,n,n,nw,s,nw,nw,ne,n,nw,n,sw,nw,n,sw,sw,sw,n,nw,n,nw,nw,n,s,nw,nw,nw,s,nw,ne,nw,n,nw,n,nw,nw,nw,n,nw,n,n,nw,nw,n,nw,n,nw,nw,n,n,nw,nw,s,nw,sw,nw,nw,s,nw,nw,nw,n,n,nw,nw,ne,nw,nw,nw,nw,nw,s,nw,nw,sw,nw,se,nw,s,nw,nw,nw,n,nw,nw,nw,se,nw,nw,nw,nw,sw,s,sw,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,se,nw,ne,nw,se,nw,sw,nw,ne,sw,se,nw,nw,sw,sw,nw,se,nw,se,se,nw,nw,nw,se,nw,nw,nw,nw,s,nw,sw,nw,se,nw,sw,nw,nw,nw,sw,nw,s,nw,se,nw,nw,nw,ne,nw,nw,nw,nw,ne,nw,se,nw,sw,sw,sw,n,ne,nw,nw,se,nw,s,sw,sw,nw,n,sw,s,sw,nw,nw,nw,nw,nw,sw,se,nw,sw,nw,nw,sw,s,nw,se,sw,sw,nw,nw,sw,nw,nw,sw,sw,n,n,ne,sw,sw,sw,nw,sw,sw,sw,sw,sw,sw,nw,nw,nw,sw,nw,n,sw,sw,se,sw,nw,nw,sw,nw,nw,sw,ne,nw,nw,sw,nw,s,ne,sw,ne,sw,sw,nw,sw,sw,sw,nw,nw,nw,sw,sw,sw,s,nw,nw,sw,se,se,nw,sw,nw,nw,sw,nw,sw,sw,nw,sw,nw,sw,sw,sw,nw,sw,nw,nw,sw,sw,ne,sw,nw,nw,nw,nw,sw,sw,sw,nw,sw,sw,s,sw,nw,nw,sw,sw,sw,sw,sw,sw,sw,sw,nw,nw,se,sw,sw,n,sw,sw,sw,sw,sw,n,sw,nw,sw,sw,sw,sw,s,sw,sw,n,sw,sw,sw,se,sw,sw,sw,nw,sw,nw,s,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,nw,ne,ne,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,n,n,sw,sw,sw,se,sw,sw,n,sw,sw,sw,sw,sw,s,sw,sw,sw,sw,sw,sw,sw,n,sw,s,s,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,se,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,n,sw,se,sw,sw,s,n,sw,nw,sw,sw,sw,sw,s,sw,s,sw,sw,sw,s,sw,sw,sw,sw,sw,sw,s,s,sw,sw,sw,s,n,s,ne,sw,s,s,sw,s,sw,s,sw,sw,sw,s,sw,sw,se,nw,sw,sw,sw,s,sw,sw,sw,s,sw,sw,s,sw,s,s,nw,s,s,sw,s,s,sw,sw,sw,sw,s,nw,s,sw,sw,s,sw,s,sw,n,nw,nw,s,s,ne,sw,se,s,sw,s,sw,sw,n,sw,nw,sw,sw,sw,sw,sw,n,sw,se,sw,sw,se,sw,se,sw,sw,se,sw,sw,n,sw,s,sw,sw,nw,s,se,n,ne,sw,sw,sw,s,se,nw,sw,sw,sw,n,se,sw,s,s,sw,s,s,sw,sw,s,s,ne,sw,nw,s,sw,se,nw,s,n,sw,sw,sw,sw,s,s,s,s,s,s,s,s,s,sw,sw,se,nw,s,sw,sw,ne,se,s,n,sw,sw,nw,s,s,sw,nw,s,s,s,sw,sw,s,sw,sw,s,s,sw,sw,s,s,s,sw,n,nw,s,sw,s,sw,nw,sw,s,se,s,s,s,s,sw,s,s,sw,sw,s,s,s,sw,se,s,nw,s,ne,s,s,s,sw,s,s,nw,sw,s,s,s,n,s,sw,s,s,s,sw,s,s,n,s,s,s,s,s,s,se,sw,s,s,s,s,se,s,s,nw,s,s,s,n,s,s,s,sw,sw,n,s,s,s,s,se,s,se,s,s,s,s,s,s,s,se,se,sw,se,ne,s,s,nw,s,s,s,sw,se,s,s,sw,s,s,s,ne,s,n,sw,s,s,s,n,s,ne,s,se,ne,ne,s,s,s,s,s,sw,s,s,s,s,nw,sw,s,s,s,s,s,s,s,n,s,s,se,s,s,s,s,s,s,s,s,s,nw,se,s,s,se,ne,s,s,s,s,se,s,s,s,s,nw,ne,s,se,s,s,s,s,s,s,s,s,s,se,s,s,s,s,s,se,s,sw,s,s,s,se,s,s,s,sw,se,se,s,sw,s,s,ne,s,s,s,s,s,nw,s,nw,s,nw,n,s,s,s,ne,ne,s,s,ne,nw,s,s,s,nw,se,se,s,s,s,s,s,se,s,s,s,s,s,s,nw,s,se,nw,s,ne,s,s,s,s,s,s,s,s,ne,s,ne,s,s,s,s,se,se,se,se,s,s,ne,s,s,s,se,s,s,s,s,ne,se,se,se,ne,ne,se,se,s,se,s,nw,se,s,se,nw,n,ne,s,se,se,se,se,s,se,s,s,s,s,nw,se,s,s,nw,s,s,s,s,s,s,s,s,ne,s,s,se,nw,se,s,s,s,se,sw,n,s,se,se,se,se,s,s,n,s,s,se,s,s,ne,se,se,se,s,se,s,se,s,se,n,s,sw,se,s,se,s,s,s,se,s,nw,ne,s,s,se,s,s,s,se,se,s,sw,s,s,s,s,s,se,ne,se,nw,se,se,se,se,nw,se,se,se,s,sw,ne,s,se,s,s,s,s,s,se,s,n,s,s,n,se,sw,se,se,n,se,se,s,se,se,ne,se,s,s,s,s,se,n,se,s,s,s,n,s,se,s,s,se,se,s,s,s,s,s,se,se,n,s,s,s,s,s,se,se,se,s,se,ne,s,se,se,s,se,se,n,se,s,se,s,se,se,se,se,s,s,ne,s,se,se,s,s,s,se,se,s,ne,sw,n,s,s,sw,se,s,sw,s,se,se,n,n,s,s,s,s,s,se,n,s,se,se,se,s,s,s,se,s,sw,s,se,se,s,nw,sw,se,se,se,se,ne,sw,n,se,se,se,nw,s,se,se,se,nw,se,se,se,se,ne,sw,nw,ne,se,s,s,se,sw,ne,se,sw,se,n,se,ne,s,se,se,ne,s,s,se,se,se,se,se,s,se,se,se,se,se,se,se,s,sw,se,nw,se,s,s,ne,se,se,se,se,sw,se,se,n,se,sw,se,s,se,se,se,n,se,se,se,se,se,se,sw,n,s,se,se,se,se,se,se,n,se,se,se,s,se,s,se,se,se,s,se,s,nw,sw,s,s,se,se,se,se,se,s,se,s,se,se,se,se,se,se,se,se,se,s,se,se,se,se,se,se,se,se,se,nw,se,se,se,se,se,n,se,n,se,s,se,se,ne,s,se,s,s,s,se,se,se,se,ne,se,se,ne,se,se,se,sw,s,se,se,se,se,se,se,n,se,se,se,se,se,se,nw,se,se,se,se,n,se,se,s,se,ne,se,se,se,se,se,n,se,se,sw,ne,se,se,n,se,se,nw,se,se,s,se,ne,n,se,se,s,se,se,sw,s,sw,se,se,ne,se,se,se,se,nw,se,ne,se,se,se,s,se,nw,se,se,se,se,se,se,ne,se,se,se,se,se,se,s,se,ne,se,se,s,se,se,se,se,se,se,se,se,se,se,nw,se,se,se,se,ne,n,ne,se,sw,se,ne,se,se,se,se,sw,se,se,se,se,se,sw,se,sw,nw,se,se,se,se,ne,ne,se,ne,s,se,se,ne,se,se,se,se,n,ne,se,se,se,s,se,nw,se,se,se,n,se,se,ne,se,s,se,n,se,se,ne,se,se,se,se,se,se,ne,s,se,ne,ne,se,se,nw,ne,se,se,se,s,se,ne,se,ne,se,se,nw,se,ne,se,se,se,se,se,ne,se,se,se,se,se,se,ne,se,nw,se,nw,ne,sw,se,se,se,se,se,se,se,ne,se,se,n,se,se,se,se,se,ne,se,se,nw,se,ne,se,n,ne,se,se,s,se,se,sw,ne,se,se,se,se,se,nw,se,s,se,se,se,se,se,se,n,ne,sw,ne,ne,n,se,se,se,nw,ne,ne,ne,se,ne,n,se,se,se,se,se,n,se,ne,se,s,se,se,ne,se,se,se,ne,ne,se,se,ne,se,se,ne,nw,nw,se,ne,se,se,se,ne,se,ne,se,se,sw,ne,ne,nw,se,se,ne,se,sw,ne,se,ne,ne,n,se,ne,nw,ne,s,ne,se,ne,se,se,se,ne,ne,se,se,ne,ne,se,ne,se,s,sw,nw,n,ne,se,n,ne,se,se,se,nw,se,se,se,n,se,se,se,ne,ne,se,ne,se,ne,ne,ne,se,se,ne,se,ne,se,se,se,ne,s,se,ne,ne,se,se,ne,ne,ne,ne,se,ne,se,sw,se,ne,ne,nw,se,ne,ne,ne,ne,se,sw,se,s,se,nw,se,ne,se,ne,se,ne,ne,se,ne,se,se,se,ne,ne,se,ne,se,se,se,se,ne,se,sw,se,se,se,ne,se,nw,se,se,se,n,ne,ne,ne,s,sw,ne,nw,ne,s,ne,ne,se,se,sw,se,se,se,se,se,nw,se,ne,ne,nw,ne,se,ne,n,nw,ne,ne,se,se,ne,ne,sw,se,se,ne,sw,se,s,ne,se,sw,se,ne,se,ne,ne,ne,sw,s,ne,se,ne,n,sw,ne,se,se,se,ne,ne,nw,sw,se,ne,ne,ne,ne,ne,se,ne,se,ne,se,se,ne,sw,ne,ne,ne,ne,se,ne,se,ne,ne,ne,ne,ne,s,ne,ne,se,se,ne,se,ne,ne,n,s,se,ne,ne,se,ne,sw,nw,ne,n,se,nw,se,ne,ne,sw,se,sw,ne,ne,ne,ne,ne,se,se,ne,ne,ne,n,ne,se,se,ne,se,n,ne,ne,se,se,ne,n,se,ne,se,se,se,nw,ne,se,ne,ne,nw,nw,ne,ne,ne,ne,ne,se,n,ne,ne,s,se,s,ne,sw,ne,ne,ne,se,se,nw,n,ne,se,sw,ne,ne,ne,sw,ne,nw,s,s,ne,s,ne,ne,ne,ne,nw,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,sw,ne,nw,ne,ne,se,ne,ne,ne,ne,ne,sw,ne,ne,ne,ne,ne,ne,s,se,ne,se,ne,ne,ne,nw,sw,ne,n,se,se,ne,se,ne,se,n,ne,se,ne,se,s,ne,ne,ne,nw,ne,ne,ne,se,se,se,ne,ne,nw,ne,ne,se,sw,se,ne,ne,se,ne,se,se,ne,se,ne,sw,ne,ne,se,se,ne,se,s,nw,ne,ne,nw,ne,ne,ne,se,ne,se,ne,se,ne,ne,ne,ne,n,ne,ne,s,ne,ne,ne,sw,nw,s,ne,ne,ne,ne,n,ne,nw,ne,se,ne,se,ne,ne,n,se,ne,ne,se,ne,ne,ne,ne,ne,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,sw,ne,nw,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,se,ne,ne,sw,ne,nw,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,s,ne,nw,ne,ne,ne,ne,sw,ne,s,s,ne,ne,ne,ne,ne,ne,sw,ne,ne,ne,ne,ne,ne,ne,nw'''

class path:

    def add_step(self, step):
        self.steps.append(step)
        self.original_steps.append(step)

    def __init__(self, steps):
        self.steps = steps.split(',') if len(steps) > 0 else []
        self.original_steps = steps.split(',') if len(steps) > 0 else []

    def absolute_length(self):
        self.clean();
        return len(self.steps)

    def clean(self):
        self.remove_negated_steps();
        self.consolidate();

    def remove_negated_steps(self):
        # Steps N and S negate each other
        self.remove_pair('n', 's')
        # As do NE and SW
        self.remove_pair('ne', 'sw')
        #And NW and SE
        self.remove_pair('nw', 'se')

    def consolidate(self):
        # One step NE and one NW can be consolidated to one step north
        self.consolidate_pair('ne', 'nw', 'n')
        # One step SE and one SW can be consolidated to one step south
        self.consolidate_pair('se', 'sw', 's')
        # One step NE and one S can be consolidated to one step SE
        self.consolidate_pair('ne', 's', 'se')
        # One step NW and one S can be consolidated to one step SW
        self.consolidate_pair('nw', 's', 'sw')
        # One step SE and one N can be consolidated to one step NE
        self.consolidate_pair('se', 'n', 'ne')
        # One step SW and one N can be consolidated to one step NW
        self.consolidate_pair('sw', 'n', 'nw')

    def remove_pair(self, a, b):
        for i in range(min(self.steps.count(a), self.steps.count(b))):
            self.steps.remove(a)
            self.steps.remove(b)

    def consolidate_pair(self, from_a, from_b, to):
        # remove a,b pairs first
        for i in range(min(self.steps.count(from_a), self.steps.count(from_b))):
            self.steps.remove(from_a)
            self.steps.remove(from_b)
            self.steps.append(to)


def puzzle1(puzzle_input):
    p = path(puzzle_input)
    return p.absolute_length()

assert puzzle1('ne,ne,ne') == 3, "ne,ne,ne is 3 steps away."
assert puzzle1('ne,ne,sw,sw') == 0, "ne,ne,sw,sw is 0 steps away (back where you started)."
assert puzzle1('ne,ne,s,s') == 2, "ne,ne,s,s is 2 steps away (se,se)."
assert puzzle1('se,sw,se,sw,sw') == 3, "se,sw,se,sw,sw is 3 steps away (s,s,sw)."

print('The result of puzzle 1 is: {}'.format(puzzle1(puzzle_input)))

def puzzle2(puzzle_input):
    steps = puzzle_input.split(',')
    complete_path = path('')
    max_distance = 0
    for step in steps:
        complete_path.add_step(step)
        max_distance = max(max_distance, complete_path.absolute_length())
    return max_distance

print('The result of puzzle 2 is: {}'.format(puzzle2(puzzle_input)))
