import sys
sys.path.append('../')
import computer
import pdb

def main(filename):

    # Solve part one of the problem.
    result = solvePartOne(filename)
    print('Sum of the alignment parameters: {}'.format(result['total']))

    # Print the state of the exterior of the ship.
    for line in result['scaffold']:
        for symbol in line:
            print(symbol, end='')
        print()

    # Solve part two of the problem.
    dust = solvePartTwo(filename)
    print('Dust collected: {}'.format(dust))


# Solves the first part of the problem. Returns the sum of alignment parameters
# of all the intersection points.
def solvePartOne(filename):

    # Load the ASCII program from file.
    asciiProgram = computer.readProgramFromFile(filename)

    # Execute it and extract the outputs.
    asciiProgram.printOutputs(False)
    asciiProgram.execute()
    outputs = asciiProgram.getOutputs()

    # Loop through the outputs and store the information.
    scaffold = [[]]
    position = 0
    for element in outputs:
        # If new line, add another line to the main list.
        if str(chr(element)) == '\n':
            scaffold.append([])
            position += 1
            continue
        
        # If not a newline, add it to the current line.
        scaffold[position].append(str(chr(element)))
    
    # Calculate the alignment parameters.
    return {'scaffold': scaffold, 'total': sumOfAlignmentParameters(scaffold)}

# Loops through all the intersections and calculates the alignment parameter
# for each one. Then returns the sum of all of them.
def sumOfAlignmentParameters(scaffold):

    total = 0
    for i in range(len(scaffold)):
        for j in range(len(scaffold[i])):

            # First check if this is a scaffold or not.
            if not isScaffold(scaffold[i][j]):
                continue

            # It is not an intersection if it is on the edge
            if i == 0 or i == len(scaffold) - 1:
                continue
            if j == 0 or j == len(scaffold[i]) - 1:
                continue

            # If not on the edge, check it has scaffold on all four sides.
            if not isScaffold(scaffold[i][j - 1]) or not isScaffold(scaffold[i][j + 1]):
                continue
            if not isScaffold(scaffold[i - 1][j]) or not isScaffold(scaffold[i + 1][j]):
                continue
            
            total += i * j
    
    return total

# Decides if an element in the exterior is a scaffold or not.
def isScaffold(symbol):
    return symbol == '#' or symbol == '^' or symbol == '<' or symbol == '>' or symbol == 'v'

# Solves part two returning the quantity of dust collected.
def solvePartTwo(filename):

    # Load the software and modify its configuration.
    asciiProgram = computer.readProgramFromFile(filename)
    asciiProgram.setMemory(0, 2)
    asciiProgram.printOutputs(False)

    # Decide the inputs.
    mainRoutine = 'A,B,B,C,A,B,C,A,B,C\n'
    routineA = 'L,6,R,12,L,4,L,6\n'
    routineB = 'R,6,L,6,R,12\n'
    routineC = 'L,6,L,10,L,10,R,6\n'
    decide = 'n\n'
    inputData = [mainRoutine, routineA, routineB, routineC, decide]
    
    # Set the inputs and execute the program.
    inputs = getInputsAsNumbers(inputData)
    asciiProgram.setInputs(inputs)
    asciiProgram.execute()

    return asciiProgram.getOutputs()[-1]

# Receives the lines with the routines and transforms characters
# to ascii codes in a list.
def getInputsAsNumbers(inputData):

    inputs = []
    for line in inputData:
        for symbol in line:
            inputs.append(ord(symbol))
    
    return inputs

if __name__ == '__main__':
    main('ascii.dat')
