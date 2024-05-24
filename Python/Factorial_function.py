def Recursion(i):
    total=1
    while i!=0:
        total=total*i
        i-=1
    print(total)
        


n=int(input("Enter the value of n : "))

Recursion(n)