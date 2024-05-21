a=input("Enter the value of a : ")
b=input("Enter the value of b : ")
c=input("Enter the value of c : ")

if (a>b) and (a>c):
    print('A is max ')
elif (b>a) and (b>c):
    print('B is max ')
elif (c>a) and (c>b):
    print('C is max')
elif (a==b) and (b==c) and (a==c):
    print("All value are Same : ")

