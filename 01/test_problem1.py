import unittest

# Import the module to be tested.
import problem1

# Define the test class.
class TestFuelMass(unittest.TestCase):
    def testFuelMass(self):
        self.assertEqual(problem1.calculateFuelMass(12), 2)
        self.assertEqual(problem1.calculateFuelMass(14), 2)
        self.assertEqual(problem1.calculateFuelMass(1969), 654)
        self.assertEqual(problem1.calculateFuelMass(100756), 33583)

    def testTotalFuelMass(self):
        self.assertEqual(problem1.calculateTotalFuelMass(14), 2)
        self.assertEqual(problem1.calculateTotalFuelMass(1969), 966)
        self.assertEqual(problem1.calculateTotalFuelMass(100756), 50346)

unittest.main()