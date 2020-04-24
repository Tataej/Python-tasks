##Змінити послідовність стовпців матриці
##так, щоб елементи її першого рядка
##були відсортовані за зростанням

from random import *
N = int(input("Input amount of rows: "))
M = int(input("Input amount of columns: "))

a = []
for i in range(N):
    z = []
    for j in range(M):
        n = int(random() * 50) - 25
        z.append(n)
        print("%4d" % n, end='')
    print()
    a.append(z)
print()
 
k = M-1
while k > 0:
    ind = 0
    for j in range(k+1):
        if a[0][j] > a[0][ind]:
            ind = j
    for i in range(N):
        m = a[i][ind]
        a[i][ind] = a[i][k]
        a[i][k] = m
    k -= 1
 
for i in range(N):
    for j in range(M):
        print("%4d" % a[i][j], end='')
    print()
