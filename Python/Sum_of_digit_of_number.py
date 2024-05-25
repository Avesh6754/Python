a=int(input("enter the value of a : "))
n=0
total=0
while a!=0:
    n=a%10
    total+=n
    a/=10
print(total)