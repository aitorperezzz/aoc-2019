import sys
sys.path.append('../')
import computer

FILENAME = 'input.dat'

def main(filename):
    # Read the program from the file.
    program = computer.readProgramFromFile(FILENAME)

    # Keep a backup of the initial memory.
    memory = computer.copyProgram(program)
 
    # Change some values in the program.
    program[1] = 12
    program[2] = 2

    # Execute the program to get the result of part one.
    computer.executeProgram(program)

    # Print the result.
    print('Value at position 0 after execution: {}'.format(program[0]))

    # Try all nouns and verbs possible to get the result of part two.
    for noun in range(0, 100):
        for verb in range(0, 100):
            # Reset the program to the initial memory.
            program = computer.copyProgram(memory)

            # Change the noun and verb.
            program[1] = noun
            program[2] = verb

            # Execute the program.
            computer.executeProgram(program)

            if program[0] == 19690720:
                print('100 * noun + verb: {}'.format(100 * noun + verb))
                return

if __name__ == '__main__':
    main(FILENAME)
