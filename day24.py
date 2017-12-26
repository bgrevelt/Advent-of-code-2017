'''
--- Day 24: Electromagnetic Moat ---

The CPU itself is a large, black building surrounded by a bottomless pit. Enormous metal tubes extend outward from the side of the building at regular intervals and descend down into the void. There's no way to cross, but you need to get inside.

No way, of course, other than building a bridge out of the magnetic components strewn about nearby.

Each component has two ports, one on each end. The ports come in all different types, and only matching types can be connected. You take an inventory of the components by their port types (your puzzle input). Each port is identified by the number of pins it uses; more pins mean a stronger connection for your bridge. A 3/7 component, for example, has a type-3 port on one side, and a type-7 port on the other.

Your side of the pit is metallic; a perfect surface to connect a magnetic, zero-pin port. Because of this, the first port you use must be of type 0. It doesn't matter what type of port you end with; your goal is just to make the bridge as strong as possible.

The strength of a bridge is the sum of the port types in each component. For example, if your bridge is made of components 0/3, 3/7, and 7/4, your bridge has a strength of 0+3 + 3+7 + 7+4 = 24.

For example, suppose you had the following components:

0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
With them, you could make the following valid bridges:

0/1
0/1--10/1
0/1--10/1--9/10
0/2
0/2--2/3
0/2--2/3--3/4
0/2--2/3--3/5
0/2--2/2
0/2--2/2--2/3
0/2--2/2--2/3--3/4
0/2--2/2--2/3--3/5
(Note how, as shown by 10/1, order of ports within a component doesn't matter. However, you may only use each port on a component once.)

Of these bridges, the strongest one is 0/1--10/1--9/10; it has a strength of 0+1 + 1+10 + 10+9 = 31.

What is the strength of the strongest bridge you can make with the components you have available?
'''



puzzle_input = '''50/41
19/43
17/50
32/32
22/44
9/39
49/49
50/39
49/10
37/28
33/44
14/14
14/40
8/40
10/25
38/26
23/6
4/16
49/25
6/39
0/50
19/36
37/37
42/26
17/0
24/4
0/36
6/9
41/3
13/3
49/21
19/34
16/46
22/33
11/6
22/26
16/40
27/21
31/46
13/2
24/7
37/45
49/2
32/11
3/10
32/49
36/21
47/47
43/43
27/19
14/22
13/43
29/0
33/36
2/6'''

test_input = '''0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10'''


components = [tuple([int(port) for port in component.split('/')]) for component in test_input.splitlines()]

def get_tails(last, components):
    if not components:
        return [[]]

    tails = [[]]

    nexts = [component for component in components if last[1] in component]
    for next in nexts:
        index = components.index(next)
        if next[1] == last[1]:
            next = (next[1], next[0])
        tails.extend([[next] + b for b in get_tails(next, components[:index] + components[index+1:])])

    return tails

def strength(bridge):
    return sum([sum(component) for component in bridge])

def puzzle_1(puzzle_input):
    components = [tuple([int(port) for port in component.split('/')]) for component in puzzle_input.splitlines()]
    bridges = get_tails((0,0), components)
    return max(strength(bridge) for bridge in bridges)

assert puzzle_1(test_input) == 31, "Of these bridges, the strongest one is 0/1--10/1--9/10; it has a strength of 0+1 + 1+10 + 10+9 = 31"
print('The result for puzzle 1 is {}'.format(puzzle_1(puzzle_input)))

def puzzle_2(puzzle_input):
    components = [tuple([int(port) for port in component.split('/')]) for component in puzzle_input.splitlines()]
    bridges = get_tails((0,0), components)
    longest = max([len(bridge) for bridge in bridges])
    longest_bridges = [bridge for bridge in bridges if len(bridge) == longest]
    return max(strength(bridge) for bridge in longest_bridges)

print('The result for puzzle 2 is {}'.format(puzzle_2(puzzle_input)))