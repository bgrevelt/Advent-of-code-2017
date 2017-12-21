'''
--- Day 21: Fractal Art ---

You find a program trying to generate some art. It uses a strange process that involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either on (#) or off (.). The program always begins with this pattern:

.#.
..#
###

Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have a size of 3.

Then, the program repeats the following process:

    If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
    Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.

Because each square of pixels is replaced by a larger one, the image gains pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules. The artist explains that sometimes, one must rotate or flip the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:

../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.

When searching for a rule to use, rotate and flip the pattern as necessary. For example, all of the following patterns match the same rule:

.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.

Suppose the book contained the following two rules:

../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#

As before, the program begins with this pattern:

.#.
..#
###

The size of the grid (3) is not divisible by 2, but it is divisible by 3. It divides evenly into a single square; the square matches the second rule, which produces:

#..#
....
....
#..#

The size of this enhanced grid (4) is evenly divisible by 2, so that rule is used. It divides evenly into four squares:

#.|.#
..|..
--+--
..|..
#.|.#

Each of these squares matches the same rule (../.# => ##./#../...), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:

##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...

Finally, the squares are joined into a new grid:

##.##.
#..#..
......
##.##.
#..#..
......

Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?

Your puzzle answer was 120.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

How many pixels stay on after 18 iterations?

'''
test_input = '''../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#'''

puzzle_input = '''../.. => ..#/.#./...
#./.. => .../#../.##
##/.. => .##/###/##.
.#/#. => #.#/..#/#.#
##/#. => .../.##/...
##/## => ##./..#/..#
.../.../... => ##../..../##../.###
#../.../... => ...#/.#.#/.#../.#.#
.#./.../... => #.#./...#/#.#./.##.
##./.../... => ..#./#.##/#.../.###
#.#/.../... => ##../##.#/..#./#.##
###/.../... => ..../.#.#/.###/#..#
.#./#../... => #..#/#.../.##./....
##./#../... => #.##/..##/####/.###
..#/#../... => ..#./#.##/####/####
#.#/#../... => .##./#.##/#.#./##.#
.##/#../... => #.##/####/.###/...#
###/#../... => ..../#.#./##.#/..##
.../.#./... => .###/.##./##../.##.
#../.#./... => ..../#.##/...#/#.#.
.#./.#./... => ...#/####/.##./#...
##./.#./... => .###/#.##/###./....
#.#/.#./... => #.##/###./..../..#.
###/.#./... => .#../#.#./#.##/#.##
.#./##./... => .###/##../..##/#..#
##./##./... => ..#./#.#./.#.#/##.#
..#/##./... => .#../####/...#/..##
#.#/##./... => ..../##.#/.##./....
.##/##./... => .#.#/.#.#/.##./####
###/##./... => ##.#/..../..../....
.../#.#/... => ..##/##../##.#/###.
#../#.#/... => ####/#.##/#.../###.
.#./#.#/... => ..../#..#/..##/.#..
##./#.#/... => #.../..##/##../..#.
#.#/#.#/... => ...#/#.#./#.#./#...
###/#.#/... => ###./###./##.#/###.
.../###/... => ..#./###./##.#/####
#../###/... => ##.#/..#./##../..##
.#./###/... => #.../#.##/##../....
##./###/... => ..##/.#.#/#..#/#.##
#.#/###/... => #.##/..#./.#../..##
###/###/... => ..#./#..#/####/.##.
..#/.../#.. => ##.#/#.##/...#/###.
#.#/.../#.. => #..#/..#./##../###.
.##/.../#.. => ..#./.#../###./#.#.
###/.../#.. => ...#/...#/.#.#/.##.
.##/#../#.. => ##../#.#./#..#/##..
###/#../#.. => ##../.#.#/##../#..#
..#/.#./#.. => ##.#/##.#/...#/.#..
#.#/.#./#.. => .###/.#.#/###./....
.##/.#./#.. => #..#/###./####/..#.
###/.#./#.. => ..#./.###/.###/...#
.##/##./#.. => #.##/..##/...#/.###
###/##./#.. => ####/##.#/#.##/#..#
#../..#/#.. => ..../.##./#.##/#...
.#./..#/#.. => #..#/##../...#/#...
##./..#/#.. => ..#./.###/..##/.#.#
#.#/..#/#.. => .##./..##/..#./#..#
.##/..#/#.. => ####/.#.#/#.../.#.#
###/..#/#.. => ..../..##/#.##/###.
#../#.#/#.. => #.##/.#.#/.#../.##.
.#./#.#/#.. => ..##/###./.###/###.
##./#.#/#.. => ##.#/##.#/#.#./##..
..#/#.#/#.. => ###./###./.#.#/.#..
#.#/#.#/#.. => ##../..#./##../....
.##/#.#/#.. => .###/#.#./##.#/##..
###/#.#/#.. => ##.#/#.#./.#.#/#...
#../.##/#.. => .#.#/...#/.#.#/..#.
.#./.##/#.. => ###./##../##.#/....
##./.##/#.. => ..##/###./#.#./#.#.
#.#/.##/#.. => ##.#/..##/#..#/####
.##/.##/#.. => ..../####/..#./##..
###/.##/#.. => .###/#..#/..../.#..
#../###/#.. => #..#/.#../.#.#/#...
.#./###/#.. => .#../..../.##./.###
##./###/#.. => ##.#/.#../.#.#/#..#
..#/###/#.. => #.##/##../..##/#...
#.#/###/#.. => ####/..##/.#../##.#
.##/###/#.. => .###/#..#/.###/#.##
###/###/#.. => ..##/.##./##../#..#
.#./#.#/.#. => ..##/.##./.##./.###
##./#.#/.#. => ..##/...#/.##./####
#.#/#.#/.#. => .###/.###/#.#./.#..
###/#.#/.#. => ##.#/###./##.#/####
.#./###/.#. => ...#/..#./.#.#/.#..
##./###/.#. => ###./##.#/#.../#.#.
#.#/###/.#. => .##./#.#./...#/..#.
###/###/.#. => .#.#/.#../..##/####
#.#/..#/##. => .##./...#/#..#/.###
###/..#/##. => #.##/.#.#/...#/..##
.##/#.#/##. => ###./.###/...#/....
###/#.#/##. => .##./.##./#.#./#...
#.#/.##/##. => #.#./.##./.#.#/.###
###/.##/##. => ..../####/.#.#/#.##
.##/###/##. => .##./.###/###./.#..
###/###/##. => #.../###./.##./##.#
#.#/.../#.# => #.#./..../#.##/###.
###/.../#.# => .#../.#.#/#.../.###
###/#../#.# => ###./#..#/####/##..
#.#/.#./#.# => ###./##.#/..../.#..
###/.#./#.# => ####/.#.#/.#../..##
###/##./#.# => #.#./####/..##/#...
#.#/#.#/#.# => #.#./#.#./#.../#.##
###/#.#/#.# => #.##/.#../..#./.##.
#.#/###/#.# => .###/..##/####/#..#
###/###/#.# => #.../..#./..#./#.##
###/#.#/### => .#.#/.###/#.##/..##
###/###/### => #.#./...#/.#../.#.#'''

