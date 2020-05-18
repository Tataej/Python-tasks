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

format_date(date = input('Input date in format month/day/year: '))


   




 

