x = int(input("how many hours a week do you work?"))
y = float(input("what is your hourly wage?"))

average_hours = 40
min_hourly_pay = 8.50


print("your gross weekly income is:", "€", x*y,"\n", "your annual income is:", "€", (x*y)*52, sep = "")
if (x > 40):
    print( "you work %d hours more than the average person" % (x - average_hours))
elif (x == 40):
    print("you work the same amount of hours as the average person(40)")
else:
    print( "you work %d hours less than the average person" % (average_hours - x))
if (y > min_hourly_pay):
    print( "you earn %d€ more than the minimumm wage" % (y - min_hourly_pay))
else:
    print( "you earn %d€ less than the minimum wage" % (min_hourly_pay - y))