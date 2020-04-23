##Написати функцію arithmetic, яка приймає
##три аргументи: перші 2 - числа, третій -
##операцію, яка повинна бути здійснена над
##ними. Якщо третій аргумент +, то додати
##їх якщо -, то відняти; *-помножити;
##/-розділити (перше на друге). В інших
##випадках повернути рядок "Невідома операція". 

def arithmetic():
        if c == "+":
            summ = a + b
            return(summ)
        elif c == "-":
            differ = a - b
            return(differ)
        elif c == "*":
            multi = a * b
            return(multi)
        elif c == "/":
            if b != 0:
                divis = a / b
                return(divis)
            else:
                return("Cannot be divided by zero")
        else:
            return("Unknown operation")

print("For arithmetic, enter two numbers and the arithmetic sign +, -, * or /")
a = (int(input("Input the first number: ")))
b = (int(input("Input the second number: ")))
c = (input("Input the arithmetic sign: "))
print(arithmetic())