import numpy as np
import math

def break_up_grid(grid, particle_size):
    number_of_particles = len(grid) // particle_size
    return [grid[ix*particle_size : (ix+1)*particle_size, iy*particle_size : (iy+1)*particle_size,] for ix in range(number_of_particles) for iy in range(number_of_particles)]

def construct_grid(particles):
    particles_per_axis = int(math.sqrt(len(particles)))
    assert particles_per_axis ** 2 == len(particles), "All grids in this puzzle are square"
    grid = None
    for ix in range(particles_per_axis):
        column = None
        for iy in range(particles_per_axis):
            if iy == 0:
                column = particles[iy * particles_per_axis + ix]
            else:
                column = np.vstack((column, particles[iy * particles_per_axis + ix]))
        if ix == 0:
            grid = column
        else:
            grid = np.hstack((grid, column))
    return grid

def get_transformations(grid):
    rotated = [grid, np.rot90(grid,1), np.rot90(grid,2), np.rot90(grid,3)]
    return rotated + [np.flip(t,axis) for t in rotated for axis in [0,1]]

def get_enhancement_rules(puzzle_input):
    enhancements = {}
    for line in puzzle_input.splitlines():
        enhancement_from, enhancement_to = [np.array([[c for c in row] for row in matrix.split('/')]) for matrix in line.split(' => ')]
        assert len(enhancement_from) == 2 or len(enhancement_from) == 3
        enhancements[tuple(map(tuple,enhancement_from))] = enhancement_to
    return enhancements

def enhance(particle, rules):
    for transformed_particle in get_transformations(particle):
        particle_as_tuple = tuple(map(tuple,transformed_particle))
        if particle_as_tuple in rules:
            return rules[particle_as_tuple]
    assert False, "I could not find a transformation rule for this particle"

def puzzle(puzzle_input, nr_of_iterations):
    grid = np.array([c for c in '.#...####']).reshape([3,3])
    enhancement_rules = get_enhancement_rules(puzzle_input)
    for iteration in range(nr_of_iterations):
        assert len(grid) % 2 == 0 or len(grid) % 3 == 0

        particles = break_up_grid(grid, 2 if len(grid) % 2 == 0 else 3)
        grid = construct_grid([enhance(particle, enhancement_rules) for particle in particles])

    return sum([row.count('#') for row in grid.tolist()])

assert puzzle(test_input, 2) == 12, "Thus, after 2 iterations, the grid contains 12 pixels that are on."
print('The solution for puzzle 1 is {}'.format(puzzle(puzzle_input,5)))
print('The solution for puzzle 2 is {}'.format(puzzle(puzzle_input,18)))
