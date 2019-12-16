import unittest

# Import the module to be tested.
import problem3

# Define the test class.
class TestWires(unittest.TestCase):
    # Test the Manhattan distance to the closest intersection between wires.
    def testClosestDistance(self):
        self.assertEqual(problem3.solveProblem('test1.dat'), 159)
        self.assertEqual(problem3.solveProblem('test2.dat'), 135)

unittest.main()