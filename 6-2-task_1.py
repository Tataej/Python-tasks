##Порахувати суми кожного рядка і кожного
##стовпця матриці. Доповнити її стовпцем,
##який містить суми елементів рядків та
##рядком, елементами якого є суми елементів
##стовпців.
       
from random import *
R = int(input("Input amount of rows: "))
C = int(input("Input amount of columns: "))

a = []
for i in range(R):
    b = []
    for j in range(C):
        b.append(int(random()*11))
        print("%3d" % b[j], end='')
    a.append(b)
    print('   |', sum(b))
 
##for i in range(R):
##    print(" --", end='')
##print()
## 
##for i in range(R):
##    s = 0
##    for j in range(C):
##        s += a[j][i]
##    print("%3d" % s, end='')
##print()

