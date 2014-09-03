import unittest
import myCalculator

class myUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.calculator = myCalculator.myCalculator();
    
    def tearDown(self):
        pass
    
    def testSum(self):
        sumResult = self.calculator.sum(2,3)
        self.assertEqual(sumResult, 5)

    if __name__ == "__main__":
        unittest.main()
    