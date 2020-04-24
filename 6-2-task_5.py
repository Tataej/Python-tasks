##Заповність дві матриці заповнюються введенням з
##клавіатури. В елементи третьої матриці такої ж
##розмірності записати більші з відповідних елементів
##перших двох.


R = int(input("Input amount of rows: "))
C = int(input("Input amount of columns: "))

matrix1 = [] 
print("Enter matrix1:") 
  
for i in range(R):          
    a =[] 
    for j in range(C):      
         a.append(int(input("Number: "))) 
    matrix1.append(a) 
  

for i in range(R): 
    for j in range(C): 
        print("%5d" %(matrix1[i][j]), end = " ") 
    print()

matrix2 = [] 
print("Enter matrix2:") 
  
for x in range(R):          
    b =[] 
    for y in range(C):      
         b.append(int(input("Number: "))) 
    matrix2.append(b) 
  

for x in range(R): 
    for y in range(C): 
        print("%5d" %(matrix2[x][y]), end = " ") 
    print()
print()
print("Matrix3 from the biggest elements")

matrix3 = [] 
  
for i in range(R):          
    c =[] 
    for j in range(C):
        if matrix1[i][j] > matrix2[i][j]:
            c.append(matrix1[i][j])
        else:
            c.append(matrix2[i][j])
    matrix3.append(c) 
  

for i in range(R): 
    for j in range(C): 
        print("%5d" %(matrix3[i][j]), end = " ") 
    print() 
