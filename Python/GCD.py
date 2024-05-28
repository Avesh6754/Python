def fun(a,b):
    while b!=0:
        a=b
        b=(a%b)
    return a

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
print(fun(a,b))