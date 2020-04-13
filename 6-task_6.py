N = int(input("Input amount of numbers: "))

import random
line = []
even = []

for i in range(0,N):
    x = int(random.randint(0,100))
    line.append(x)
    if x % 2 == 0:
        even.append(i)
print('Randome line: ', line)
print('Indexes of even numbers: ', even)
