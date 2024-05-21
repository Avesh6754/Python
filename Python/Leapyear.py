Year=input("Enter the year : ")
if int(Year)%4==0 and int(Year)%100!=0 or int(Year)%400==0:
    print("Leap year ")
else:
    print("Not a Leap Year")