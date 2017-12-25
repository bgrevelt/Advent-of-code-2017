'''
--- Day 23: Coprocessor Conflagration ---

You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

set X Y sets register X to the value of Y.
sub X Y decreases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul instruction invoked?

Your puzzle answer was 3025.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Now, it's time to fix the problem.

The debug mode switch is wired directly to register a. You flip the switch, which makes register a now start at 1 when the program is executed.

Immediately, the coprocessor begins to overheat. Whoever wrote this program obviously didn't choose a very efficient implementation. You'll need to optimize the program if it has any hope of completing before Santa needs that printer working.

The coprocessor's ultimate goal is to determine the final value left in register h once the program completes. Technically, if it had that... it wouldn't even need to run the program.

After setting register a to 1, if the program were to run to completion, what value would be left in register h?
'''
from collections import defaultdict
from math import sqrt

def get_value(operand, registers):
    try:
        # this is a number
        return int(operand)
    except:
        return registers[operand]

def set(operands, registers):
    assert len(operands) == 2
    assert operands[0].isalpha()
    registers[operands[0]] = get_value(operands[1], registers)

def sub(operands, registers):
    assert len(operands) == 2
    assert operands[0].isalpha()
    registers[operands[0]] -= get_value(operands[1], registers)

def multiply(operands, registers):
    assert len(operands) == 2
    assert operands[0].isalpha()
    registers[operands[0]] *= get_value(operands[1], registers)

def jump(operands, registers):
    assert len(operands) == 2
    if get_value(operands[0], registers) != 0:
        return get_value(operands[1], registers)

def execute_instruction(instruction, registers):
    operation = instruction.split()[0]
    operands = instruction.split()[1:]
    instruction_map = {'set' : set, 'sub' : sub, 'mul' : multiply, 'jnz' : jump}
    assert operation in instruction_map
    return instruction_map[operation](operands, registers)

puzzle_input = '''set b 57
set c b
jnz a 2
jnz 1 5 
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d         
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''


def puzzle_1(puzzle_input):
    instructions = puzzle_input.splitlines();
    registers = defaultdict(int)
    number_of_multiplications = 0
    instruction_pointer = 0;
    while instruction_pointer < len(instructions):
        if 'mul' in instructions[instruction_pointer]:
            number_of_multiplications += 1
        jump = execute_instruction(instructions[instruction_pointer], registers)
        if jump:
            instruction_pointer += jump
        else:
            instruction_pointer += 1
    return number_of_multiplications

print('The solution to puzzle 1 is: {}'.format(puzzle_1(puzzle_input)))

def is_prime(x):
    prime = False
    if x > 1:
        prime = True
        k = 2
        n = sqrt(x) # to find square of x only once (or n = x ** 0.5 to get rid of math module)
        while k <= n and prime is True:
            if x % k == 0:
                prime = False
            k += 1
    return prime

def puzzle_2(puzzle_input):
    ''' Some manual analysis here:
    Instructions 0-7 are setup instructions, executed only once:
    set b 57
    set c b
    jnz a 2
    jnz 1 5
    mul b 100
    sub b -100000
    set c b
    sub c -17000

    which comes down to:
    b = 105700
    c = 122700

    Then we get to a couple of loops
    Interesting thing to notice is that g is used as the working register.

    -- LOOP3
    set f 1
    set d 2
        -- LOOP 2
        set e 2
            -- LOOP !
            set g d
            mul g e
            sub g b
            jnz g 2
            set f 0
            sub e -1
            set g e
            sub g b
            jnz g -8
        sub d -1
        set g d
        sub g b
        jnz g -13
    jnz f 2
    sub h -1
    set g b
    sub g c
    jnz g 2
    jnz 1 3
    sub b -17
    jnz 1 -23

    Looking at the loops one at at time:

    Loop 1:
    set g d
    mul g e
    sub g b
    jnz g 2     if d * e - b == 0: f = 0
    set f 0
    sub e -1    e += 1
    set g e
    sub g b
    jnz g -8    if e - b != 0 goto start of loop

    Translates to
    while e != b:
        if d * e  == b:
            f = 0
        e -= 1

    loop 2:
    set e 2
    --loop1
    sub d -1    d += 1
    set g d     g = d
    sub g b     g -= b
    jnz g -13   if d - b != 0: go back

    translates to
    while d != b:
        loop1
        d += 1

    loop 3:
    set f 1
    set d 2
        -- LOOP 2
    jnz f 2     if f == 0: h += 1
    sub h -1
    set g b
    sub g c
    jnz g 2     if b == c: exit
    jnz 1 3     -- This is the exit instruction 1 is never 0 and the offset of 3 takes us out of the program
    sub b -17   b += 17
    jnz 1 -23   alllways go back to start of loop

    Translates to
    while True:
        f = 1
        d = 2
        loop2
        if f == 0:
            h -= 1
        if b == c:
            break
        b += 17

    So the complete program looks like this
    b = 105700
    c = 122700
    while True:
        f = 1
        d = 2
        while d != b:
            while e != b:
                if d * e  == b:
                    f = 0
                e += 1
            d += 1
        if f == 0:
            h += 1
        if b == c:
            break
        b += 17

    which can be further simplified to
    b = 105700
    h = 0
    while b != 122700:
        f = 1
        for d in range(2,b,1):
            for e in range(b):
                if d * e  == b:
                    f = 0
        if f == 0:
            h += 1

        b += 17

    which in turn can be simplified to
    h = 0
    b = 105700
    while True:
        b = 105700 + (i*17)
        if any(d * e == b for d in range(2,b,1) for e in range(b)):
            h += 1
        if b == 122700:
            break
        b += 17

    This shows that the only thing of importance is if for any (x,y) in
    ([2..b],[0..b]) there is one for which a*y == b
    Which means we are basically checking if b is a prime

    There's not default is_prime in python, but there are a couple of standard solution, so I grapped one from the interwebs
    ending up with:
    '''
    h = 0
    b = 105700
    while True:
        if not is_prime(b):
            h += 1
        if b == 122700:
            break
        b += 17
    return h

print('The solution to puzzle 2 is: {}'.format(puzzle_2(puzzle_input)))

