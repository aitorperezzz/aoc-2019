import sys
sys.path.append('../')
import computer

FILENAME = 'input.dat'

def main(filename):

    # Keep a backup of the initial instructions.
    instructions = computer.readInstructionsFromFile(filename)

    # Create a program with the previous instructions.
    program = computer.Program(instructions)

    # Change some values in the program.
    program.instructions[1] = 12
    program.instructions[2] = 2

    # Execute the program to get the result of part one.
    program.execute()

    # Print the result.
    print('Value at position 0 after execution: {}'.format(program.instructions[0]))

    # Try all nouns and verbs possible to get the result of part two.
    for noun in range(0, 100):
        for verb in range(0, 100):
            # Reset the program to the initial memory.
            program = computer.Program(instructions)

            # Change the noun and verb.
            program.instructions[1] = noun
            program.instructions[2] = verb

            # Execute the program.
            program.execute()

            if program.instructions[0] == 19690720:
                print('100 * noun + verb: {}'.format(100 * noun + verb))
                return

if __name__ == '__main__':
    main(FILENAME)
