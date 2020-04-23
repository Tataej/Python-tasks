##Написати функцію date, яка приймає 3 аргументи -
##день, місяць, рік. повернути True, якщо така
##дата є в нашому календарі, і False - в іншому
##випадку


def date(d,m,y):
        # задаем месяцы по кол-ву дней
    m31 = (1, 3, 5, 7, 8, 10, 12)
    m30 = (4, 6, 9, 11)
    # если год високосный
    if y %4 == 0:
        # проверяем попадает ли месяц и день в лимиты
        if m == 2 and 0 < d <= 29:
            print(True)
        elif m in m31 and 0 < d <= 31:
            print(True)
        elif m in m30 and 0 < d <= 30:
            print(True)
        else:
            print(False)
    # если год обычный
    elif y %4 != 0:
        # проверяем попадает ли месяц и день в лимиты
        if m ==2 and 0 < d < 28:
            print(True)
        elif m in m31 and 0 < d <= 31:
            print(True)
        elif m in m30 and 0 < d <= 30:
            print(True)
        else:
            print(False)
    else:
        print(False)

d = (int(input("Input the day: ")))
m = (int(input("Input the month: ")))
y = (int(input("Input the year: ")))
print(date(d,m,y))
