import unittest
import problem6

# Define the testing class.
class TestProblem6(unittest.TestCase):
    def testTotalNumberOrbits(self):
        self.assertEqual(problem6.solveProblem('test.dat', False)['orbits'], 42)

    def testShortestPath(self):
        self.assertEqual(problem6.solveProblem('test_part2.dat', True)['shortest'], 4)

unittest.main()