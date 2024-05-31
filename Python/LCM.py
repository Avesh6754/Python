
LCM=0
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
great=0

if a>b:
    great=a
else:
    great=b

while(True):
    if(great%a==0)and(great%b==0):
        LCM=great
        break
    great+=1

print(LCM)
