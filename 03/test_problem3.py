import unittest
import problem3

# Define the test class.
class TestWires(unittest.TestCase):
    # Test minimal distance to intersection between wires and
    # minimal signal delay.
    def testMinimalValues(self):
        result = problem3.calculateResults('test1.dat')
        self.assertEqual(result['closest'], 159)
        self.assertEqual(result['minDelay'], 610)
        result = problem3.calculateResults('test2.dat')
        self.assertEqual(result['closest'], 135)
        self.assertEqual(result['minDelay'], 410)

# Call main function if the file is executed.
if __name__ == '__main__':
    unittest.main()