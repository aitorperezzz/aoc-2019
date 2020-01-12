import unittest
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

# Run the main function if the file is executed, not imported.
if __name__ == '__main__':
    unittest.main()