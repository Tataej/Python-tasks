##2. Calculate the Profit
##You work for a manufacturer, and have been asked to calculate
##the total profit made on the sales of a product. You are given
##a dictionary containing the cost price per unit (in dollars),
##sell price per unit (in dollars), and the starting inventory.
##Return the total profit made, rounded to the nearest dollar.
##Assume all of the inventory has been sold.
##Examples
##profit({
##  "cost_price": 32.67,
##  "sell_price": 45.00,
##  "inventory": 1200
##}) ➞ 14796
## 
##profit({
##  "cost_price": 225.89,
##  "sell_price": 550.00,
##  "inventory": 100
##}) ➞ 32411
## 
##profit({
##  "cost_price": 2.77,
##  "sell_price": 7.95,
##  "inventory": 8500
##}) ➞ 44030
##Notes
##Profit = Total Sales - Total Cost

def profit(params):
    profit = 0
    if params['cost_price'] > 0 and params["sell_price"] > 0 and params["inventory"] >0:
        profit = int(round((params["sell_price"] - params["cost_price"]) * params["inventory"]))
        print('Profit ({')
        for key in params:
            print("{}: {}".format(key, params[key]))
        print('}) --> ',profit)
        return profit
    else:
        print('The mistake of inputting data')
        return None

##cost_price = float(input('Input cost_price: '))
##sell_price = float(input('Input sell_price: '))
##inventory = int(input('Input amount of inventory: '))
##params ={"cost_price": cost_price, "sell_price": sell_price, "inventory": inventory}
##profit(params)


import unittest
  
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

    def test_profit1(self):
        """Check profit"""
        params = {"cost_price": 2.85, "sell_price": 5.0, "inventory": 183.0}
        print("id: " + self.id())
        self.assertEqual(profit(params),393)
              
    def test_profit2(self):
        """Check profit"""
        params = {"cost_price": 1, "sell_price": 3, "inventory": 30}
        print("id: " + self.id())
        self.assertNotEqual(profit(params),20)

    def test_profit3(self):
        """Check profit"""
        params = {"cost_price": 0, "sell_price": 3, "inventory": 30}
        print("id: " + self.id())
        self.assertNotEqual(profit(params),20)
     

        


if __name__ == '__main__':
    unittest.main()
       
