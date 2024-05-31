Year=int(input("Enter the year : "))
if Year % 4 ==0 and Year %100!=0 or Year %400==0:
    print("Leap year ")
else:
    print("Not a Leap Year")
