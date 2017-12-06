'''
-- Day 6: Memory Reallocation ---

A debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that has been seen before.

For example, imagine a scenario with only four memory banks:

    The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks, so it is chosen for redistribution.
    Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on, the 7 blocks are spread out over the memory banks. The fourth, first, and second banks get two blocks each, and the third bank gets one back. The final result looks like this: 2 4 1 2.
    Next, the second bank is chosen because it contains the most blocks (four). Because there are four memory banks, each gets one block. The result is: 3 1 2 3.
    Now, there is a tie between the first and fourth memory banks, both of which have three blocks. The first bank wins the tie, and its three blocks are distributed evenly over the other three banks, leaving it with none: 0 2 3 4.
    The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: 1 3 4 1.
    The third bank is chosen, and the same thing happens: 2 4 1 2.

At this point, we've reached a state we've seen before: 2 4 1 2 was already seen. The infinite loop is detected after the fifth block redistribution cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?
'''
import copy
from operator import add

input = '11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11'

def rotate_right(l,n):
    return l[-n:] + l[:-n]

def split_number(n, splits):
    return [n // splits if i >= n % splits else n // splits + 1 for i in range(splits)]

def day6(input):
    previous_redistributions = [copy.deepcopy(input)]
    while(True):
        largest_value = max(input)
        largest_block_index = input.index(largest_value)
        input[largest_block_index] = 0
        redistributed_blocks = rotate_right(split_number(largest_value, len(input)), largest_block_index+1)
        input = list(map(add, input, redistributed_blocks))
        if input in previous_redistributions:
            return (len(previous_redistributions), previous_redistributions.index(input))
        previous_redistributions.append(copy.deepcopy(input))

def day6_1(input):
    return day6(input)[0]

def day6_2(input):
    r = day6(input)
    return r[0] - r[1]

assert day6_1([0,2,7,0]) == 5, "Puzzle 1 sanity check failed"
assert day6_2([0,2,7,0]) == 4, "Puzzle 2 sanity check failed"


print("The result for puzzle one is {}".format(day6_1([int(n) for n in input.split()])))
print("The result for puzzle two is {}".format(day6_2([int(n) for n in input.split()])))
