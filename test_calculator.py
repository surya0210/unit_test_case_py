import unittest
import calculator
from calculatorv2 import Calculator

class TestsCalculator(unittest.TestCase):

    def test_add_functionality(self):
        result=calculator.calc_add(10,20)
        self.assertEqual(result,30)

    def test_add_functionality_two_negative(self):
        result=calculator.calc_add(-10,-20)
        self.assertEqual(result,-30)

    def test_add_functionality_class(self):
        calc1=Calculator(10,20)
        result=calc1.calc_add()
        self.assertAlmostEqual(result,31,delta=1)


    def test_sub_functionality_class(self):
        calc1=Calculator(10,20)
        result=calc1.calc_sub()
        self.assertAlmostEqual(result,-10,delta=1)
    
    def test_mul_functionality_class(self):
        calc1=Calculator(10,20)
        result=calc1.calc_mul()
        self.assertAlmostEqual(result,200,delta=1)

    @unittest.skipUnless(False,"hgfhfgh")
    def test_div_functionality_class(self):
        calc1=Calculator(10,20)
        result=calc1.calc_div()
        self.assertAlmostEqual(result,.5,delta=1)
    
        # pass