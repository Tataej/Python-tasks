##8. Volume of a Spherical Shell
##The volume of a spherical shell is the difference between the enclosed
##volume of the outer sphere and the enclosed volume of the inner sphere:
##Create a function that takes r1 and r2 as arguments and returns the volume
##of a spherical shell rounded to the nearest thousandth.
##
##Examples
##vol_shell(3, 3) ➞ 0
## 
##vol_shell(7, 2) ➞ 1403.245
## 
##vol_shell(3, 800) ➞ 2144660471.753
##Notes
##The inputs are always positive numbers. r1 could be the inner radius or the outer radius, don't return a negative number.
##

import math

def vol_shell(r1, r2):
    if r1 > 0 and r2 > 0:
        vol1 = 4 / 3 * math.pi * r1**3
        vol2 = 4 / 3 * math.pi * r2**3
        if vol1 > vol2:
            vol = vol1 - vol2
            print("vol_shell(%d, %d) --> %.3f" %(r1, r2, vol))
            return ("%.3f" %(vol))
        elif vol1 < vol2:
            vol = vol2 - vol1
            print("vol_shell(%d, %d) --> %.3f" %(r1, r2, vol))
            return ("%.3f" %(vol))
        else:
            print("The volume of a spherical shell = 0")
            return None
    else:
        print("The entered number are incorrect")


r1 = int(input("Input radius 1: "))
r2 = int(input("Input radius 2: "))
vol_shell(r1, r2)
