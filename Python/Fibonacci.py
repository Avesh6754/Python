a=input("Enter the value of a ")
b=1
i=-1
ans=0
while(i<int(a)):
   ans=i+b
   i=b
   b=ans
   print(b) 