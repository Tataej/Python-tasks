rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))

print("Rectangle Star Pattern")
print('X '*columns)
print()
for i in range(rows-2):
    print('X'+' @'*(columns-2)+' X')
    print()
print('X '*columns)
      
