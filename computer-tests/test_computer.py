import unittest
import sys

# Import the computer module.
sys.path.append('../')
import computer

# Class to completely test the computer, one function for each problem.
class TestComputer(unittest.TestCase):

    # Test the cases that appear in problem 2.
    def testProblem2(self):
        program = computer.executeProgram([1,9,10,3,2,3,11,0,99,30,40,50])
        self.assertEqual(program, [3500,9,10,70,2,3,11,0,99,30,40,50])
        
        program = computer.executeProgram([1,0,0,0,99])
        self.assertEqual(program, [2,0,0,0,99])
        
        program = computer.executeProgram([2,3,0,3,99])
        self.assertEqual(program, [2,3,0,6,99])
        
        program = computer.executeProgram([2,4,4,5,99,0])
        self.assertEqual(program, [2,4,4,5,99,9801])

        program = computer.executeProgram([1,1,1,4,99,5,6,0,99])
        self.assertEqual(program, [30,1,1,4,2,5,6,0,99])


if __name__ == '__main__':
    unittest.main()