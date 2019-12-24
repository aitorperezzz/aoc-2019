import unittest
import problem12

class TestMoons(unittest.TestCase):
    def testFullProblem(self):
        result = problem12.main('test1.dat', 10)
        self.assertEqual(result['energy'], 179)
        self.assertEqual(result['repeat'], 2772)
        result = problem12.main('test2.dat', 100)
        self.assertEqual(result['energy'], 1940)
        self.assertEqual(result['repeat'], 4686774924)

if __name__ == '__main__':
    unittest.main()