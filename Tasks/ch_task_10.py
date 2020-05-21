##10. Stupid Addition
##Create a function that takes two parameters and, if both parameters are
##strings, add them as if they were integers or if the two parameters are
##integers, concatenate them.
##Examples
##stupid_addition(1, 2) ➞ "12"
## 
##stupid_addition("1", "2") ➞ 3
## 
##stupid_addition("1", 2) ➞ None
##Notes
##If the two parameters are different data types, return None.
##All parameters will either be strings or integers.


def stupid_addition(a, b):
    if type(a) == str and type(b) == str:
        d = int(b)
        c = int(a)
        print('stupid_addition("%s", "%s") ➞ ' %(a, b),(c+d))
        return(c+d)
    elif type(a) == int and type(b) == int:
        c = str(a)
        d = str(b)
        print('stupid_addition("%s", "%s") ➞ ' %(a, b),(c+d))
        return(c+d)
    else:
        print("stupid_addition(", a, ", ", b, ') ➞ None' )
        return(None)



