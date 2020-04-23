##Написати функцію season, яка приймає
##1 аргумент - номер місяця (від 1 до 12),
##і повертає пору року, якій цей місяць
##належить (зима, весна, літо або осінь).

def season(a):
    if a>0 and a<=2 or a==12:
        return ("Winter")
    elif a>2 and a<=5:
        return ("Spring")
    elif a>5 and a <=8:
        return ("Summer")
    elif a>8 and a<12:
        return ("Autumn")
    else:
        return ("There is no such month")
    
a = (int(input("Input the number of month: ")))
print(season(a))
