'''

'''

'''
puzzle input:
Begin in state A.
Perform a diagnostic checksum after 12208951 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state E.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state A.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state D.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state F.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
'''

class Tape:
    def __init__(self):
        self.values = [0]
        self.position = 0

    def write(self, value):
        self.values[self.position] = value

    def read(self):
        return self.values[self.position]

    def move_left(self):
        if self.position == 0:
            self.values.insert(0,0)
        else:
            self.position -= 1

    def move_right(self):
        self.position += 1
        if self.position == len(self.values):
            self.values.append(0)

def StateA(tape):
    if tape.read() == 0:
        tape.write(1)
        tape.move_right()
        return StateB
    else:
        tape.write(0)
        tape.move_left()
        return StateE

def StateB(tape):
    if tape.read() == 0:
        tape.write(1)
        tape.move_left()
        return StateC
    else:
        tape.write(0)
        tape.move_right()
        return StateA

def StateC(tape):
    if tape.read() == 0:
        tape.write(1)
        tape.move_left()
        return StateD
    else:
        tape.write(0)
        tape.move_right()
        return StateC

def StateD(tape):
    if tape.read() == 0:
        tape.write(1)
        tape.move_left()
        return StateE
    else:
        tape.write(0)
        tape.move_left()
        return StateF

def StateE(tape):
    if tape.read() == 0:
        tape.write(1)
        tape.move_left()
        return StateA
    else:
        tape.write(1)
        tape.move_left()
        return StateC

def StateF(tape):
    if tape.read() == 0:
        tape.write(1)
        tape.move_left()
        return StateE
    else:
        tape.write(1)
        tape.move_right()
        return StateA
    
def puzzle1():
    state = StateA
    tape = Tape()
    for i in range(12208951):
        state = state(tape);
    return tape.values.count(1)

print('The result for puzzle 1 is {}'.format(puzzle1()))