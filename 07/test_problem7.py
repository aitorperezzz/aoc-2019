import unittest
import problem7

class TestProblem7(unittest.TestCase):
    def testPartOne(self):
        resultsTest1 = problem7.solvePartOne('test1.dat')
        self.assertEqual(resultsTest1['bestOutput'], 43210)
        self.assertEqual(resultsTest1['bestSettings'], [4,3,2,1,0])

        resultsTest1 = problem7.solvePartOne('test2.dat')
        self.assertEqual(resultsTest1['bestOutput'], 54321)
        self.assertEqual(resultsTest1['bestSettings'], [0,1,2,3,4])

        resultsTest1 = problem7.solvePartOne('test3.dat')
        self.assertEqual(resultsTest1['bestOutput'], 65210)
        self.assertEqual(resultsTest1['bestSettings'], [1,0,4,3,2])

if __name__ == '__main__':
    unittest.main()