m = int(input("Input amount of numbers: "))

import random
line = []
for i in range(m):
    n = int(random.randint(-5,5))
    line.append(n)
    i +=1

lineP = []
lineN = []
for i in line:
    if i < 0:
        lineN.append(i)
    elif i > 0:
        lineP.append(i)

print("Random line: ", line)
print("Positive line: ", lineP)
print("Negative line: ", lineN)
