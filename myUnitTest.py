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

    def testMinus(self):
        minusResult = self.calculator.minus(3,2)
        self.assertEqual(minusResult, 1)
        
    def testMultiply(self):
        multiplyResult = self.calculator.multiply(5,4)
        self.assertEquals(multiplyResult, 20)
        
    if __name__ == "__main__":
        unittest.main()
    