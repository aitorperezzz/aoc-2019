import unittest
import problem10

class TestAsteroids(unittest.TestCase):
    def testBestLocation(self):
        bestx = [3, 5, 1, 6, 11]
        besty = [4, 8, 2, 3, 13]
        visibles = [8, 33, 35, 41, 210]
        for i in range(4):
            result = problem10.main('tests/test' + str(i + 1) + '.dat')
            self.assertEqual(result['bestx'], bestx[i])
            self.assertEqual(result['besty'], besty[i])
            self.assertEqual(result['visibles'], visibles[i])

# Call the main function
if __name__ == '__main__':
    unittest.main()