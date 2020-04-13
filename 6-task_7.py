N = int(input("Input amount of numbers: "))

import random
line = []

for i in range(0,N):
    x = int(random.randint(0,100))
    line.append(x)
uniq = set(line)    
      
print('Randome line: ', line)
print('Unique numbers: ', uniq)
