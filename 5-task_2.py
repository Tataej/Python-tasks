print('Enter ten two-digit number: ') 
x = (input())
x = x.split()
x = [int(item) for item in x]

for i in range(len(x)):
   if x[i] %5 == 0:
       print(x[i])
  
       



    
