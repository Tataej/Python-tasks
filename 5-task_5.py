import random
print("input ten numbers not bigger than 100:")
numbers = list(map(int, input (). split ()))

P = random.randrange(101)
H = random.randrange(101)
print("Your numbers are: ",numbers[0:10]," and numbers %d and %d for comparative" %(P,H))

sumNum = 0
multNum = 0
counter = 0
if P > H:
    P, H = H, P

for i in range(numbers):    
    while numbers[i] != P or numbers[i] != H:
    
        if numbers[i] < P:
            sumNum += numbers[i]
            print("Sum of numbers which are less than %d is " %(P))
            i +=1,
        elif numbers[i] > H:
            multNum += numbers[i]
            i +=1
        else:
            counter += 1

        





#print('H=',H)
