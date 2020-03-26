import math 
print("Enter the area of the square hall:")
s = int(input())
print("Enter the stage radius:")
r = int(input())
print("Enter the desired distance from the wall to the stage:")
k = int(input())
w = round(math.sqrt(s))
d = r * 2
if k > (w-d):
    print("The distance from the wall to the stage is bigger than the desired one")
elif k == (w-d):
    print("There is the desired distance from the wall to the stage")
elif k < (w-d):
    print("There isn't the desired distance from the wall to the stage")
else:
    print("The mistake of input")
