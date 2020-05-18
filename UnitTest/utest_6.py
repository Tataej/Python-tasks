##6. Date Format
##Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
##Examples
##format_date("11/12/2019") ➞ "20191211"
## 
##format_date("12/31/2019") ➞ "20193112"
## 
##format_date("01/15/2019") ➞ "20191501"
##Notes
##Return value should be a string.
##

from datetime import datetime

def format_date(date):
    dateD = datetime.strptime(date, "%m/%d/%Y")
    dateF = datetime.strftime(dateD, "%Y%d%m")
    print("format_date (%s) --> %s" %(date, dateF))
    return(dateF)

#format_date(date = input('Input date in format month/day/year: '))


import unittest

   
class TestDateFormat(unittest.TestCase):
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

    def test_format_date(self):
        """Check when result = 1"""
        print("id: " + self.id())
        self.assertEqual(format_date('12/31/2019'), '20193112')

        


if __name__ == '__main__':
    unittest.main()



 

