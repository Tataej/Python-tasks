##1. FizzBuzz Interview Question
##Create a function that takes a number as an argument and returns "Fizz",
##"Buzz" or "FizzBuzz".
##If the number is a multiple of 3 the output should be "Fizz".
##If the number given is a multiple of 5, the output should be "Buzz".
##If the number given is a multiple of both 3 and 5, the output should be
##"FizzBuzz".
##If the number is not a multiple of either 3 or 5, the number should be
##output on its own as shown in the examples below.
##The output should always be a string even if it is not a multiple of 3 or 5
##Examples
##fizz_buzz(3) ➞ "Fizz"
## 
##fizz_buzz(5) ➞ "Buzz"
## 
##fizz_buzz(15) ➞ "FizzBuzz"
## 
##fizz_buzz(4) ➞ "4"

import unittest

def checkNumber(x):
    if x % 3 == 0 and x % 5 != 0:
        return("Fizz")
    elif x % 5 == 0 and x % 3 != 0:
        return("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        return("FizzBuzz")
    else:
        x = str(x)
        return('%s' %(x))

##x = int(input('Input number: '))
##print(checkNumber(x))


import unittest

def checkNumber(x):
    if x % 3 == 0 and x % 5 != 0:
        return("Fizz")
    elif x % 5 == 0 and x % 3 != 0:
        return("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        return("FizzBuzz")
    else:
        x = str(x)
        return('%s' %(x))
    
class MyTest(unittest.TestCase):
    """My Test"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("===========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("===========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("setUp")
        print("===========")

    def tearDown(self):
        """Tear down for class"""
        print("===========")
        print("tearDownClass")

    def test_checkFizz(self):
        """Add operation test"""
        print("id: " + self.id())
        self.assertEqual(checkNumber(3),'Fizz')

    def test_checkBuzz(self):
        """Add operation test"""
        print("id: " + self.id())
        self.assertEqual(checkNumber(5),'Buzz')
        
    def test_checkFizzBuzz(self):
        """Add operation test"""
        print("id: " + self.id())
        self.assertEqual(checkNumber(15),"FizzBuzz")

    def test_checkNumber(self):
        """Add operation test"""
        print("id: " + self.id())
        self.assertEqual(checkNumber(11),'11')
        


if __name__ == '__main__':
    unittest.main()
