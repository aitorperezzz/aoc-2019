import sys
sys.path.append('../')
import computer

FILENAME = 'input.dat'
if len(sys.argv) == 2:
    FILENAME = sys.argv[1]

def main(filename):

    # Get a copy of the BOOST software.
    boostProgram = computer.readProgramFromFile(filename)
    boostProgram.printOutputs(False)

    # Solve part one.
    boostProgram.setInputs([1])
    boostProgram.execute()
    print('BOOST parameter: {}'.format(boostProgram.getOutputs()[-1]))

    # Solve part two.
    boostProgram.resetExecutionState()
    boostProgram.setInputs([2])
    boostProgram.execute()
    print('Coordinates of the distress signal: {}'.format(boostProgram.getOutputs()[-1]))

if __name__ == '__main__':
    main(FILENAME)