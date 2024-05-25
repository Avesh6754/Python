

def Sum(a):
    if a==0:
        return 0
   
    return (a%10+Sum(int(a/10))) 

a=int(input("enter the value of a : "))
print(Sum(a))
