##Написати функцію is_prime, яка приймає
##1 аргумент - число від 0 до 1000, і повертає
##True, якщо воно просте, і False - в іншому випадку

def is_prime(n):
    import math
    if n < 2:
        return False
    elif n == 2:
        return True
    limit = math.sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True

n = (int(input("Input number from 0 to 1000: ")))
print(is_prime(n))
