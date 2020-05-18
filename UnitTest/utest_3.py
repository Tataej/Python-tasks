##3. How Many Solutions Does This Quadratic Have?
##A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. Given a, b and c, you should return the number of solutions to the equation.
##Examples
##solutions(1, 0, -1) ➞ 2
##// x² - 1 = 0 has two solutions (x = 1 and x = -1).
## 
##solutions(1, 0, 0) ➞ 1
##// x² = 0 has one solution (x = 0).
## 
##solutions(1, 0, 1) ➞ 0
##// x² + 1 = 0 has no solutions.
##Notes
##You do not have to calculate the solutions, just return how many there are.
##a will always be non-zero.

import math

def solutions(a, b, c):
    d = b**2-4*a*c 
    if d < 0:
        print ("solutions(%d, %d, %d) --> 0" %(a, b, c))
        return 0
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        print ("solutions(%d, %d, %d) --> 1" %(a, b, c))
        return 1
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        print ("solutions(%d, %d, %d) --> 2" %(a, b, c))
        return 2

##a = int(input("Enter the coefficients of a: "))
##b = int(input("Enter the coefficients of b: "))
##c = int(input("Enter the coefficients of c: "))
##print(solutions(a, b, c))

import unittest

   
class TestSolutions(unittest.TestCase):
    """My Test"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("===========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("tearDownClass")
        print("===========")

    def setUp(self):
        """Set up for test"""
        print("setUp")
        print("===========")

    def tearDown(self):
        """Tear down for test"""
        print("===========")
        print("tearDownClass")

    def test_result1(self):
        """Check when result = 1"""
        print("id: " + self.id())
        self.assertEqual(solutions(1, 0, 0), 1)

    def test_result2(self):
        """Check when result = 2"""
        print("id: " + self.id())
        self.assertEqual(solutions(1, 0, -1), 2)
        
    def test_result0(self):
        """Check when result = 0"""
        print("id: " + self.id())
        self.assertEqual(solutions(1, 0, 1),0)

        


if __name__ == '__main__':
    unittest.main()



 
