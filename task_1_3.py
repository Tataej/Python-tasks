year = int(input("Input an year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year,".format(year),round(year / 100 + 1)," century"),
       else:
           print("{0} is not a leap year,".format(year),round(year / 100 + 1)," century")
   else:
       print("{0} is a leap year,".format(year),round(year / 100 + 1)," century")
else:
   print("{0} is not a leap year,".format(year),round(year / 100 + 1)," century")
