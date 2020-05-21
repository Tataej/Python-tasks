##11. Is the Number a Repdigit
##A repdigit is a positive number composed out of the same digit.
##Create a function that takes an integer and returns whether it's a
##repdigit or not.
##Examples
##is_repdigit(66) ➞ True
## 
##is_repdigit(0) ➞ True
## 
##is_repdigit(-11) ➞ False
##Notes
##The number 0 should return True (even though it's not a positive number).

def is_repdigit(a):
    if a > 0:
        y = len(str(a))
        x = int((str(a))[0])
        if a == (x * (10**y - 1) / 9):
            print('is_repdigit(%d) --> True' %(a))
            return True
        else:
            print('is_repdigit(%d) --> False' %(a))
            return False
    else:
        print('Inputted number is not positive')
        return None

a = int(input('Input positive number bigger than null: '))
is_repdigit(a)
