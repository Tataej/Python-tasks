N = int(input("Input amount of numbers: "))

import random
line = []

for i in range(0,N):
    x = int(random.randint(0,100))
    line.append(x)
a = min(line)
b = max(line)
line = sorted(line)
print('Randome line: ', line)
line[0], line[-1] = line[-1], line[0]
print('Randome line: ', line)

