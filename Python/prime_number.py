a=input("Enter the value of a ")
ans=1
if a==1:
    print("not prime number : ")

else:
    for x in range(2,int(a)+1):
        if(int(a)%x==0):
            print(" Not Prime number : ")
            break
        else:
            print("Prime number : ")
            break

        

    