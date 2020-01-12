import sys
sys.path.append('../')
import computer

# Choose the name of the input file.
FILENAME = 'input.dat'
if len(sys.argv) == 2:
    FILENAME = sys.argv[1]

# Read and execute.
def main(filename):
    program = computer.readProgramFromFile(filename)
    computer.executeProgram(program)

# Execute main function if the program is ran.
if __name__ == '__main__':
    main(FILENAME)