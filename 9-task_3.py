##Написати функцію square, яка приймає 1 аргумент -
##сторону квадрата, і повертає 3 значення (за
##допомогою кортежу): периметр квадрата, площу
##квадрата і діагональ квадрата.


def square(a):
    import math
    if a != 0:
        return({
            "Периметр:":(4*a),
            "Площа:":(a*a),
            "Діагональ":(a*math.sqrt(2))
        })
    else:
        print("Невірне число")

a = (int(input("Введіть довжину сторони квадрату: ")))
print(square(a))

