##24. Buggy Uppercase Counting
##In the Code tab is a function which is meant to return how
##many uppercase letters there are in a list of various words.
##Fix the list comprehension so that the code functions normally!
##Examples
##count_uppercase(['SOLO', 'hello', 'Tea', 'wHat']) ➞ 6
## 
##count_uppercase(['little', 'lower', 'down']) ➞ 0
## 
##count_uppercase(['EDAbit', 'Educate', 'Coding']) ➞ 5


def count_uppercase(x):
    count = 0
    i = 0
    for i in x:
        result = 0
        for j in i:
            j = [j]
            for y in j:
                y = str(y)
                if y.isupper():
                    result +=1
        count += result
    print('count_uppercase(',x,') --> %d' %(count))
    return(count)



count_uppercase(['SOLO', 'hello', 'Tea', 'wHat']) 
 
count_uppercase(['little', 'lower', 'down']) 
 
count_uppercase(['EDAbit', 'Educate', 'Coding'])
