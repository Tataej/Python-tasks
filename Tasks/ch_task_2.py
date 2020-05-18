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

import unittest

def profit(params):
    profit = 0
    if params['cost_price'] > 0 and params["sell_price"] > 0 and params["inventory"] >0:
        profit = int(round((params["sell_price"] - params["cost_price"]) * params["inventory"]))
        print('Profit ({')
        for key in prof:
            print("{}: {}".format(key, params[key]))
        print('}) --> ',profit)
        return profit
    else:
        print('The mistake of inputting data')
        return None

x = float(input('Input cost_price: '))
y = float(input('Input sell_price: '))
z = int(input('Input amount of inventory: '))
prof ={"cost_price": x, "sell_price": y, "inventory": z}
profit(prof)
print(prof)
        
