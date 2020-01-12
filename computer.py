# computer.py is the module for executing intcode programs.
COMPUTER_SUM = 1
COMPUTER_MULTIPLY = 2
COMPUTER_HALT = 99

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
        # Execute the appropriate operation.
        if program[position] == COMPUTER_SUM:
            executeSum(program, program[position + 1], program[position + 2], program[position + 3])
        elif program[position] == COMPUTER_MULTIPLY:
            executeMultiplication(program, program[position + 1], program[position + 2], program[position + 3])
        elif program[position] == COMPUTER_HALT:
            return program
        else:
            print('ERROR: computer does not recognise opcode {}'.format(program[position]))
        
        position += 4

def executeSum(program, input1, input2, output):
    program[output] = program[input1] + program[input2]

def executeMultiplication(program, input1, input2, output):
    program[output] = program[input1] * program[input2]