##Знайти максимальний елемент серед мінімальних
##елементві стовпів матриці.

import random
M = int(input("Input amount of rows: "))
N = int(input("Input amount of columns: "))
matrix = [[random.randrange(0,999) for y in range(M)] for x in range(N)]

minL = []
minNum = 0

for i in range(M):
    for j in range(N):
        print("%4d" %(matrix[i][j]), end=" ")
        
    print()

for j in range(N):
    num = []
    for i in range(M):
        num.append(matrix[i][j])
        minNum = min(num)
    minL.append(minNum)
print("Max from min of columns is %d" %(max(minL)))
    
