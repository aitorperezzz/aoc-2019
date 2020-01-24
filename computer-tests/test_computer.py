import unittest
import sys

# Import the computer module.
sys.path.append('../')
import computer

# Class to completely test the computer, one function for each problem.
class TestComputer(unittest.TestCase):

    # Test the cases that appear in problem 2.
    def testProblem2(self):
        program = computer.Program()

        program.setInstructions([1,9,10,3,2,3,11,0,99,30,40,50])
        program.resetExecutionState()
        program.execute()
        self.assertEqual(program.getInstructions(), [3500,9,10,70,2,3,11,0,99,30,40,50])

        program.setInstructions([1,0,0,0,99])
        program.resetExecutionState()
        program.execute()
        self.assertEqual(program.getInstructions(), [2,0,0,0,99])

        program.setInstructions([2,3,0,3,99])
        program.resetExecutionState()
        program.execute()
        self.assertEqual(program.getInstructions(), [2,3,0,6,99])

        program.setInstructions([2,4,4,5,99,0])
        program.resetExecutionState()
        program.execute()
        self.assertEqual(program.getInstructions(), [2,4,4,5,99,9801])

        program.setInstructions([1,1,1,4,99,5,6,0,99])
        program.resetExecutionState()
        program.execute()
        self.assertEqual(program.getInstructions(), [30,1,1,4,2,5,6,0,99])
    
    def testProblem5(self):

        # Test part one of the problem.
        program = computer.readProgramFromFile('../05/input.dat')
        program.printOutputs(False)
        program.setInputs([1])
        program.execute()
        outputs = program.getOutputs()
        for i in range(len(outputs) - 1):
            self.assertEqual(outputs[i], 0)
        self.assertEqual(outputs[-1], 16434972)

        # Test input equal to 8 using position mode.
        program.setInstructions([3,9,8,9,10,9,4,9,99,-1,8])
        program.resetExecutionState()
        program.setInputs([8])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1)
        program.setInstructions([3,9,8,9,10,9,4,9,99,-1,8])
        program.resetExecutionState()
        program.setInputs([5])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 0)

        # Test input less than 8 using position mode.
        program.setInstructions([3,9,7,9,10,9,4,9,99,-1,8])
        program.resetExecutionState()
        program.setInputs([6])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1)
        program.setInstructions([3,9,7,9,10,9,4,9,99,-1,8])
        program.resetExecutionState()
        program.setInputs([10])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 0)
        program.setInstructions([3,9,7,9,10,9,4,9,99,-1,8])
        program.resetExecutionState()
        program.setInputs([8])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 0)

        # Test input equal to 8 using immediate mode.
        program.setInstructions([3,3,1108,-1,8,3,4,3,99])
        program.resetExecutionState()
        program.setInputs([8])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1)
        program.setInstructions([3,3,1108,-1,8,3,4,3,99])
        program.resetExecutionState()
        program.setInputs([5])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 0)

        # Test less than 8 using immediate mode.
        program.setInstructions([3,3,1107,-1,8,3,4,3,99])
        program.resetExecutionState()
        program.setInputs([6])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1)
        program.setInstructions([3,3,1107,-1,8,3,4,3,99])
        program.resetExecutionState()
        program.setInputs([10])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 0)
        program.setInstructions([3,3,1107,-1,8,3,4,3,99])
        program.resetExecutionState()
        program.setInputs([8])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 0)

        # Test jump: output 0 if the input was 0, 1 if the input was different from 0.
        # In position mode.
        program.setInstructions([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
        program.resetExecutionState()
        program.setInputs([0])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 0)
        program.setInstructions([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
        program.resetExecutionState()
        program.setInputs([15])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1)
        # In immediate mode.
        program.setInstructions([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])
        program.resetExecutionState()
        program.setInputs([0])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 0)
        program.setInstructions([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])
        program.resetExecutionState()
        program.setInputs([15])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1)

        # Large test, test if equal, less, greater than 8.
        program.setInstructions([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        program.resetExecutionState()
        program.setInputs([2])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 999)
        program.setInstructions([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        program.resetExecutionState()
        program.setInputs([10])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1001)
        program.setInstructions([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        program.resetExecutionState()
        program.setInputs([8])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1000)

        # Test part two of the problem.
        program = computer.readProgramFromFile('../05/input.dat')
        program.printOutputs(False)
        program.setInputs([5])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 16694270)
    
    # The tests for problem 7 are inside that folder.

    # Run the tests for the characteristics of problem 7.
    def testProblem9(self):

        # Test a program that should produce a copy of itself.
        instructions = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        program = computer.Program(instructions)
        program.printOutputs(False)
        program.execute()
        self.assertEqual(program.getOutputs(), instructions)

        # The number in output should be 16 digits long.
        program = computer.Program([1102,34915192,34915192,7,4,7,99,0])
        program.printOutputs(False)
        program.execute()
        self.assertEqual(len(str(program.getOutputs()[0])), 16)

        # This program should output the big number it contains.
        program = computer.Program([104,1125899906842624,99])
        program.printOutputs(False)
        program.execute()
        self.assertEqual(program.getOutputs()[0], 1125899906842624)

        # Test the problem itself.
        program = computer.readProgramFromFile('../09/input.dat')
        program.printOutputs(False)
        program.setInputs([1])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 2662308295)
        program = computer.readProgramFromFile('../09/input.dat')
        program.printOutputs(False)
        program.setInputs([2])
        program.execute()
        self.assertEqual(program.getOutputs()[0], 63441)


if __name__ == '__main__':
    unittest.main()