import math 
print("To find the hypotenuse of the triangle, enter")
a = float(input("1 cathet: "))
b = float(input("2 cathet: "))
a **=2
b **=2
c = math.sqrt(a+b)
print("The hypotenuse of the riangle is ",c)