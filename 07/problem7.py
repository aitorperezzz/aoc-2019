import sys
sys.path.append('../')
import computer
import math
import pdb

# Decide the filename.
FILENAME = 'input.dat'

def main(filename):

    # Solve part one of the problem.
    resultsPartOne = solvePartOne(filename)
    print('Part 1. Best output for thrusters: {}'.format(resultsPartOne['bestOutput']))
    print('Part 1. Best sequence for thrusters: {}'.format(resultsPartOne['bestSettings']))

    # Solve the second part.
    bestInLoop = solvePartTwo(filename)
    print('Best result when the amplifiers are in a loop: {}'.format(bestInLoop))

# Solves the first part of the problem.
def solvePartOne(filename):

    # Load the amplifier software.
    amplifierSoftware = computer.readInstructionsFromFile(filename)

    # Create a table with all possible settings.
    settings = []
    currentSettings = getNextPermutation(None, 0, 5)
    while currentSettings != None:
        settings.append(copyList(currentSettings))
        currentSettings = getNextPermutation(currentSettings, 0, 5)

    # Create the results table, initialized to None.
    results = []
    for i in range(len(settings)):
        results.append([])
        for j in range(len(settings[i])):
            results[i].append(None)

    # Fill in the results table.
    for i in range(len(results)):
        for j in range(len(results[i])):
            if i - 1 >= 0:
                # Decide if the previous row of settings is the same until position j included.
                differ = False
                for k in range(j + 1):
                    if settings[i][k] != settings[i - 1][k]:
                        # The settings are not the same.
                        differ = True
                        break
                
                # If the rows of settings do not differ, copy the value and move on.
                if not differ:
                    results[i][j] = results[i - 1][j]
                    continue
            
            # Get a copy of the amplifier software and decide the input value.
            program = computer.Program(amplifierSoftware)
            currentInput = results[i][j - 1] if j - 1 >= 0 else 0
            program.setInputs([settings[i][j], currentInput])
            program.printOutputs(False)

            # Run the operation.
            program.execute()
            results[i][j] = program.getOutputs()[0]

    # Find the best output value and the best sequence.
    bestOutput = - math.inf
    index = 0
    for k in range(len(results)):
        if results[k][4] > bestOutput:
            bestOutput = results[k][4]
            index = k
    bestSettings = settings[index]

    return {'bestOutput':bestOutput, 'bestSettings': bestSettings}


def solvePartTwo(filename):

    # Load the amplifier software.
    amplifierSoftware = computer.readInstructionsFromFile(filename)

    # Create a table with all possible settings.
    settings = []
    currentSettings = getNextPermutation(None, 5, 5)
    while currentSettings != None:
        settings.append(copyList(currentSettings))
        currentSettings = getNextPermutation(currentSettings, 5, 5)
    
    # Create an array for the five amplifiers.
    amplifiers = []
    for i in range(5):
        amplifiers.append(computer.Program())
        amplifiers[i].printOutputs(False)
        amplifiers[i].returnOnFirstOutput(True)
        amplifiers[i].setInputs([])

    # Calculate results and keep the best.
    bestResult = - math.inf
    for i in range(len(settings)):

        # Reset the software of all the amplifiers.
        for j in range(len(amplifiers)):
            amplifiers[j].setInstructions(amplifierSoftware)
            amplifiers[j].resetPosition()
            amplifiers[j].emptyOutputs()

            # Establish the settings of all five amplifiers.
            amplifiers[j].setInputs([settings[i][j]])

        
        # Execute in a loop until one of the programs halts with a HALT instruction.
        currentInput = 0
        lastFinishResult = computer.FINISH_ERROR
        index = 0
        while True:

            # Set the input for the next amplifier.
            amplifiers[index].appendToInputs([currentInput])

            # Execute the 'index' amplifier with the previous input.
            amplifiers[index].emptyOutputs()
            amplifiers[index].returnOnFirstOutput(True)
            lastFinishResult = amplifiers[index].execute()

            # Break if the program reached a HALT instruction.
            if lastFinishResult == computer.FINISH_HALT:
                break

            # Get the output of the previous run.
            currentInput = amplifiers[index].getOutputs()[0]

            # Update the index.
            index = (index + 1) % len(amplifiers)
        
        # Store, in results, the last output from the last amplifier.
        result = amplifiers[4].getOutputs()[0]
        if result > bestResult:
            bestResult = result
    
    return bestResult


# Receives a permutation and returns the next one.
def getNextPermutation(permutation, begin, size):
    # If None is given, provide the first permutation.
    if permutation == None:
        return list(range(begin, begin + size))
    else:
        for i in reversed(range(size - 1)):

            # Look for the first time a number is lesser than the next one.
            if permutation[i] < permutation[i + 1]:
                # Get a sorted list of the numbers we can assign to position i.
                available = sorted(permutation[(i + 1):])

                # Get the smallest one that is bigger than the i-th.
                for j in range(len(available)):
                    if available[j] > permutation[i]:
                        permutation[i] = available[j]
                        break

                # Order the rest of the sequence with the remaining numbers.
                position = i + 1
                for j in range(begin, begin + size):
                    if not j in permutation[:(i + 1)]:
                        permutation[position] = j
                        position += 1
 
                return permutation

        return None

# Copies a list and returns it.
def copyList(listProvided):
    result = []
    for element in listProvided:
        result.append(element)
    
    return result

if __name__ == '__main__':
    main(FILENAME)