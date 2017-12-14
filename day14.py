from day10 import puzzle2 as knot_hash

puzzle_input = 'nbysizxe'

def char_to_bits(char):
    n = int(char,16)
    return [True if n & (2**bit) else False for bit in range(3,-1,-1)]

def knot_hash_string_to_bits(string):
    bits = []
    for c in string:
        bits += char_to_bits(c)
    return bits

def get_grid(puzzle_input):
    return [knot_hash_string_to_bits(knot_hash('{}-{}'.format(puzzle_input, row))) for row in range(128)]

def puzzle1(puzzle_input):
    return sum([row.count(True) for row in get_grid(puzzle_input)])


print('The result of puzzle 1 is: {}'.format(puzzle1(puzzle_input)))

def print_grid(grid):
    for row in grid:
        print(''.join(row))

# Mark all elements of a group in the grid starting at an arbitrary element in the group
def find_group(x,y,grid, group_number):
    grid[y][x] = '{0:2}'.format(group_number)
    coords = ((x_,y_) for x_ in [x-1,x+1] for y_ in [y-1,y+1] if x_ >= 0 and x_ < len(grid[y]) and y_ >= 0 and y_ < len(grid))
    for coord in coords:
        if grid[coord[1]][coord[0]] == True:
            find_group(coord[0], coord[1], grid, group_number)

def puzzle2(puzzle_input):
    groups_found = 0
    grid = get_grid(puzzle_input)
    # grid not contains a grid of booleans. Any value that is True is part of an undiscovered group.
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == True:
                groups_found += 1
                # Find group will mark all cells that are part of the group with the number of the group
                find_group(x,y,grid, groups_found)

    return groups_found

print('The solution for puzzle2 is: {}'.format(puzzle2(puzzle_input)))

