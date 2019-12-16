import unittest
import problem6

# Define the testing class.
class TestProblem6(unittest.TestCase):
    def testNumberOrbits(self):
        result = 
        self.assertEqual(problem6.solveProblem('test.dat')['orbits'], 42)
        self.assertEqual(problem6.solveProblem('test_part2.dat')['shortest'], 4)

unittest.main()