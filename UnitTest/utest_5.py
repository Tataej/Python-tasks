##5. List of Multiples
##Create a function that takes two numbers as arguments (num, length)
##and returns a list of multiples of num up to length.
##Examples
##list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
## 
##list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
## 
##list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
##Notes
##Notice that num is also included in the returned list.

def list_of_multiples(num, length):
    numbers = [num]
    for i in range(2, length+1):
        numbers.append(num*i)
        i += 1
    print("list_of_multiples(%d, %d) --> " %(num, length), numbers)
    return numbers

##num = int(input("Input number 1: "))
##length = int(input("Input number 2: "))
##list_of_multiples(num, length)

import unittest

   
class TestList(unittest.TestCase):
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
        """Check list for (2, 4)"""
        print("id: " + self.id())
        self.assertListEqual(list_of_multiples(2, 4), [2, 4, 6, 8])

    def test_result2(self):
        """Check list for (5, 1)"""
        print("id: " + self.id())
        self.assertListEqual(list_of_multiples(4, 1), [4])
                


if __name__ == '__main__':
    unittest.main()



 


