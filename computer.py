# computer.py is the module for executing intcode programs.

import pdb

# Define the opcodes.
OPCODE_SUM = 1
OPCODE_MULTIPLY = 2
OPCODE_INPUT = 3
OPCODE_OUTPUT = 4
OPCODE_JUMP_IF_TRUE = 5
OPCODE_JUMP_IF_FALSE = 6
OPCODE_LESS_THAN = 7
OPCODE_EQUALS = 8
OPCODE_HALT = 99

# Define the parameter modes.
PARAMETER_POSITION = 0
PARAMETER_VALUE = 1

# Stores information about an opcode.
class Opcode():
    def __init__(self, opcode):
        # Get the opcode itself.
        self.opcode = opcode % 100

        # Get the parameters modes.
        self.modes = []
        value = int(opcode / 100)
        while value >= 1:
            self.modes.append(value % 10)
            value = int(value / 10)

# Receives a filename and returns a list with the integers of the program.
def readProgramFromFile(filename):
    with open(filename, 'r') as inputFile:
        program = [int(element) for element in inputFile.read().rstrip('\n').replace(' ', '').split(',')]
    
    return program

def copyProgram(initial):
    result = []
    for number in initial:
        result.append(number)
    
    return result

def executeProgram(program):
    position = 0
    length = len(program)
    while position < length:

        # Parse the next opcode.
        opcode = Opcode(program[position])

        # Execute the appropriate operation.
        if opcode.opcode == OPCODE_SUM:
            position = executeSum(program, position, opcode.modes)
        elif opcode.opcode == OPCODE_MULTIPLY:
            position = executeMultiplication(program, position, opcode.modes)
        elif opcode.opcode == OPCODE_INPUT:
            position = executeInput(program, position)
        elif opcode.opcode == OPCODE_OUTPUT:
            position = executeOutput(program, position, opcode.modes)
        elif opcode.opcode == OPCODE_JUMP_IF_TRUE:
            position = executeJumpIfTrue(program, position, opcode.modes)
        elif opcode.opcode == OPCODE_JUMP_IF_FALSE:
            position = executeJumpIfFalse(program, position, opcode.modes)
        elif opcode.opcode == OPCODE_LESS_THAN:
            position = executeLessThan(program, position, opcode.modes)
        elif opcode.opcode == OPCODE_EQUALS:
            position = executeEquals(program, position, opcode.modes)
        elif opcode.opcode == OPCODE_HALT:
            return program
        else:
            print('ERROR: opcode {} not recognised by the computer'.format(program[position]))

# Receives a starting position and a program, and returns the values for the parameters.
# If in positional mode, it accessess the address, else it returns the value itself.
def parseParameters(program, position, modes, totalParameters):
    values = []
    for i in range(totalParameters):
        if i < len(modes):
            # We have a code for the parameters's mode.
            value = program[program[position + i]] if modes[i] == PARAMETER_POSITION else program[position + i]
        else:
            # The default mode is positional.
            value = program[program[position + i]]
        values.append(value)

    return values

def executeSum(program, position, modes):
    # Parse the parameters to know the values.
    values = parseParameters(program, position + 1, modes, 2)

    # Store the result at the appropriate address.
    program[program[position + 3]] = values[0] + values[1]

    return position + 4

def executeMultiplication(program, position, modes):
    # Parse the parameters to know the values.
    values = parseParameters(program, position + 1, modes, 2)

    # Store the result at the appropriate address.
    program[program[position + 3]] = values[0] * values[1]

    return position + 4

def executeInput(program, position):
    number = input('Input: ')
    program[program[position + 1]] = int(number)

    return position + 2

def executeOutput(program, position, modes):
    values = parseParameters(program, position + 1, modes, 1)
    print('Output: {}'.format(values[0]))

    return position + 2

def executeJumpIfTrue(program, position, modes):
    values = parseParameters(program, position + 1, modes, 2)

    return values[1] if values[0] != 0 else position + 3

def executeJumpIfFalse(program, position, modes):
    values = parseParameters(program, position + 1, modes, 2)

    return values[1] if values[0] == 0 else position + 3

def executeLessThan(program, position, modes):
    values = parseParameters(program, position + 1, modes, 2)

    program[program[position + 3]] = 1 if values[0] < values[1] else 0

    return position + 4

def executeEquals(program, position, modes):
    values = parseParameters(program, position + 1, modes, 2)

    program[program[position + 3]] = 1 if values[0] == values[1] else 0

    return position + 4