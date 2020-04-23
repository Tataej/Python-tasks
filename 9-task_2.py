##Написати функцію is_year_leap, приймає 1 аргумент -
##рік, і повертає True, якщо рік високосний, і False
##в іншому випадку


def is_year_leap():
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print("True. {0} is a leap year".format(year))
           else:
               print("False. {0} is not a leap year".format(year))
       else:
           print("True. {0} is a leap year".format(year))
    else:
       print("False. {0} is not a leap year".format(year))

year = int(input("Input an year: "))
print(is_year_leap())
