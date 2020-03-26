print("Choose figure (1 - rectangle, 2 - triangle, 3 - circle):  ")
figure = input()
 
if figure == '1':
	print("The length of rectangle sides:")
	a = float(input("a = "))
	b = float(input("b = "))
	print("The square: %.2f" % (a*b))
elif figure == '2':
	print("The length of triangle sides: ")
	a = float(input("a = "))
	b = float(input("b = "))
	c = float(input("c = "))
	p = (a + b + c) / 2
	import math
	s = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print("The square:", s)
elif figure == '3':
	r = float(input("Radius of circle R = "))
	import math
	print("The square: %.2f" % (math.pi*r**2))
else:
	print("A mistake of input")
    
