def Recursion(i):
    if i==1:
        return 1
    else:
        return i*Recursion(i-1)

n=int(input("Enter the value of n : "))

print(Recursion(n))