##5. List of Multiples
##Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
##Examples
##list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
## 
##list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
## 
##list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
##Notes
##Notice that num is also included in the returned list.

def list_of_multiples(num, length):
    numbers = [num]
    i = 1
    for i in range(2, length+1):
        numbers.append(num*i)
        i += 1
    print("list_of_multiples(%d, %d) --> " %(num, length), numbers)
    return numbers

num = int(input("Input number 1: "))
length = int(input("Input number 2: "))
list_of_multiples(num, length)
