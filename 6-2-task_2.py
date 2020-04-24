##Сформувати  матрицю від 0 до 999 на екран.
##Порахувати кількість двозначних чисел в ній.


from random import *
R = int(input("Input amount of rows: "))
C = int(input("Input amount of columns: "))

numbers = [0]*R
for i in range(R):
    numbers[i] = [0]*C
    
for i in range(R):
    for j in range(C):
        numbers[i][j] = randint(0,999)

counter = 0

for i in range(R):
    for j in range(C):
        print("%4d" %(numbers[i][j]), end=" ")
        if numbers[i][j] > 9 and numbers[i][j] < 100:
            counter +=1
    print()

print("In the matrix: %d of two digit numbers" %(counter))
        
