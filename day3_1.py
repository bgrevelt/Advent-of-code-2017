'''
ou come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 368078.

'''
from itertools import islice

# this solution is kind of dodgy, since there is probably a mathemetical way to solve the puzzle that is much faster.as
# On the other hand this is a straightforward solution that runs in less than a seconds, so let's be lazy as long as we can.
def index_generator():
    current_ring_index = 1
    coord = (0,0)

    state = 'right'
    yield coord
    while(True):
        if(coord[0] == current_ring_index and coord[1] == -current_ring_index):
            current_ring_index = current_ring_index + 1

        if state == 'right':
            coord = (coord[0] +1, coord[1])
            if(coord[0] == current_ring_index and coord[1] == -current_ring_index):
                current_ring_index = current_ring_index + 1

            if coord[0] == current_ring_index:
                state = 'up'
        elif state == 'up':
            coord = (coord[0], coord[1]+1)
            if coord[1] == current_ring_index:
                state = 'left'
        elif state == 'left':
            coord = (coord[0] -1, coord[1])
            if coord[0] == (-1 * current_ring_index):
                state = 'down'
        elif state == 'down':
            coord = (coord[0], coord[1] -1)
            if coord[1] == (-1 * current_ring_index):
                state = 'right'

        yield coord;


def get_coord_of_value(value):
    return next(islice(index_generator(), value-1, None))

def get_minimum_distance_to_value(value):
    x, y = get_coord_of_value(value)
    return abs(x) + abs(y)

assert get_minimum_distance_to_value(1) == 0,  "Data from square 1 is carried 0 steps, since it's at the access port."
assert get_minimum_distance_to_value(12) == 3, "Data from square 12 is carried 3 steps, such as: down, left, left."
assert get_minimum_distance_to_value(23) == 2, "Data from square 23 is carried only 2 steps: up twice."
assert get_minimum_distance_to_value(1024) == 31, "Data from square 1024 must be carried 31 steps."

# Part 1
print('Answer part one: {}'.format(get_minimum_distance_to_value(368078)))

def get_adjacent_squares(coord):
    offsets = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1) ]
    return [(coord[0] + a , coord[1] + b) for a,b, in offsets]

def get_first_value_larger_then_input(input):
    gen = index_generator()
    found = False

    # set the first cell to one manually an make sure to skip it in the generator
    current_memory = {(0,0) : 1}
    next(gen)

    while(True):
        next_coord = next(gen)
        adjacent_squares = get_adjacent_squares(next_coord)
        coord_value = sum([current_memory[square] for square in adjacent_squares if square in current_memory])
        current_memory[next_coord] = coord_value
        if coord_value > input:
            return coord_value

# Part 2
print('Answer part two: {}'.format(get_first_value_larger_then_input(368078)))
