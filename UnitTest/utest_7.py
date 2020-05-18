##7. Check If Lines Are Parallel
##Given two lines, determine whether or not they are parallel.
##Lines are represented by a list [a, b, c], which corresponds to
##the line ax+by=c.
##Examples
##lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ true
### x+2y=3 and x+2y=4 are parallel.
## 
##lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ false
### 2x+4y=1 and 4x+2y=1 are not parallel.
## 
##lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ true
### Lines are parallel to themselves.
##Notes
##All the coefficients will be integers (whole numbers).

def lines_are_parallel(line1, line2):
  if(line1[1]!=0 and line2[1]!=0):
    if(line1[0]/line1[1]==line2[0]/line2[1]):
      print("lines_are_parallel({},{}".format(line1,line2),") --> true")
      return True
    else:
      print("lines_are_parallel({},{}".format(line1,line2),") --> false")
      return False
  else:
    if(line1[0]==line2[0] and line1[1]==line2[1]):
      print("lines_are_parallel({},{}".format(line1,line2),") --> true")
      return True
    else:
      print("lines_are_parallel({},{}".format(line1,line2),") --> false")
      return False
    
##line1=[]
##line2=[]
##print("Enter the values of a1 b1 c1 :")
##for i in range(3):
##        x=int(input())
##        line1.append(x)  
##print("Enter the values of a2 b2 c2 :")
##for i in range(3):
##        x=int(input())
##        line2.append(x) 
##
##lines_are_parallel(line1, line2)


import unittest

   
class TestParallelLines(unittest.TestCase):
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

    def test_line_are_parralel(self):
        """Check lines are parallel"""
        print("id: " + self.id())
        self.assertEqual(lines_are_parallel([1, 2, 3],[1, 2, 4]), True)

    def test_line_not_parralel(self):
        """Check lines are not parallel"""
        print("id: " + self.id())
        self.assertEqual(lines_are_parallel([2, 4, 1],[1, 4, 2]), False)

        


if __name__ == '__main__':
    unittest.main()

