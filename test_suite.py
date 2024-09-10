import unittest
import test_calculator
# Create an instance of test loader
loader=unittest.TestLoader()


#Create an instance of Test suite
suite=unittest.TestSuite()

#load test case from a module
suite.addTests(loader.loadTestsFromModule(test_calculator))
# suite.addTests(loader.loadTestsFromModule(test_calculator))
# suite.addTests(loader.loadTestsFromModule(test_calculator))


#load test case from a class 
suite.addTests(loader.loadTestsFromTestCase(test_calculator.TestsCalculator))


#create an instance of runner

runner=unittest.TextTestRunner()

test_result=runner.run(suite)

print(test_result.testsRun)


test_result.addDuration(elapsed=5,test=1)