print("Enter sum of money:")
sum = int(input())
if sum > 0 and sum < 11:
    print("We can exchange one hryvnia for you")
elif sum > 10 and sum < 100:
    a = round(sum/10)
    b = (sum - a* 10)
    if b != 0:
        print("We can exchange ",a,"ten hryvnia and",b,"one hryvnia for you" )
    else:
        print("We can exchange ",a,"ten hryvnia or",sum,"one hryvnia for you" )
elif sum > 99 and sum < 200:
    c = round((sum-100)/10)
    d = sum - c - 100
    if c != 0:
        print("We can exchange one hundred and",c,"ten hryvnia and",d,"one hryvnia for you" )
    elif d == 0 and c == 0:
        print("We can exchange one hundred hryvnia for you" )
    elif c !=0 and d == 0:
        print("We can exchange one hundred and",c,"ten hryvnia for you" )
    else:
        print("We can exchange one hundred and",d,"one hryvnia for you" )
else:
    f = sum // 200 # number of 200
    h = sum - f * 200 # 
    m = h // 100 # number of 100
    n = h - m*100
    p = n // 10 # number of 10
    x = n - p * 10 # number of 1
    if m != 0 and p != 0 and x != 0:
        print("We can exchange",f," two hundred, ", m," one hundred",p,"ten hryvnia and",x,"one hryvnia for you" )
    elif m == 0 and p != 0 and x != 0:
        print("We can exchange",f," two hundred, ",p,"ten hryvnia and",x,"one hryvnia for you" )
    elif m ==0 and p == 0 and x != 0:
        print("We can exchange",f," two hundred and",x,"one hryvnia for you" )
    elif m != 0 and p == 0 and x !=0:
        print("We can exchange",f," two hundred, ", m," one hundred and",x,"one hryvnia for you" )
    elif m !=0 and p != 0 and x == 0:
        print("We can exchange",f," two hundred, ", m," one hundred",p,"ten hryvnia for you" )
    elif m !=0 and p == 0 and x == 0:
        print("We can exchange",f," two hundred, ", m," one hundred hryvnia for you" )
    else:
        print("We can exchange",f," two hundred for you" )
       

        

