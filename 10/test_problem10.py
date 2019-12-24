import unittest
import problem10

class TestAsteroids(unittest.TestCase):
    def testBestLocation(self):
        bestx = [3, 5, 1, 6]
        besty = [4, 8, 2, 3]
        visibles = [8, 33, 35, 41]
        for i in range(4):
            result = problem10.main('tests/test' + str(i + 1) + '.dat', full=False)
            self.assertEqual(result['bestx'], bestx[i])
            self.assertEqual(result['besty'], besty[i])
            self.assertEqual(result['visibles'], visibles[i])

    def testBestLocationAndVaporized(self):
        result = problem10.main('tests/test5.dat', full=True)
        self.assertEqual(result['bestx'], 11)
        self.assertEqual(result['besty'], 13)
        self.assertEqual(result['visibles'], 210)
        self.assertEqual(result['vaporizedx'], 8)
        self.assertEqual(result['vaporizedy'], 2)

# Call the main function when the file is executed.
if __name__ == '__main__':
    unittest.main()