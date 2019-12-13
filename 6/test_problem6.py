import unittest
import problem6

# Define the testing class.
class TestProblem6(unittest.TestCase):
    def testNumberOrbits(self):
        self.assertEqual(problem6.calculateNumberOrbits('test.dat'), 42)

unittest.main()