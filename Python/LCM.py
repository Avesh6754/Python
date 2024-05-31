import math


def fun(gcd,a,b):
    LCM=(a*b)/gcd
    print(int(LCM))    
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
num1=a
num2=b
while(num1!=num2):
    if num1>num2:
        num1=num1-num2
    else:
        num2=num2-num1
    gcd=num1
fun(gcd,a,b)



