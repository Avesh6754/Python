n=int(input("Enter the value of n : "))

total=0
Or=n
F=0
while Or!=0:
    F=Or%10
    total=(total*10)+F
    Or//=10
print(total)
