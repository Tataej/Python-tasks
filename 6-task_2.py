from random import *

n = int(input("N = "))

numbers = []
for i in range(n+1):
    numbers.append(randint(-5,4))
print(numbers)
print("***********")

countersPositive = 0
numbersPositive = []
for i in numbers:
    if numbers[i] > 0:
        numbersPositive.append(numbers[i])
        countersPositive += 1
        i +=1
print(numbersPositive)

#print("max count for %d " %(numbers[counters.index(max(counters))]))
