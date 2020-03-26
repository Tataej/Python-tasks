print("Enter number:")
a = int(input())
if a > 0:
    a = str(a)
    print("The number is positive and consist from ",len(a),"digits")
elif a < 0:
    a = str(-a)
    print("The number is negative and consist from ",len(a),"digits")
elif a == 0:
    print("The number is null")
else:
    print("The mistake of input")
