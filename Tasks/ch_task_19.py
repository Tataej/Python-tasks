##19. Oddish vs. Evenish
##Create a function that determines whether a number is Oddish or Evenish.
##A number is Oddish if the sum of all of its digits is odd, and a number
##is Evenish if the sum of all of its digits is even. If a number is Oddish,
##return "Oddish". Otherwise, return "Evenish".
##For example, oddish_or_evenish(121) should return "Evenish",
##since 1 + 2 + 1 = 4. oddish_or_evenish(41) should return "Oddish",
##since 4 + 1 = 5.
##Examples
##oddish_or_evenish(43) ➞ "Oddish"
## 
##oddish_or_evenish(373) ➞ "Oddish"
## 
##oddish_or_evenish(4433) ➞ "Evenish"

def oddish_or_evenish(a):
    n = a
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    if tot %2 == 0:
        print('oddish_or_evenish(%d) --> "Oddish"' %(a))
        return('Oddish')
    else:
        print('oddish_or_evenish(%d) --> "Evenish"' %(a))
        return('Oddish')


oddish_or_evenish(43)
oddish_or_evenish(4433)

