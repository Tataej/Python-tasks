##Користувач робить внесок в розмірі n
##гривень строком на years років під 10%
##річних (щороку розмір його внеску
##збільшується на 10%. Ці гроші додаються
##до суми вкладу, і на них в наступному
##році теж будуть відсотки).

##Написати функцію bank, яка приймає аргументи
##n і years, і повертає суму, яка буде на
##рахунку користувача


def bank(n,years):
    d=n
    for i in range(0,years):
        d = float(d + d/10)
        n = round(d,2)
        i +=1
    return(n)

n = (float(input("Input the amount of money: ")))
years = (int(input("Input the amount of years for deposit: ")))
print(bank(n,years))
