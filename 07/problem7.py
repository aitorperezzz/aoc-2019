import sys
sys.path.append('../')
import computer
import math
import pdb

# Decide the filename.
FILENAME = 'input.dat'
if len(sys.argv) == 2:
    FILENAME = sys.argv[1]

def main(filename):

    # Load the amplifier software.
    amplifierSoftware = computer.readProgramFromFile(filename)

    # Create a table with all possible settings.
    settings = []
    currentSettings = getNextCombination(None, 5)
    while currentSettings != None:
        settings.append(copyList(currentSettings))
        currentSettings = getNextCombination(currentSettings, 5)

    # Create the results table, initialized to None.
    results = []
    for i in range(len(settings)):
        results.append([])
        for j in range(len(settings[i])):
            results[i].append(None)

    # Fill in the results table.
    for i in range(len(results)):
        for j in range(len(results[i])):
            currentInput = None
            if i - 1 >= 0:
                # Decide if all the row of settings is the same until position j (included).
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
            
            # Get a copy of the amplifier software and decide on the input value.
            program = computer.copyProgram(amplifierSoftware)
            currentInput = results[i][j - 1] if j - 1 >= 0 else 0

            # Run the operation.
            results[i][j] = computer.executeProgram(program, [settings[i][j], currentInput], False)[0]

    # Find the best value in the table.
    bestOutput = - math.inf
    index = 0
    for k in range(len(results)):
        if results[k][4] > bestOutput:
            bestOutput = results[k][4]
            index = k
    bestSettings = settings[index]

    print('The best output for thrusters is {}'.format(bestOutput))
    print('best sequence for thrusters: {}'.format(bestSettings))

# Gets an array with a permutation and returns the next one.
# Returns None if it reached the end.
def getNextCombination(combination, size):
    #pdb.set_trace()
    if combination == None:
        return list(range(size))
    else:
        for i in reversed(range(size - 1)):

            # Look for the first time a number is lesser than the next one.
            if combination[i] < combination[i + 1]:
                # Get a sorted list of the numbers we can assign to position i.
                available = sorted(combination[(i + 1):])

                # Get the smallest one that is bigger than the i-th.
                for j in range(len(available)):
                    if available[j] > combination[i]:
                        combination[i] = available[j]
                        break

                # Order the rest of the sequence with the remaining numbers.
                position = i + 1
                for j in range(size):
                    if not j in combination[:(i + 1)]:
                        combination[position] = j
                        position += 1
                
                return combination

                
        return None

# Copies a list and returns it.
def copyList(listProvided):
    result = []
    for element in listProvided:
        result.append(element)
    
    return result

if __name__ == '__main__':
    main(FILENAME)