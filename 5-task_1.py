print('You need to guess the number from 0 to 100. You have 10 attempts: ')

x = 0
import random
b = random.randint(0, 100)
while x<10:
    a = int(input('Input number: '))
    if a >= b:
        print('Your number is greater. Try again!')
    elif a<=b:
        print('Your number is less. Try again!')
    else:
        print('You are winner!')
    
    x += 1 

print('Your attempts are ended')
    
