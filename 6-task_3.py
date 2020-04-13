m = int(input("Input amount of numbers: "))
line = [0]*m
sumL = 0
multiply = 1
for i in range(m):
    line[i] = int(input("Input number: "))
    sumL += line[i]
    multiply *= line[i]
    i +=1
print(line)
print(sumL)
print(multiply)


