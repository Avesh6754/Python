
GCD=0
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
smaller=0

if a>b:
    smaller=b
else:
    smaller=a

for i in range(1,smaller+1):
    if a%i==0 and b%i==0:
            GCD=i
print(GCD)
